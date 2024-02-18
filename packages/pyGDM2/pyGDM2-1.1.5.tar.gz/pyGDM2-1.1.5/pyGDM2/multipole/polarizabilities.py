# encoding: utf-8
#
#Copyright (C) 2017-2024, P. R. Wiecha
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
tools around multipole decomposition and effective polarizabilities

"""
from __future__ import print_function
from __future__ import absolute_import

import warnings
import time
import numpy as np
import copy

from pyGDM2.multipole.main import multipole_decomposition_exact



#==============================================================================
# GLOBAL PARAMETERS
#==============================================================================
DTYPE_C = np.complex64




#==============================================================================
# EXCEPTIONS
#==============================================================================



# =============================================================================
# CONSISTENCY TESTS / HELPER
# =============================================================================
def _test_availability_generalized_polarizability(sim, which_moment, wavelength, 
                      method='lu', verbose=False, long_wavelength_approx=False):
    which_moment = which_moment.lower()
    wl = wavelength
    
    calc_gp = False
    if which_moment in ['p1', 'p0', 'p']:
        if not hasattr(sim, 'K_P_E'):
            calc_gp = True
        elif wl not in sim.K_P_E.keys():
            calc_gp = True
            
    if which_moment in ['pt', 'p']:
        if not hasattr(sim, 'K_T_E'):
            calc_gp = True
        elif wl not in sim.K_T_E.keys():
            calc_gp = True
            
    if which_moment == 'm':
        if not hasattr(sim, 'K_M_E'):
            calc_gp = True
        elif wl not in sim.K_M_E.keys():
            calc_gp = True
            
    if which_moment in ['qe1', 'qe0', 'qe']:
        if not hasattr(sim, 'K_QE_E'):
            calc_gp = True
        elif wl not in sim.K_QE_E.keys():
            calc_gp = True
            
    if which_moment in ['qet', 'qe']:
        if not hasattr(sim, 'K_QT_E'):
            calc_gp = True
        elif wl not in sim.K_QT_E.keys():
            calc_gp = True
            
    if which_moment == 'qm':
        if not hasattr(sim, 'K_QM_E'):
            calc_gp = True
        elif wl not in sim.K_QM_E.keys():
            calc_gp = True
    
    if calc_gp:
        if verbose:
            warnings.warn('generalized polarizabilities not available. evaluating...')
        generalized_polarizability(sim, wavelength=wl, method=method, 
                                   long_wavelength_approx=long_wavelength_approx)



# =============================================================================
# MODULE FUNCTIONS
# =============================================================================
def generalized_polarizability(sim, field_index=None, wavelength=None, 
                               method='lu', epsilon=0.01, r0=None,
                               which_moments=['p1', 'pt', 'qe', 'qt', 'm', 'qm'],
                               long_wavelength_approx=False, verbose=1):
    """generalized electric and magnetic polarizabilities
    
    ** ------- FUNCTION STILL UNDER TESTING ------- **
    
    Returns the generalized polarizability tensors that can be used with arbitrary,
    inhomogeneous illumination fields to calculate the effective 
    electric and magnetic multipole moments, induced in the nanostructure.
    
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int, default: None
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`.
        Either `field_index` or `wavelength` must be given.
    
    wavelength : float, default: None
        Optional wavelength (alternative to `field_index`) at which to 
        calculate susceptibility matrix (in nm). 
        Either `field_index` or `wavelength` must be given.
    
    method : string, default: "scipyinv"
        inversion method. One of ["lu", "numpyinv", "scipyinv", "cupy", "cuda"]
         - "scipyinv" scipy default inversion (`scipy.linalg.inv`)
         - "numpyinv" numpy inversion (`np.linalg.inv`, if numpy compiled accordingly: LAPACK's `dgesv`)
         - "cupy" uses CUDA GPU via `cupy`
         - "cuda" (equivalent to "cupy")
         - "lu" LU-decomposition (`scipy.linalg.lu_factor`) - inefficient for `decay_rate`!
    
    epsilon : float, default: 0.01
        additional step on r0 (in nm) to avoid numerical divergence of the Bessel terms
        
    r0 : array, default: None
        [x,y,z] position of mulipole decomposition development. 
        If `None`, use structure's center of gravity
    
    which_moments : list of str, default: ['p1', 'pt', 'qe1', 'qt', 'm', 'qm']
        which generalized polarizability tensors to calculate and return. supported:
            - 'p1': electric dipole - only first order (rank 2)
            - 'pt': toroidal dipole (rank 3)
            - 'qe1': electric quadrupole - only first order (rank 4)
            - 'qt': toroidal electric quadrupole (rank 4)
            - 'm': magnetic dipole (rank 2)
            - 'qm': magnetic quadrupole (rank 3)
            
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation
        
    verbose : bool default=True
        print runtime info
    
    
    Returns
    -------
    
    by default 6 lists of N tensors, with N the number of discretization cells (see kwarg `which_moments`):
        
    K_P_E, K_T_E, K_QE_E, K_QT_E, K_M_E, K_QM_E
    
    Notes
    -----
    For details , see: 
        
    *PAPER SUBMITTED*
    
    For details about the underlying exact multipole decomposition, see: 
        
    Alaee, R., Rockstuhl, C. & Fernandez-Corbaton, I. *An electromagnetic 
    multipole expansion beyond the long-wavelength approximation.*
    Optics Communications 407, 17–21 (2018)
    
    """
    # =============================================================================
    #     Exception handling
    # =============================================================================
    if field_index is None and wavelength is None:
        raise Exception("Either `field_index` or `wavelength` must be given!")
        
    if field_index is not None and wavelength is not None:
        warnings.warn("`field_index` AND `wavelength` are given! Ignoring `wavelength`.")
        
    
    
    # =============================================================================
    # preparation
    # =============================================================================
    from pyGDM2 import core
    
    which_moments = [wm.lower() for wm in which_moments]
    
    if field_index is not None:
        from pyGDM2 import tools
        wavelength = tools.get_field_indices(sim)[field_index]['wavelength']
    
    if 'p1' in which_moments and not hasattr(sim, 'K_P_E'):
        sim.K_P_E = dict()
    if 'pt' in which_moments and not hasattr(sim, 'K_T_E'):
        sim.K_T_E = dict()
    if 'qe' in which_moments and not hasattr(sim, 'K_QE_E'):
        sim.K_QE_E = dict()
    if 'qt' in which_moments and not hasattr(sim, 'K_QT_E'):
        sim.K_QT_E = dict()
    if 'm' in which_moments and not hasattr(sim, 'K_M_E'):
        sim.K_M_E = dict()
    if 'qm' in which_moments and not hasattr(sim, 'K_QM_E'):
        sim.K_QM_E = dict()
    
    
    
    if verbose:
        t0 = time.time()
        print("wl={}nm. calc. K:".format(np.round(wavelength, 1)), end='')
    
    
    ## structure
    geo = sim.struct.geometry
    alpha = sim.dyads.getPolarizabilityTensor(wavelength, sim.struct)
    if r0 is None:
        r0 = np.average(geo, axis=0)
    sim.r0 = r0
    if np.abs(np.linalg.norm(geo - r0, axis=1)).min() > epsilon:
        epsilon = 0
    Dr = geo - r0  #   = r-r0
    norm_r = np.linalg.norm(Dr + epsilon, axis=1)  # epsilon: avoid divergence of 1/kr at r=0
    norm_r2 = norm_r**2
    
    ## illumination properties
    sim.struct.setWavelength(wavelength)
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, r0[None,:])[0]  # assume structure is fully in one environment
    n_env = eps_env**0.5
    k0 = 2.0*np.pi / wavelength
    k = k0*n_env
    kr = k * norm_r
    
    ## bessel functions and pre-factors
    if not long_wavelength_approx:
        from scipy.special import spherical_jn as sph_jn
        j0kr = sph_jn(0, kr)
        j1kr = sph_jn(1, kr) / kr
        j2kr = sph_jn(2, kr) / (kr**2)
        j3kr = sph_jn(3, kr) / (kr**3)
        f_pt = 1/2; f_ptA=3; f_ptB=-1
        f_qe = 3; fqe2=2; fqe2A = 5; fqe2B = -1; fqe2C = -1
        f_m = 3/2; f_qm = 15
    else:
        j0kr = j1kr = j2kr = j3kr = np.ones_like(kr)
        f_pt = 1/10; f_ptA=1; f_ptB=-2
        f_qe = 1; fqe2=1/14; fqe2A = 4; fqe2B = -5; fqe2C = 2
        f_m = 1/2; f_qm = 1
    
    
    ## ----- gen. propagator
    K = core.get_general_propagator(sim, wavelength, method=method)
    if method.lower() in ['cupy', 'cuda']:
        K = K.get()
    if method.lower() == 'lu':
        import scipy.linalg as la
        K = la.lu_solve(K, np.identity(K[0].shape[0], dtype=K[0].dtype))
        
    if verbose:
        t1 = time.time()
        print(" {:.1f}ms.  electric... ".format((t1-t0)*1000), end='')
    K2 = K.reshape(len(K)//3, 3, -1, 3).swapaxes(1,2).reshape(-1, 3, 3).reshape(len(K)//3,len(K)//3, 3, 3)
    K2a = np.matmul(alpha[:,None,...], K2)
    Ka = np.concatenate(np.concatenate(K2a, axis=1), axis=1)


# =============================================================================
#     electric-electric
# =============================================================================
    ## ----- electric-electric generalized polarizability - dipole
    if 'p1' in which_moments:
        K_P_E = np.sum(K2a * j0kr[:,None,None,None], axis=0)
        sim.K_P_E[wavelength] = K_P_E       # store in simulation object


    ## ----- higher order electric moments
    if 'pt' in which_moments or 'qe' in which_moments or 'qt' in which_moments:
        K_re = np.zeros_like(Ka)
        for i_dp in range(len(Ka)):
            K_re.T[i_dp] = (Dr * Ka.T[i_dp].reshape((len(Ka)//3,3))).reshape((len(Ka),))
        K2_re = K_re.reshape(len(Ka)//3, 3, -1, 3).swapaxes(1,2).reshape(-1, 3, 3).reshape(len(Ka)//3,len(Ka)//3, 3, 3)
            
        
    ## ----- toroidal dipole generalized polarizability 
    if 'pt' in which_moments:
        Qt1 = np.zeros((len(Ka)//3,3,3,3), dtype=np.complex64)
        Qt2 = np.zeros((len(Ka)//3,3,3), dtype=np.complex64)
        for i_a in range(3):
            for i_b in range(3):
                Qt1[:, i_a, i_b] = np.sum(
                    (
                    K2_re[...,i_b,:] * Dr[:,i_a,None,None]
                      ) * j2kr[:, None, None], axis=0)
            Qt2[:, i_a] = np.sum(
                (K2a[...,i_a,:]) * norm_r2[:,None,None]* j2kr[:, None, None], axis=0)
                
        K_T1_E = k**2 * f_pt * f_ptA * Qt1 
        K_T2_E = k**2 * f_pt * f_ptB * Qt2
    
        K_T_E = K_T1_E + K_T2_E[...,None,:]/3
        sim.K_T_E[wavelength] = K_T_E       # store in simulation object


    ## ----- electric quadrupole generalized polarizability 
    krondelta = np.identity(3)
    if 'qe' in which_moments:
        Qe11 = np.zeros((len(Ka)//3,3,3,3), dtype=np.complex64)
        Qe12 = np.zeros((len(Ka)//3,3,3,3,3), dtype=np.complex64)

        for i_a in range(3):
            for i_b in range(3):
                Qe11[:, i_a, i_b] = np.sum(
                    (
                    3*(Dr[:,i_b,None,None] * K2a[...,i_a,:] +
                       Dr[:,i_a,None,None] * K2a[...,i_b,:])
                      ) * j1kr[:, None,None], axis=0)
                
                for i_c in range(3):  # keep separate scalar product elements in last index
                    Qe12[:, i_a, i_b, i_c] = np.sum(
                        (
                        - 2*K2_re[...,i_c,:] * krondelta[i_a,i_b]   # diagonal term
                          ) * j1kr[:, None,None], axis=0)
        
        K_QE_E = f_qe * (Qe12 + Qe11[...,None,:]/3)
        sim.K_QE_E[wavelength] = K_QE_E
    
    
    ## ----- electric toroidal quadrupole generalized polarizability 
    if 'qt' in which_moments:
        Qet1 = np.zeros((len(Ka)//3,3,3,3,3), dtype=np.complex64)
        Qet2 = np.zeros((len(Ka)//3,3,3,3), dtype=np.complex64)
        Qet3 = np.zeros((len(Ka)//3,3,3,3,3), dtype=np.complex64)

        for i_a in range(3):
            for i_b in range(3):
                Qet2[:, i_a, i_b] = np.sum(
                    (
                    fqe2B * (Dr[:,i_a,None,None] * K2a[...,i_b,:] + Dr[:,i_b,None,None] * K2a[...,i_a,:])
                      ) * norm_r2[:,None,None] * j3kr[:, None,None], axis=0)
                
                for i_c in range(3):  # keep separate scalar product elements in last index
                    Qet1[:, i_a, i_b, i_c] = np.sum(
                        (
                         fqe2A * K2_re[...,i_c,:] * Dr[:,i_a,None,None] * Dr[:,i_b,None,None]
                          ) * j3kr[:, None,None], axis=0)
                    Qet3[:, i_a, i_b, i_c] = np.sum(
                        (
                         fqe2C * K2_re[...,i_c,:] * krondelta[i_a,i_b]  # diagonal term
                          ) * norm_r2[:,None,None] * j3kr[:, None,None], axis=0)
        K_QT_E = f_qe * fqe2 * k**2 * (Qet1 + Qet2[...,None,:]/3 + Qet3)
        sim.K_QT_E[wavelength] = K_QT_E



# =============================================================================
#     electric-magnetic
# =============================================================================
    if 'm' in which_moments or 'qm' in which_moments:
        if verbose:
            t2 = time.time()
            print("{:.1f}ms.  magnetic... ".format((t2-t1)*1000), end='')
        K_he = np.zeros_like(Ka)
        for i_dp in range(len(Ka)):
            K_he.T[i_dp] = np.cross(Dr, Ka.T[i_dp].reshape((len(Ka)//3,3))).reshape((len(Ka),))
        K2_he = K_he.reshape(len(Ka)//3, 3, -1, 3).swapaxes(1,2).reshape(-1, 3, 3).reshape(len(Ka)//3,len(Ka)//3, 3, 3)
    
    
    ## ----- electric-magnetic generalized polarizability         
    if 'm' in which_moments:
        K_M_E = np.sum(K2_he * j1kr[:, None, None, None], axis=0)
        K_M_E = -1j*k * f_m * K_M_E
        sim.K_M_E[wavelength] = K_M_E       # store in simulation object


    ## ----- electric-magnetic quadrupole generalized polarizability
    if 'qm' in which_moments:
        Qm = np.zeros((len(Ka)//3,3,3,3), dtype=np.complex64)
        for i_a in range(3):
            for i_b in range(3):
                Qm[:, i_a, i_b] = np.sum(
                    (
                    Dr[:,i_a,None,None] * K2_he[...,i_b,:]  + 
                    Dr[:,i_b,None,None] * K2_he[...,i_a,:] 
                      ) * j2kr[:, None, None], axis=0)
                
        K_QM_E = -1j*k * f_qm * Qm 
        sim.K_QM_E[wavelength] = K_QM_E       # store in simulation object
    
    
    if verbose: 
        print("{:.1f}ms. Done.".format((time.time()-t2)*1000))
    
# =============================================================================
#     return results
# =============================================================================
    return_list = []
    for _m in which_moments:
        if _m.lower() == "p1":
            return_list.append(K_P_E)
        if _m.lower() == "pt":
            return_list.append(K_T_E)
        if _m.lower() in ["qe"]:
            return_list.append(K_QE_E)
        if _m.lower() in ["qt"]:
            return_list.append(K_QT_E)
        if _m.lower() == "m":
            return_list.append(K_M_E)
        if _m.lower() in ["qm"]:
            return_list.append(K_QM_E)
    
    return return_list







def eval_generalized_polarizability_p(sim, field_index, which_order='p', method='lu', 
                                      long_wavelength_approx=False):
    """get electric dipole moment via generalized polarizability
    
    will evaluate generalized pola. and store it in simulation, in case it 
    is not yet calculated.
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int, default: None
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`.
        Either `field_index` or `wavelength` must be given.
        
    which_order : str, optional
        The default is 'p'. One of:
            - 'p': full dipole moment including toroidal contribution
            - 'p1': only first order dipole
            - 'pt': only toroidal dipole moment
    
    method : string, default: "lu"
        inversion method if generalized pola. not yet calculated. 
        One of ["lu", "numpyinv", "scipyinv", "cupy", "cuda"]
        
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation


    Returns
    -------
    electric dipole moment (complex vector)

    """
    from pyGDM2 import tools
    
    kws_wl = tools.get_field_indices(sim)[field_index]
    wl = kws_wl['wavelength']
    
    for which_moment in ['p1', 'pt']:
        _test_availability_generalized_polarizability(sim, which_moment, 
              wl, method=method, long_wavelength_approx=long_wavelength_approx)
    
        
    K_P_E = sim.K_P_E[wl]
    K_T_E = sim.K_T_E[wl]
    
    ## illuminatin field for 'field_index'
    env_dict = sim.dyads.getConfigDictG(wl, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(sim.struct.geometry, env_dict, **kws_wl)
    
    if which_order.lower() in ['p', 'p0', 'p1']:  # 'p0' equiv. to 'p1'
        p1 = np.sum(np.matmul(K_P_E, E0[...,None]), axis=(0,2))
        if which_order.lower() in ['p0', 'p1']:
            p = p1
        
    if which_order.lower() in ['p', 'pt']:
        pt = np.array([np.sum(np.matmul(K_T_E[...,i,:,:], E0[:,:,None]), axis=(0,2)) for i in range(3)])
        pt = np.sum(pt, axis=1)
        if which_order.lower() == 'p':
            p = p1 + pt
        else:
            p = pt
    return p


def eval_generalized_polarizability_qe(sim, field_index, which_order='qe', method='lu', 
                                      long_wavelength_approx=False):
    """get electric quadrupole moment via generalized polarizability
    
    will evaluate generalized pola. and store it in simulation, in case it 
    is not yet calculated.
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int, default: None
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`.
        Either `field_index` or `wavelength` must be given.
        
    which_order : str, optional
        The default is 'qe'. One of:
            - 'qe': full electric quadrupole moment (including toroidal contribution)
            - 'qe1': only first order contribution to quadrupole
            - 'qet': only toroidal quadrupole moment
            
    method : string, default: "lu"
        inversion method if generalized pola. not yet calculated. 
        One of ["lu", "numpyinv", "scipyinv", "cupy", "cuda"]
        
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation

        
    Returns
    -------
    electric quadrupole moment (complex tensor, 3x3)

    """
    from pyGDM2 import tools
    
    kws_wl = tools.get_field_indices(sim)[field_index]
    wl = kws_wl['wavelength']
    
    for which_moment in ['qe', 'qt']:
        _test_availability_generalized_polarizability(sim, which_moment, 
              wl, method=method, long_wavelength_approx=long_wavelength_approx)
    
        
    K_QE_E = sim.K_QE_E[wl]
    K_QT_E = sim.K_QT_E[wl]
    
    ## illumination field for 'field_index'
    env_dict = sim.dyads.getConfigDictG(wl, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(sim.struct.geometry, env_dict, **kws_wl)
    
    
    if which_order.lower() in ['q', 'qe', 'qe0', 'qe1']:  # 'qe0' equiv. to 'qe1'
        qe1 = np.array([
            [np.sum(np.matmul(K_QE_E[...,i,j,:,:], E0[:,:,None]), axis=(0,2)) 
                                         for j in range(3)] for i in range(3)])
        qe1 = np.sum(qe1, axis=-1)
        if which_order.lower() in ['qe0', 'qe1']:
            qe = qe1
        
    if which_order.lower() in ['q', 'qe', 'qet', 'qt']:
        qet = np.array([
            [np.sum(np.matmul(K_QT_E[...,i,j,:,:], E0[:,:,None]), axis=(0,2)) 
                                         for j in range(3)] for i in range(3)])
        qet = np.sum(qet, axis=-1)
        if which_order.lower() in ['q', 'qe']:  # 'q' equiv. to 'qe'
            qe = qe1 + qet
        else:
            qe = qet
    return qe


def eval_generalized_polarizability_m(sim, field_index, method='lu', 
                                      long_wavelength_approx=False):
    """get magnetic dipole moment via generalized polarizability
    
    will evaluate generalized pola. and store it in simulation, in case it 
    is not yet calculated.
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int, default: None
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`.
        Either `field_index` or `wavelength` must be given.
            
    method : string, default: "lu"
        inversion method if generalized pola. not yet calculated. 
        One of ["lu", "numpyinv", "scipyinv", "cupy", "cuda"]
        
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation

        
    Returns
    -------
    magnetic quadrupole moment (complex vector)

    """
    from pyGDM2 import tools
    
    kws_wl = tools.get_field_indices(sim)[field_index]
    wl = kws_wl['wavelength']
    
    for which_moment in ['m']:
        _test_availability_generalized_polarizability(sim, which_moment, 
              wl, method=method, long_wavelength_approx=long_wavelength_approx)     
    
    K_M_E = sim.K_M_E[wl]
    
    ## illuminatin field for 'field_index'
    env_dict = sim.dyads.getConfigDictG(wl, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(sim.struct.geometry, env_dict, **kws_wl)
    
    m = np.sum(np.matmul(K_M_E, E0[...,None]), axis=(0,2))
    
    return m


def eval_generalized_polarizability_qm(sim, field_index, method='lu', 
                                      long_wavelength_approx=False):
    """get magnetic quadrupole moment via generalized polarizability
    
    will evaluate generalized pola. and store it in simulation, in case it 
    is not yet calculated.
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int, default: None
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`.
        Either `field_index` or `wavelength` must be given.
            
    method : string, default: "lu"
        inversion method if generalized pola. not yet calculated. 
        One of ["lu", "numpyinv", "scipyinv", "cupy", "cuda"]
        
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation

        
    Returns
    -------
    magnetic quadrupole tensor (complex tensor, 3x3)

    """
    from pyGDM2 import tools
    
    kws_wl = tools.get_field_indices(sim)[field_index]
    wl = kws_wl['wavelength']
    
    for which_moment in ['qm']:
        _test_availability_generalized_polarizability(sim, which_moment, 
              wl, method=method, long_wavelength_approx=long_wavelength_approx)
    
    K_QM_E = sim.K_QM_E[wl]
    
    ## illuminatin field for 'field_index'
    env_dict = sim.dyads.getConfigDictG(wl, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(sim.struct.geometry, env_dict, **kws_wl)
    
    qm = np.array([np.sum(np.matmul(K_QM_E[...,i,:,:], E0[:,:,None]), axis=(0,2)) for i in range(3)])
    
    return qm


def extract_effective_polarizability(sim, method='lu',
                                     which_moments=['p1','m'], long_wavelength_approx=True,
                                     illumination_mode='dipole', npoints=25, r_sphere=1000,
                                     store_simulation_object=False):
    """Extract effective electric and magnetic dipole polarizability for structure
    
    solve inverse problem of adjusting polarizability for different illuminations
    via pseudoinverse
    
    *doc to be completed*
    
    store_simulation_object : Bool, default: False
        optionally store full sim in output dictionnary. 
        *Caution:* This contains numba compiled objects which are not 
        necessarily reloadable on other operating systems than the 
        one used for the simulation

    """
    from pyGDM2 import fields
    from pyGDM2 import tools
    from scipy import linalg
    
    def sample_spherical(npoints, ndim=3):
        """random pos. on sphere (R=1). from: https://stackoverflow.com/questions/33976911"""
        vec = np.random.randn(ndim, npoints)
        vec /= np.linalg.norm(vec, axis=0)
        return vec

    ## dipoles of random position and random orientation
    wavelengths = sim.efield.wavelengths
    
    r0 = np.average(sim.struct.geometry, axis=0)
    sim.r0 = r0
    

    if illumination_mode.lower() == 'dipole':
        rnd_pos = sample_spherical(npoints, ndim=3).T * r_sphere
        field_kwargs = [
            dict(x0=rnd_pos[i,0], y0=rnd_pos[i,1], z0=rnd_pos[i,2], 
                 mx=np.random.random()*r_sphere,
                 my=np.random.random()*r_sphere,
                 mz=np.random.random()*r_sphere)
            for i in range(npoints)
            ]
        field_generator = fields.dipole_electric
    else:
    ## -- alternative: plane wave with different polarizations / incident angles
        field_kwargs = [
            dict(inc_angle=0, inc_plane='xz', E_s=0.0, E_p=1.0),
            dict(inc_angle=0, inc_plane='xz', E_s=1.0, E_p=0.0),
            dict(inc_angle=90, inc_plane='xz', E_s=1.0, E_p=0.0),
            dict(inc_angle=90, inc_plane='xz', E_s=0.0, E_p=1.0),
            dict(inc_angle=90, inc_plane='yz', E_s=1.0, E_p=0.0),
            dict(inc_angle=90, inc_plane='yz', E_s=0.0, E_p=1.0),
            ]
        field_generator = fields.plane_wave
    
    n_illum = len(field_kwargs)
    efield = fields.efield(field_generator, wavelengths=wavelengths, kwargs=copy.deepcopy(field_kwargs))
    _sim = sim.copy()
    _sim.efield = efield
    _sim.scatter(method=method)
    
    ahh = []
    aee = []
    for i_wl, wl in enumerate(wavelengths):
        p_eval = np.zeros((3, n_illum), dtype=np.complex64)
        m_eval = np.zeros((3, n_illum), dtype=np.complex64)
        E0_eval = np.zeros((3, n_illum), dtype=np.complex64)
        H0_eval = np.zeros((3, n_illum), dtype=np.complex64)
        for idx, kw  in enumerate(field_kwargs):
            ## illuminatin field for 'field_index'
            env_dict = _sim.dyads.getConfigDictG(wl, _sim.struct, _sim.efield)
            E0 = efield.field_generator([_sim.r0], env_dict, wavelength=wl, **kw)[0]
            # inc. field array shape: (3, n_fields)
            E0_eval[:, idx] = E0
            
            H0 = efield.field_generator([_sim.r0], env_dict, wavelength=wl, returnField='H', **kw)[0]
            H0_eval[:, idx] = H0
            
            kw_wl = kw.copy()
            kw_wl['wavelength'] = wl
            field_index = tools.get_closest_field_index(_sim, kw_wl)
            p, m = multipole_decomposition_exact(_sim, field_index, which_moments=which_moments, 
                                                 long_wavelength_approx=long_wavelength_approx)
            p_eval[...,idx] = p
            m_eval[...,idx] = m
        
        ## pseudo-inverse of all illuminations
        AEinv = linalg.pinv(np.conj(E0_eval).T)
        AHinv = linalg.pinv(np.conj(H0_eval).T)
        
        ## optimum alphas to obtain dipole moments for each illumination
        alpha_pinv = np.conj(np.dot(AEinv, np.conj(p_eval).T)).T
        alpha_minv = np.conj(np.dot(AHinv, np.conj(m_eval).T)).T
        
        aee.append(alpha_pinv.reshape([3,3]))
        ahh.append(alpha_minv.reshape([3,3]))
    
    enclosing_radius = tools.get_enclosing_sphere_radius(sim)
    
    dict_pola_pseudo = dict(
                r0=sim.r0, r0_MD=sim.r0, r0_ED=sim.r0, 
                full_geometry=sim.struct.geometry, 
                alpha_pE=aee, 
                alpha_mH=ahh, 
                wavelengths=sim.efield.wavelengths, 
                enclosing_radius=enclosing_radius,
                k0_spectrum=2 * np.pi / np.array(wavelengths).copy(),
                )
    
    # optionally add also the full sim.
    if store_simulation_object:
        dict_pola_pseudo['sim'] = sim
    
    return dict_pola_pseudo

