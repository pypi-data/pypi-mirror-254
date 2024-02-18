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
# import math

import numpy as np
import copy
import numba

import time

from pyGDM2.multipole.main import multipole_decomposition_exact
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_m
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_p
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_qe
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_qm
from pyGDM2.multipole.polarizabilities import _test_availability_generalized_polarizability
from pyGDM2.multipole import propagators as mp_propagators

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
def _check_multipole_list(p, m, qe, qm, r_p, r_m, r_qe, r_qm, r0):
    
    # dipole moment definitions
    if len(p) == 0 and len(m) == 0 and len(qe) == 0 and len(qm) == 0:
        raise Exception("All multipoles are zero. Please define at least one multipole moment.")
    if len(p) == 0:
        p = np.zeros((0, 3), dtype=np.complex64)
        r_p = np.zeros((0, 3), dtype=np.float32)
    if len(m) == 0:
        m = np.zeros((0, 3), dtype=np.complex64)
        r_m = np.zeros((0, 3), dtype=np.float32)
    if len(qe) == 0:
        qe = np.zeros((0, 3), dtype=np.complex64)
        r_qe = np.zeros((0, 3), dtype=np.float32)
    if len(qm) == 0:
        qm = np.zeros((0, 3), dtype=np.complex64)
        r_qm = np.zeros((0, 3), dtype=np.float32)
        
    # positions 
    if r0 is None:
        if r_p is None and r_m is None and r_qe is None and r_qm is None:
            raise Exception("No positions for the multipoles are given.")
        if len(r_p) != len(p):
            raise Exception("Same number of dipole positions and dipole moments required! `p` and `r_p` must be lists of same length.")
        if len(r_m) != len(m):
            raise Exception("Same number of dipole positions and dipole moments required! `m` and `r_m` must be lists of same length.")
        if len(r_qe) != len(qe):
            raise Exception("Same number of quadrupole positions and quadrupole moments required! `qe` and `r_qe` must be lists of same length.")
        if len(r_qm) != len(qm):
            raise Exception("Same number of quadrupole positions and quadrupole moments required! `qm` and `r_qm` must be lists of same length.")
    else:
        # global r0 defined: override specific positions
        r0 = np.array(r0)
        if len(r0) != 3: 
            raise Exception("Multipole position must be carthesian coordinate (array of 3 float)")
        if len(p) > 0:
            r_p = np.array([r0 for _ in p], dtype= np.float32)
        if len(m) > 0:
            r_m = np.array([r0 for _ in m], dtype= np.float32)
        if len(qe) > 0:
            r_qe = np.array([r0 for _ in qe], dtype= np.float32)
        if len(qm) > 0:
            r_qm = np.array([r0 for _ in qm], dtype= np.float32)
    
    return p, m, qe, qm, r_p, r_m, r_qe, r_qm, r0


def _eval_G0(G0func, R1, R2, wl, eps_env):
    """evaluate a free-space Green's tensor `G0func`
    """
    if np.linalg.norm(R1-R2)==0:
        warnings.warn("Green's tensor singularity. Returning zero.")
        return np.zeros((3,3), dtype=np.complex64)
    
    xx, yy, zz, xy, xz, yx, yz, zx, zy = G0func(R1, R2, wl, eps_env)
    G0 = np.array([
        [xx, xy, xz],
        [yx, yy, yz],
        [zx, zy, zz],
        ]).astype(np.complex64)
    
    return G0


# =============================================================================
# LOW-LEVEL (working with lists of multipoles)
# =============================================================================
def _multipole_extinct(sim, field_index,
                       p=[], m=[], qe=[], qm=[],
                       r_p=None, r_m=None, r_qe=None, r_qm=None,
                       r0=None, eps_dd=0.001, 
                       normalization_E0=True,
                       ):
    """extinction cross-section for an explicit list of multipole moments
    
    
    Parameters
    ----------
    wavelength : float
        radiation wavelength
    
    eps_env : float
        envirnoment permittivity (real part)
        
    r0 : array. optional
        [x,y,z] position of mulipole decomposition development.
        Alternatively the positions of each mutlipole can be specified.
        The default is `None`.
        
    p, m, qe, qm : lists of ndarrays. optional
        lists of dipole and quadrupole moments to propagate to the farfield.
        The default is [].
        
    r_p, r_m, r_qe, r_qm : ndarrays or list of such. optional
        Has effect only if r0 is not specified. Carthesian coordinates of 
        each multipole individually.
    
    
    Returns
    -------
    total extinction cross sections for each multipole type (in nm^2)
        
    
    Notes
    -----
    For details about the extinction section of multipole moments, see:
    
    Evlyukhin, A. B. et al. *Multipole analysis of light scattering by 
    arbitrary-shaped nanoparticles on a plane surface.*, 
    JOSA B 30, 2589 (2013)
    """
# =============================================================================
#     exception handling
# =============================================================================
    p, m, qe, qm, r_p, r_m, r_qe, r_qm, r0 = _check_multipole_list(
        p=p, m=m, qe=qe, qm=qm, r_p=r_p, r_m=r_m, r_qe=r_qe, r_qm=r_qm, r0=r0)
    
    
# =============================================================================
#     preparation
# =============================================================================  
    from pyGDM2 import tools 
    from pyGDM2 import linear
    
    field_params = tools.get_field_indices(sim)[field_index]
    wavelength   = field_params['wavelength']
    sim.struct.setWavelength(wavelength)
    k0 = 2*np.pi / wavelength
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, sim.struct.geometry[:1])[0]  # structure must be fully in one environment zone
    n_env = (eps_env**0.5).real
    
    ## incident field and its gradients at multipole position
    env_dict = sim.dyads.getConfigDictG(wavelength, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(r_p, env_dict, **field_params)
    H0 = sim.efield.field_generator(r_m, env_dict, returnField='H', **field_params)
    
    gradE0 = linear.field_gradient(sim, field_index, r_qe, 
                                   delta=eps_dd, which_fields=['E0'])
    gradH0 = linear.field_gradient(sim, field_index, r_qm, 
                                   delta=eps_dd, which_fields=['H0'])
    gradE0cj = np.conj(np.array(gradE0)[...,3:])
    gradH0cj = np.conj(np.array(gradH0)[...,3:])
    
    ## normalization
    if normalization_E0:
        # intensity of incident field at each multipole
        E2in_p = np.sum(np.abs(sim.efield.field_generator(r_p, env_dict, **field_params))**2, axis=1).real
        E2in_m = np.sum(np.abs(sim.efield.field_generator(r_m, env_dict, **field_params))**2, axis=1).real
        E2in_qe = np.sum(np.abs(sim.efield.field_generator(r_qe, env_dict, **field_params))**2, axis=1).real
        E2in_qm = np.sum(np.abs(sim.efield.field_generator(r_qm, env_dict, **field_params))**2, axis=1).real
    else:
        E2in_p = np.ones(len(r_p))
        E2in_m = np.ones(len(r_m))
        E2in_qe = np.ones(len(r_qe))
        E2in_qm = np.ones(len(r_qm))
    
    E0 = E0 / E2in_p[:,None]
    H0 = H0 / E2in_m[:,None]
    gradE0cj = gradE0cj / E2in_qe[:,None]
    gradH0cj = gradH0cj / E2in_qm[:,None]
    
# =============================================================================
#     calc the ECS per multipole order
# =============================================================================
    prefactor = (4 * np.pi * k0 * 1/n_env).real
    
    ecs_p = prefactor * (np.sum(np.conjugate(E0)*p)).imag
    ecs_m = prefactor / n_env * (np.sum(np.conjugate(H0)*m)).imag
    ecs_Qe = prefactor / 12. * (np.sum([np.tensordot(gradE0cj[:,i,:] + gradE0cj[:,i,:].T, qe[i]) for i in range(len(qe))] )).imag
    ecs_Qm = prefactor / n_env / 6 * (np.sum([np.tensordot(gradH0cj[:,i,:].T, qm[i]) for i in range(len(qm))] )).imag
    
    return [ecs_p, ecs_m, ecs_Qe, ecs_Qm]


def _multipole_scs(sim, field_index,
                   p=[], m=[], qe=[], qm=[],
                   r_p=None, r_m=None, r_qe=None, r_qm=None,
                   r0=None, eps_dd=0.001, 
                   normalization_E0=True,
                   ):
    """scattering cross-section for an explicit list of multipole moments
    
    Radiated electro-magnetic field  (E-field) in the far-field 
    (by default on a sphere of radius `r` around the nanostructure).
    
    
    Parameters
    ----------
    wavelength : float
        radiation wavelength
    
    eps_env : float
        envirnoment permittivity (real part)
        
    r0 : array. optional
        [x,y,z] position of mulipole decomposition development.
        Alternatively the positions of each mutlipole can be specified.
        The default is `None`.
        
    p, m, qe, qm : lists of ndarrays. optional
        lists of dipole and quadrupole moments to propagate to the farfield.
        The default is [].
        
    r_p, r_m, r_qe, r_qm : ndarrays or list of such. optional
        Has effect only if r0 is not specified. Carthesian coordinates of 
        each multipole individually.
    
    Returns
    -------
    total scattering cross sections for each multipole type (in nm^2)
        
    
    Notes
    -----
    For details about the exact multipole formalism and scs calculation, see: 
        
    Alaee, R., Rockstuhl, C. & Fernandez-Corbaton, I. *An electromagnetic 
    multipole expansion beyond the long-wavelength approximation.*
    Optics Communications 407, 17–21 (2018)        
    """
# =============================================================================
#     exception handling
# =============================================================================
    p, m, qe, qm, r_p, r_m, r_qe, r_qm, r0 = _check_multipole_list(
        p=p, m=m, qe=qe, qm=qm, r_p=r_p, r_m=r_m, r_qe=r_qe, r_qm=r_qm, r0=r0)
    
# =============================================================================
#     preparation
# =============================================================================  
    from pyGDM2 import tools 
    
    field_params = tools.get_field_indices(sim)[field_index]
    wavelength   = field_params['wavelength']
    sim.struct.setWavelength(wavelength)
    k0 = 2*np.pi / wavelength
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, sim.struct.geometry[:1])[0]  # structure must be fully in one environment zone
    n_env = (eps_env**0.5).real
    k = k0*n_env
    
    ## normalization
    if normalization_E0:
        ## incident field intensity at each multipole location
        env_dict = sim.dyads.getConfigDictG(wavelength, sim.struct, sim.efield)
        
        E2in_p = np.sum(np.abs(sim.efield.field_generator(r_p, env_dict, **field_params))**2, axis=1).real
        E2in_m = np.sum(np.abs(sim.efield.field_generator(r_m, env_dict, **field_params))**2, axis=1).real
        E2in_qe = np.sum(np.abs(sim.efield.field_generator(r_qe, env_dict, **field_params))**2, axis=1).real
        E2in_qm = np.sum(np.abs(sim.efield.field_generator(r_qm, env_dict, **field_params))**2, axis=1).real
    else:
        E2in_p = np.ones(len(r_p))
        E2in_m = np.ones(len(r_m))
        E2in_qe = np.ones(len(r_qe))
        E2in_qm = np.ones(len(r_qm))
    
# =============================================================================
#     calc the ECS per multipole order
# =============================================================================
    ## factor 100: cm --> m (cgs units)
    sc_factor_dp = 100/12*(k0**4).real
    sc_factor_Q = 100/1440*(k0**4).real
        
    scs_p = sc_factor_dp * np.sum(np.abs(p)**2 / E2in_p[:,None])
    scs_m = sc_factor_dp * np.sum(np.abs(m)**2 / E2in_m[:,None])
    scs_Qe = sc_factor_Q * np.sum(np.abs(k*qe)**2 / E2in_qe[:,None])
    scs_Qm = sc_factor_Q * np.sum(np.abs(k*qm)**2 / E2in_qm[:,None])
    
    return [scs_p, scs_m, scs_Qe, scs_Qm]


def _multipole_nearfield(wavelength, r_probe, eps_env=1, 
                         p=[], m=[], qe=[], qm=[],
                         r_p=None, r_m=None, r_qe=None, r_qm=None,
                         r0=None, which_fields=["Es","Bs"]):
    """calculate scattered field of multiple multipole (valid in the nearfield region)
    
    !! not performance optimized !!
    
    Parameters
    ----------
    wavelength : float
        radiation wavelength
        
    r_probe : tuple (x,y,z) or list of 3-lists/-tuples
        (list of) coordinate(s) to evaluate nearfield on. 
        Format: tuple (x,y,z) or list of 3 lists: [Xmap, Ymap, Zmap] 
        (the latter can be generated e.g. using :func:`.tools.generate_NF_map`)
    eps_env : float
        envirnoment permittivity (real part)
        
    r0 : array. optional
        [x,y,z] position of mulipole decomposition development.
        Alternatively the positions of each mutlipole can be specified.
        The default is `None`.
        
    p, m, qe, qm : lists of ndarrays. optional
        lists of dipole and quadrupole moments to propagate to the farfield.
        The default is [].
        
    r_p, r_m, r_qe, r_qm : ndarrays or list of such. optional
        Has effect only if r0 is not specified. Carthesian coordinates of 
        each multipole individually.
        
    which_fields : list of str, default: ["Es","Bs"]
        which fields to calculate and return. available options: 
            ["Es", "Bs"]
    
    Returns
    -------
    depending on kwarg `which_fields`, one or two lists of 6-tuples, complex : 
        - scattered Efield ("Es")
        - scattered Bfield ("Bs")
    
    the tuples are of shape (X,Y,Z, Ax,Ay,Az) with Ai the corresponding 
    complex field component
    
    Notes
    -----
    Details about the calculation of the field scattered by quadrupoles:
    Babicheva and Evlyukhin
    **Analytical model of resonant electromagnetic dipole-quadrupole coupling 
    in nanoparticle arrays**
    Phys. Rev. B 99, 195444 (2019)

    """
# =============================================================================
#     exception handling
# =============================================================================
    p, m, qe, qm, r_p, r_m, r_qe, r_qm, r0 = _check_multipole_list(
        p=p, m=m, qe=qe, qm=qm, r_p=r_p, r_m=r_m, r_qe=r_qe, r_qm=r_qm, r0=r0)

# =============================================================================
#     the main calculation
# =============================================================================
    return_field_list = []
    for returnfield in which_fields:
        
        if returnfield.lower() in ['e', 'es']:
            func_G_p = mp_propagators.G0_Ep
            func_G_m = mp_propagators.G0_Em
            func_G_qe = mp_propagators.G0_Eqe
            func_G_qm = mp_propagators.G0_Eqm
        elif returnfield.lower() in ['h', 'b', 'hs', 'bs']:
            func_G_p = mp_propagators.G0_Hp
            func_G_m = mp_propagators.G0_Hm
            func_G_qe = mp_propagators.G0_Hqe
            func_G_qm = mp_propagators.G0_Hqm
            
        ## evaluate the propagators
        Fp = np.zeros([len(r_probe), 3], dtype=np.complex64)
        Fm = np.zeros([len(r_probe), 3], dtype=np.complex64)
        FQe = np.zeros([len(r_probe), 3], dtype=np.complex64)
        FQm = np.zeros([len(r_probe), 3], dtype=np.complex64)
        for i, _r in enumerate(r_probe):
            # ED
            for j, r0 in enumerate(r_p):
                n_vec = (_r - r0) / np.linalg.norm((_r - r0)) # scat. direction
                Gp = _eval_G0(func_G_p, r0, _r, wavelength, eps_env)
                Fp[i] += np.dot(Gp, p[j]) # add scattered field
                
            # MD
            for j, r0 in enumerate(r_m):
                n_vec = (_r - r0) / np.linalg.norm((_r - r0)) # scat. direction                
                Gm = _eval_G0(func_G_m, r0, _r, wavelength, eps_env)
                Fm[i] += np.dot(Gm, m[j]) # add scattered field
                
            # QE
            for j, r0 in enumerate(r_qe):
                n_vec = (_r - r0) / np.linalg.norm((_r - r0)) # scat. direction                
                Gqe = _eval_G0(func_G_qe, r0, _r, wavelength, eps_env)
                qen = np.tensordot(qe, n_vec, axes=(-1,-1))
                FQe[i] += np.dot(Gqe, qen[j]) # add scattered field
            
            # QM    
            for j, r0 in enumerate(r_qm):
                Gqm = _eval_G0(func_G_qm, r0, _r, wavelength, eps_env)
                qmn = np.tensordot(qm, n_vec, axes=(-1,-1))
                FQm[i] += np.dot(Gqm, qmn[j]) # add scattered field
            
        
        # sum contributions of all multipoles and append calculation positions
        F = Fp + Fm + FQe + FQm
        F_iwth_pos = np.concatenate([r_probe, F], axis=1)
        return_field_list.append(F_iwth_pos)
    
    return return_field_list


def _multipole_farfield(wavelength, eps_env, r0=None, 
                        p=[], m=[], qe=[], qm=[],
                        r_p=None, r_m=None, r_qe=None, r_qm=None,
                        r_probe=None,
                        r=100000., 
                        tetamin=0, tetamax=np.pi/2., Nteta=10, 
                        phimin=0, phimax=2*np.pi, Nphi=36, 
                        return_value='map'):
    """far-field scattering of an explicit list of multipole moments
    
    Radiated electro-magnetic field  (E-field) in the far-field 
    (by default on a sphere of radius `r` around the nanostructure).
    
    
    Parameters
    ----------
    wavelength : float
        radiation wavelength
    
    eps_env : float
        envirnoment permittivity (real part)
        
    r0 : array. optional
        [x,y,z] position of mulipole decomposition development.
        Alternatively the positions of each mutlipole can be specified.
        The default is `None`.
        
    p, m, qe, qm : lists of ndarrays. optional
        lists of dipole and quadrupole moments to propagate to the farfield.
        The default is [].
        
    r_p, r_m, r_qe, r_qm : ndarrays or list of such. optional
        Has effect only if r0 is not specified. Carthesian coordinates of 
        each multipole individually.
    
    r_probe : tuple (x,y,z) or list of 3-lists/-tuples. optional
        defaults to *None*, which means it is not used and a solid angle defined by
        a spherical coordinate range is used instead. If `r_probe` is given, this
        overrides `r`, `tetamin`, `tetamax`, `Nteta`, `Nphi`.
        (list of) coordinate(s) to evaluate farfield on. 
        Format: tuple (x,y,z) or list of 3 lists: [Xmap, Ymap, Zmap] 
        The default is None. (Not used)
        
    r : float, default: 100000.
        radius of integration sphere (distance to coordinate origin in nm)
        
    tetamin, tetamax : float, float; defaults: 0, np.pi/2
        minimum and maximum polar angle in radians 
        (in linear steps from `tetamin` to `tetamax`)
        
    phimin, phimax : float, float; defaults: 0, 2*np.pi
        minimum and maximum azimuth angle in radians, excluding last position
        (in linear steps from `phimin` to `phimax`)
        
    Nteta, Nphi : int, int; defaults: 10, 36
        number of polar and azimuthal angles on sphere to calculate,
    
    return_value : str, default: 'map'
        Values to be returned. Either 'map' (default) or 'integrated'.
          - "map" : (default) return spatially resolved farfield intensity at each spherical coordinate (5 lists)
          - "efield" : return spatially resolved E-fields at each spherical coordinate (5 lists)
          - "int_Es" : return the integrated scattered field (as float)
    
    
    Returns
    -------
    using `r_probe` for position definition:
        3 lists of 6-tuples (x,y,z, Ex,Ey,Ez), complex : 
            - scattered Efield or E-intensity
        
    if solid angle is defined via spherical coordinate range:
        - return_value == "map" : 5 arrays of shape (Nteta, Nphi) : 
            - [tetalist : teta angles - if solid angle range input]
            - [philist : phi angles - if solid angle range input]
            - I_sc : intensity of scattered field, 
        
        - return_value == "efield" : float
            - [tetalist : teta angles - if solid angle range input]
            - [philist : phi angles - if solid angle range input]
            - E_sc : complex scattered field at each pos.
            
        - return_value == "int_XX" : float
            integrated total intensity over specified solid angle
        
    
    Notes
    -----
    See equation (G1) in
    
    Alaee, R., Rockstuhl, C. & Fernandez-Corbaton, I. *An electromagnetic 
    multipole expansion beyond the long-wavelength approximation.*
    Optics Communications 407, 17–21 (2018)
        
    """
# =============================================================================
#     exception handling
# =============================================================================
    if np.pi < tetamax < 0:
        raise ValueError("`tetamax` out of range, must be in [0, pi]")
    
    if r_probe is not None and return_value in ['int_es', 'int_E0', 'int_Etot']:
        raise ValueError("probing farfield on user-defined positions does not support integration " +
                         "of the intensity since no surface differential can be defined. Use spherical " +
                         "coordinate definition to do the integration.")
    
    p, m, qe, qm, r_p, r_m, r_qe, r_qm, r0 = _check_multipole_list(
        p=p, m=m, qe=qe, qm=qm, r_p=r_p, r_m=r_m, r_qe=r_qe, r_qm=r_qm, r0=r0)
    
        
# =============================================================================
#     preparation
# =============================================================================
    ## --- spherical probe coordinates
    if r_probe is None:
        tetalist = np.ones((int(Nteta), int(Nphi)))*np.linspace(tetamin, tetamax, int(Nteta))[:,None]
        philist = np.ones((int(Nteta), int(Nphi)))*np.linspace(phimin, phimax, int(Nphi), endpoint=False)[None,:]
        xff = (r * np.sin(tetalist) * np.cos(philist)).flatten()
        yff = (r * np.sin(tetalist) * np.sin(philist)).flatten()
        zff = (r * np.cos(tetalist)).flatten()
        _r_probe = np.transpose([xff, yff, zff])
    else:
        _r_probe = r_probe
        
    ## --- spherical integration steps
    dteta = (tetamax-tetamin) / float(Nteta-1)  # endpoint included
    dphi = (phimax-phimin) / float(Nphi)        # endpoint not included
    
    ## --- environment
    k0 = 2*np.pi / wavelength
    n_env = (eps_env**0.5).real
    k = k0*n_env
    
#==============================================================================
#     electric polarization of structure, fundamental field
#==============================================================================        
    Escat = np.zeros(shape=(len(_r_probe), 3), dtype=DTYPE_C)
    
    def eval_prefactors(r0, _r_probe, k, k0):
        n_vec = _r_probe - r0
        R_d = np.linalg.norm(n_vec, axis=1)
        n_vec = n_vec / R_d[:,None]     # unit vector along direction of scattering
        
        phase_factor = np.exp(1j*k*R_d)
        prefactor = k0**2 * phase_factor / R_d
        
        return prefactor, n_vec
    
    
    for _r0, _p in zip(r_p, p):
        prefactor, n0_vec = eval_prefactors(_r0, _r_probe, k, k0)
        Es_p = prefactor[:,None] * np.cross(n0_vec, np.cross((_p)[None,:], n0_vec))
        Escat += Es_p     # sum all electric dipole fields
    
    for _r0, _m in zip(r_m, m):
        prefactor, n0_vec = eval_prefactors(_r0, _r_probe, k, k0)
        Es_m = prefactor[:,None] * np.cross(_m[None,:], n0_vec)
        Escat += Es_m     # sum all magnetic dipole fields
    
    for _r0, _qe in zip(r_qe, qe):
        prefactor, n0_vec = eval_prefactors(_r0, _r_probe, k, k0)
        Es_qe = prefactor[:,None] * 1j * k/6 * np.cross(n0_vec, 
                    np.cross(n0_vec, np.tensordot(_qe, n0_vec, axes=(-1,-1)).T))
        Escat += Es_qe     # sum all electric quadrupole fields
    
    for _r0, _qm in zip(r_qm, qm):
        prefactor, n0_vec = eval_prefactors(_r0, _r_probe, k, k0)
        Es_qm = prefactor[:,None] * 1j * k/6 * np.cross(n0_vec, 
                    np.tensordot(_qm, n0_vec, axes=(-1,-1)).T)
        Escat += Es_qm     # sum all magnetic quadrupole fields

    
    Iscat = np.sum((np.abs(Escat)**2), axis=1)



#==============================================================================
#     return either of scattered field / intensity / map
#==============================================================================
    ## --- total field (no polarizer)
    if r_probe is None:
        out_shape = tetalist.shape
    else:
        out_shape = len(_r_probe)
        
    I_sc  = Iscat.reshape(out_shape)
    
    
    if return_value.lower() in ['map', 'map_i', 'i_map']:
        if r_probe is None:
            return tetalist, philist, I_sc
        else:
            return I_sc
    elif return_value.lower() in ['efield', 'fields', 'field']:
        if r_probe is None:
            return tetalist, philist, Escat
        else:
            return Escat
    else:
        d_solid_surf = r**2 * np.sin(tetalist) * dteta * dphi
        if return_value.lower() in ['int_es', 'int']:
            return np.sum(I_sc * d_solid_surf)
        
        else:
            raise ValueError("Parameter 'return_value' must be one of ['map', 'int_es', 'efield'].")



# =============================================================================
# HIGH-LEVEL (pyGDM2 compatibility)
# =============================================================================
def extinct(sim, field_index, with_toroidal=True, r0=None, eps_dd=0.001, 
            use_generalized_polarizabilities=False, normalization_E0=True,
            long_wavelength_approx=False):
    """extinction cross sections from multipole decomposition
    
    ** ------- FUNCTION STILL UNDER TESTING ------- **
    
    Returns extinction cross sections for electric and magnetic dipole and 
    quadrupole moments of the multipole decomposition.
    
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`
    
    with_toroidal : bool, default: True
        whether to add toroidal moments to electric dipole and quadrupole
    
    r0 : array, default: None
        [x,y,z] position of mulipole decomposition development. 
        If `None`, use structure's center of gravity
    
    eps_dd : float, default: 0.1
        numerical integration step (in nm). Used for e/m quadrupole extinction.
    
    normalization_E0 : bool, default: True
        normalizes sections to max. incident field intensity
        
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation
        
        
    Returns
    -------
    sigma_ext_p : float
        electric dipole extinction cross section (in nm^2)
    
    sigma_ext_m : float
        magnetic dipole extinction cross section (in nm^2)
        
    sigma_ext_q : float
        electric quadrupole extinction cross section (in nm^2)
        
    sigma_ext_mq : float
        magnetic quadrupole extinction cross section (in nm^2)
    
    
    Notes
    -----
    For details about the extinction section of multipole moments, see:
    
    Evlyukhin, A. B. et al. *Multipole analysis of light scattering by 
    arbitrary-shaped nanoparticles on a plane surface.*, 
    JOSA B 30, 2589 (2013)
    
    """
# =============================================================================
#     Exception handling
# =============================================================================

# =============================================================================
#     extinction section calculation
# =============================================================================
    from pyGDM2 import linear
    from pyGDM2 import tools
    
    ## by default, use center of gravity for multimode expansion
    geo = sim.struct.geometry
    if r0 is None:
        r0 = np.average(geo, axis=0)
    
    ## get dipole moments
    if not use_generalized_polarizabilities:
        p, p1, m, Qe, Qe1, Qm = multipole_decomposition_exact(
                sim, field_index, r0=r0, 
                long_wavelength_approx=long_wavelength_approx, 
                which_moments=['p', 'p1', 'm', 'qe', 'qe1', 'qm'])
        if not with_toroidal:
            p = p1
            Qe = Qe1
    else:
        if with_toroidal:
            p = eval_generalized_polarizability_p(sim, field_index, which_order='p')
            Qe = eval_generalized_polarizability_qe(sim, field_index, which_order='qe')
        else:
            p = eval_generalized_polarizability_p(sim, field_index, which_order='p1')
            Qe = eval_generalized_polarizability_qe(sim, field_index, which_order='qe1')
        m = eval_generalized_polarizability_m(sim, field_index)
        Qm = eval_generalized_polarizability_qm(sim, field_index)
        
    ## prefactors and incident field
    field_params = tools.get_field_indices(sim)[field_index]
    wavelength   = field_params['wavelength']
    sim.struct.setWavelength(wavelength)
    k0 = 2*np.pi / wavelength
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, geo[:1])[0]  # structure must be fully in one environment zone
    n_env = (eps_env**0.5).real
    
    ## incident field and its gradients at multipole position
    env_dict = sim.dyads.getConfigDictG(wavelength, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(r0[None,:], env_dict, **field_params)
    H0 = sim.efield.field_generator(r0[None,:], env_dict, returnField='H', **field_params)
    
    gradE0, gradH0 = linear.field_gradient(sim, field_index, r0[None,:], 
                                           delta=eps_dd, which_fields=['E0', 'H0'])
    gradE0cj = np.conj(np.array(gradE0)[:,0,3:])
    gradH0cj = np.conj(np.array(gradH0)[:,0,3:])
    
    ## normalization
    if normalization_E0:
        E2in = np.sum(np.abs(E0)**2, axis=1)   # intensity of incident field
    else:
        E2in = 1.0
    prefactor = (4 * np.pi * k0 * 1/n_env * 1/E2in).real
    
    ecs_p = prefactor * (np.sum(np.conjugate(E0)*p)).imag
    ecs_m = prefactor / n_env * (np.sum(np.conjugate(H0)*m)).imag
    ecs_Qe = prefactor / 12. * (np.sum(np.tensordot(gradE0cj + gradE0cj.T, Qe) )).imag
    ecs_Qm = prefactor / n_env / 6 * (np.sum(np.tensordot(gradH0cj.T, Qm) )).imag
    
    return [ecs_p, ecs_m, ecs_Qe, ecs_Qm]
    

def scs(sim, field_index, with_toroidal=True, 
        use_generalized_polarizabilities=False, 
        r0=None, normalization_E0=True,
        long_wavelength_approx=False):
    """total scattering cross section from multipole decomposition
    
    ** ------- FUNCTION STILL UNDER TESTING ------- **
    
    Returns scattering cross sections for electric and magnetic dipole and 
    quadrupole moments of the multipole decomposition.
    
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`
    
    with_toroidal : bool, default: True
        whether to add toroidal moments to electric dipole and quadrupole
            
    use_generalized_polarizabilities : bool, default: False
        if True, use generalized polarizabilities
        (does not require evaluation of `core.scatter` for new incident field 
         configurations, first calculation is more expensive)
    
    r0 : array, default: None
        [x,y,z] position of mulipole decomposition development. 
        If `None`, use structure's center of gravity
    
    normalization_E0 : bool, default: True
        normalizes sections to max. incident field intensity
        
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation
    
    
    Returns
    -------
    sigma_scat_p : float
        electric dipole scattering cross section (in nm^2)
    
    sigma_scat_m : float
        magnetic dipole scattering cross section (in nm^2)
        
    sigma_scat_q : float
        electric quadrupole scattering cross section (in nm^2)
        
    sigma_scat_mq : float
        magnetic quadrupole scattering cross section (in nm^2)
    
    
    Notes
    -----
    For details about the exact multipole formalism and scs calculation, see: 
        
    Alaee, R., Rockstuhl, C. & Fernandez-Corbaton, I. *An electromagnetic 
    multipole expansion beyond the long-wavelength approximation.*
    Optics Communications 407, 17–21 (2018)
    
    """
    from pyGDM2 import tools
# =============================================================================
#     Exception handling
# =============================================================================

# =============================================================================
#     scattering section calculation
# =============================================================================
    ## by default, use center of gravity for multimode expansion
    geo = sim.struct.geometry
    if r0 is None:
        r0 = np.average(geo, axis=0)
    
    ## get dipole moments
    if not use_generalized_polarizabilities:
        p, p1, m, Qe, Qe1, Qm = multipole_decomposition_exact(
                sim, field_index, r0=r0,
                which_moments=['p', 'p1', 'm', 'qe', 'qe1', 'qm'], 
                long_wavelength_approx=long_wavelength_approx)
        if not with_toroidal:
            p = p1
            Qe = Qe1
    else:
        if with_toroidal:
            p = eval_generalized_polarizability_p(sim, field_index, which_order='p', long_wavelength_approx=long_wavelength_approx)
            Qe = eval_generalized_polarizability_qe(sim, field_index, which_order='qe', long_wavelength_approx=long_wavelength_approx)
        else:
            p = eval_generalized_polarizability_p(sim, field_index, which_order='p1', long_wavelength_approx=long_wavelength_approx)
            Qe = eval_generalized_polarizability_qe(sim, field_index, which_order='qe1', long_wavelength_approx=long_wavelength_approx)
        m = eval_generalized_polarizability_m(sim, field_index, long_wavelength_approx=long_wavelength_approx)
        Qm = eval_generalized_polarizability_qm(sim, field_index, long_wavelength_approx=long_wavelength_approx)
    
    ## prefactors / illumination fields
    field_params = tools.get_field_indices(sim)[field_index]
    wavelength   = field_params['wavelength']
    sim.struct.setWavelength(wavelength)
    k0 = 2*np.pi / wavelength
    
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, geo[:1])[0]  # assume structure is fully in one environment
    n_env = (eps_env**0.5).real
    k = k0*n_env
    
    ## normalization: incident field intensity at multipole position
    env_dict = sim.dyads.getConfigDictG(wavelength, sim.struct, sim.efield)
    E0 = sim.efield.field_generator(r0[None,:], env_dict, **field_params)
    if normalization_E0:
        E2in = np.sum(np.abs(E0)**2, axis=1)   # intensity of incident field
    else:
        E2in = 1.0
    
    ## factor 100: cm --> m (cgs units)
    sc_factor_dp = 100/12*(k0**4 / E2in).real
    sc_factor_Q = 100/1440*(k0**4 / E2in).real
    
    
    scs_p = sc_factor_dp * np.sum(np.abs(p)**2)
    scs_m = sc_factor_dp * np.sum(np.abs(m)**2)
    scs_Qe = sc_factor_Q * np.sum(np.abs(k*Qe)**2)
    scs_Qm = sc_factor_Q * np.sum(np.abs(k*Qm)**2)
            
    return [scs_p, scs_m, scs_Qe, scs_Qm]



def farfield(sim, field_index, 
             r_probe=None,
             r=100000., 
             tetamin=0, tetamax=np.pi/2., Nteta=10, 
             phimin=0, phimax=2*np.pi, Nphi=36, 
             polarizerangle='none', return_value='map', 
             normalization_E0=False, 
             which_moments=['p', 'm', 'qe', 'qm'],
             long_wavelength_approx=False, r0=None):
    """spatially resolved and polarization-filtered far-field scattering 
    
    For a given incident field, calculate the electro-magnetic field 
    (E-component) in the far-field around the nanostructure 
    (on a sphere of radius `r`).
    
    Propagator for scattering into a substrate contributed by C. Majorel
    
    Pure python implementation.
    
    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
        
    field_index : int
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`
    
    r_probe : tuple (x,y,z) or list of 3-lists/-tuples. optional. Default: don't use
        defaults to *None*, which means it is not used and a solid angle defined by
        a spherical coordinate range is used instead. If `r_probe` is given, this
        overrides `r`, `tetamin`, `tetamax`, `Nteta`, `Nphi`.
        (list of) coordinate(s) to evaluate farfield on. 
        Format: tuple (x,y,z) or list of 3 lists: [Xmap, Ymap, Zmap] 
        
    r : float, default: 100000.
        radius of integration sphere (distance to coordinate origin in nm)
        
    tetamin, tetamax : float, float; defaults: 0, np.pi/2
        minimum and maximum polar angle in radians 
        (in linear steps from `tetamin` to `tetamax`)
        
    phimin, phimax : float, float; defaults: 0, 2*np.pi
        minimum and maximum azimuth angle in radians, excluding last position
        (in linear steps from `phimin` to `phimax`)
        
    Nteta, Nphi : int, int; defaults: 10, 36
        number of polar and azimuthal angles on sphere to calculate,
        
    polarizerangle : float or 'none', default: 'none'
        optional polarization filter angle **in degrees**(!). If 'none' (default), 
        the total field-intensity is calculated (= no polarization filter)
    
    return_value : str, default: 'map'
        Values to be returned. Either 'map' (default) or 'integrated'.
          - "map" : (default) return spatially resolved farfield intensity at each spherical coordinate (5 lists)
          - "efield" : return spatially resolved E-fields at each spherical coordinate (5 lists)
          - "int_Es" : return the integrated scattered field (as float)
          - "int_E0" : return the integrated fundamental field (as float)
          - "int_Etot" : return the integrated total field (as float)
          
    normalization_E0 : bool, default: False
        has only effect on return_value=="int_Es": Normalizes scattering 
        to peak of incident field intensity inside structure
        
    r0 : array, default: None
        [x,y,z] position of mulipole decomposition development. 
        If `None`, use structure's center of gravity
    
    which_moments : list of str, default: ['p', 'm', 'qe', 'qm']
        which multipole moments to use for farfield calculations. Supported:
            - 'p': electric dipole (full)
            - 'm': magnetic dipole
            - 'qe': electric quadrupole (full)
            - 'qm': magnetic quadrupole
            - 'p1': electric dipole (first order)
            - 'pt': toroidal dipole
            - 'qe1': electric quadrupole (first order)
            - 'qet': toroidal quadrupole
            
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation
    
    Returns
    -------
    using `r_probe` for position definition:
        3 lists of 6-tuples (x,y,z, Ex,Ey,Ez), complex : 
            - scattered Efield or E-intensity
            - total Efield (inlcuding fundamental field) or total E intensity
            - fundamental Efield (incident field) or E0 intensity
        
    if solid angle is defined via spherical coordinate range:
        - return_value == "map" : 5 arrays of shape (Nteta, Nphi) : 
            - [tetalist : teta angles - if solid angle range input]
            - [philist : phi angles - if solid angle range input]
            - I_sc : intensity of scattered field, 
            - I_tot : intensity of total field (I_tot=|E_sc+E_0|^2), 
            - I0 : intensity of incident field
        
        - return_value == "efield" : float
            - [tetalist : teta angles - if solid angle range input]
            - [philist : phi angles - if solid angle range input]
            - E_sc : complex scattered field at each pos.
            - E_tot : complex total field at each pos. (E_sc+E0)
            - E0 : complex incident field at each pos.
            
        - return_value == "int_XX" : float
            integrated total intensity over specified solid angle
        
    Notes
    -----
    See equation (G1) in
    
    Alaee, R., Rockstuhl, C. & Fernandez-Corbaton, I. *An electromagnetic 
    multipole expansion beyond the long-wavelength approximation.*
    Optics Communications 407, 17–21 (2018)
        
    """
# =============================================================================
#     exception handling
# =============================================================================
    if sim.E is None: 
        raise ValueError("Error: Scattering field inside the structure not yet evaluated. Run `core.scatter` simulation first.")
    
    if str(polarizerangle).lower() == 'none':
        polarizer = 0
    else:
        polarizer = polarizerangle * np.pi/180.
    
    if np.pi < tetamax < 0:
        raise ValueError("`tetamax` out of range, must be in [0, pi]")
    
    if r_probe is not None and return_value in ['int_es', 'int_E0', 'int_Etot']:
        raise ValueError("probing farfield on user-defined positions does not support integration " +
                         "of the intensity since no surface differential can be defined. Use spherical " +
                         "coordinate definition to do the integration.")
    
    which_moments = [wm.lower() for wm in which_moments]
    if ('p' in which_moments and 'p1' in which_moments) or ('p' in which_moments and 'pt' in which_moments):
        raise Exception("Please use one single electric dipole moment for farfield propagation.")
    if ('qe' in which_moments and 'qe1' in which_moments) or ('qe' in which_moments and 'qet' in which_moments):
        raise Exception("Please use one single electric quadrupole moment for farfield propagation.")
        
# =============================================================================
#     preparation
# =============================================================================
    from pyGDM2 import tools
    ## --- spherical probe coordinates
    if r_probe is None:
        tetalist = np.ones((int(Nteta), int(Nphi)))*np.linspace(tetamin, tetamax, int(Nteta))[:,None]
        philist = np.ones((int(Nteta), int(Nphi)))*np.linspace(phimin, phimax, int(Nphi), endpoint=False)[None,:]
        xff = (r * np.sin(tetalist) * np.cos(philist)).flatten()
        yff = (r * np.sin(tetalist) * np.sin(philist)).flatten()
        zff = (r * np.cos(tetalist)).flatten()
        _r_probe = np.transpose([xff, yff, zff])
    else:
        _r_probe = r_probe
        
    ## --- spherical integration steps
    dteta = (tetamax-tetamin) / float(Nteta-1)  # endpoint included
    dphi = (phimax-phimin) / float(Nphi)        # endpoint not included
    
    ## --- incident field config
    field_params    = tools.get_field_indices(sim)[field_index]
    wavelength      = field_params['wavelength']
    
    ## --- structure
    geo = sim.struct.geometry
    if r0 is None:
        r0 = np.average(geo, axis=0)
    n_vec = _r_probe - r0
    R_d = np.linalg.norm(n_vec, axis=1)
    n0_vec = n_vec / R_d[:,None]     # unit vector for direction of scattering
    
    ## --- environment
    sim.struct.setWavelength(wavelength)
    k0 = 2*np.pi / wavelength
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, geo[:1])[0]  # assume structure is fully in one environment
    n_env = (eps_env**0.5).real
    k = k0*n_env
    
#==============================================================================
#     electric polarization of structure, fundamental field
#==============================================================================        
    ## --- fundamental field - use dummy structure with 
    env_dict = sim.dyads.getConfigDictG(wavelength, sim.struct, sim.efield)
    if return_value == 'int_Es':
        from pyGDM2 import fields
        E0 = fields.nullfield(_r_probe, env_dict, wavelength, returnField='E')
    else:
        E0 = sim.efield.field_generator(_r_probe, env_dict, **field_params)
        
    
    p, p1, pt, m, Qe, Qe1, Qet, Qm = multipole_decomposition_exact(
                sim, field_index, r0=r0,
                which_moments=['p', 'p1', 'pt', 'm', 'qe', 'qe1', 'qet', 'qm'], 
                long_wavelength_approx=long_wavelength_approx)
    
    phase_factor = np.exp(1j*k*R_d)
    prefactor = k0**2 * phase_factor / (R_d)
    
    Es_p1 = prefactor[:,None] * np.cross(n0_vec, np.cross((p1)[None,:], n0_vec))
    Es_pt = prefactor[:,None] * np.cross(n0_vec, np.cross((pt)[None,:], n0_vec))    
    Es_p = Es_p1 + Es_pt
    Es_m = prefactor[:,None] * np.cross(m[None,:], n0_vec)
    
    Es_qe1 = prefactor[:,None] * 1j * k/6 * np.cross(n0_vec, 
                 np.cross(n0_vec, np.tensordot(Qe1, n0_vec, axes=(-1,-1)).T))
    Es_qet = prefactor[:,None] * 1j * k/6 * np.cross(n0_vec, 
                 np.cross(n0_vec, np.tensordot(Qet, n0_vec, axes=(-1,-1)).T))
    Es_qe = Es_qe1 + Es_qet
    Es_qm = prefactor[:,None] * 1j * k/6 * np.cross(n0_vec, 
                                    np.tensordot(Qm, n0_vec, axes=(-1,-1)).T)

    ## sum up all multipole fields
    Escat = np.zeros(shape=(len(_r_probe), 3), dtype=sim.efield.dtypec)
    if ('p1' in which_moments and 'pt' in which_moments) or 'p' in which_moments:
        Escat += Es_p
    elif 'p1' in which_moments:
        Escat += Es_p1
    elif 'pt' in which_moments:
        Escat += Es_pt
    if 'm' in which_moments:
        Escat += Es_m
    if ('qe1' in which_moments and 'qet' in which_moments) or 'qe' in which_moments:
        Escat += Es_qe
    elif 'qe1' in which_moments:
        Escat += Es_qe1
    elif 'qet' in which_moments:
        Escat += Es_qet
    if 'qm' in which_moments:
        Escat += Es_qm
    
    
    Iscat = np.sum((np.abs(Escat)**2), axis=1)


#==============================================================================
#    calc. fields through optional polarization filter
#==============================================================================
    if str(polarizerangle).lower() != 'none':
        ## --- scattered E-field parallel and perpendicular to scattering plane
        Es_par  = ( Escat.T[0] * np.cos(tetalist.flatten()) * np.cos(philist.flatten()) + 
                    Escat.T[1] * np.sin(philist.flatten()) * np.cos(tetalist.flatten()) - 
                    Escat.T[2] * np.sin(tetalist.flatten()) )
        Es_perp = ( Escat.T[0] * np.sin(philist.flatten()) - Escat.T[1] * np.cos(philist.flatten()) )
        ## --- scattered E-field parallel to polarizer
        Es_pol  = ( Es_par * np.cos(polarizer - philist.flatten()) - 
                    Es_perp * np.sin(polarizer - philist.flatten()) )
        
        ## --- fundamental E-field parallel and perpendicular to scattering plane
        E0_par  = ( E0.T[0] * np.cos(tetalist.flatten()) * np.cos(philist.flatten()) + 
                    E0.T[1] * np.sin(philist.flatten()) * np.cos(tetalist.flatten()) - 
                    E0.T[2] * np.sin(tetalist.flatten()) )
        E0_perp = ( E0.T[0] * np.sin(philist.flatten()) - E0.T[1] * np.cos(philist.flatten()) )
        ## --- fundamental E-field parallel to polarizer
        E0_pol  = ( E0_par * np.cos(polarizer - philist.flatten()) - 
                    E0_perp * np.sin(polarizer - philist.flatten()) )

#==============================================================================
#     Intensities with and without fundamental field / polarizer
#==============================================================================
    ## --- total field (no polarizer)
    if r_probe is None:
        out_shape = tetalist.shape
    else:
        out_shape = len(_r_probe)
        
    I_sc  = Iscat.reshape(out_shape)
    I0    = np.sum((np.abs(E0)**2), axis=1).reshape(out_shape)
    I_tot = np.sum((np.abs(E0 + Escat)**2), axis=1).reshape(out_shape)
    
    ## --- optionally: with polarizer
    if str(polarizerangle).lower() != 'none':
        I_sc  = (np.abs(Es_pol)**2).reshape(out_shape)
        I0    = (np.abs(E0_pol)**2).reshape(out_shape)
        I_tot = (np.abs(Es_pol + E0_pol)**2).reshape(out_shape)
    
    
    if return_value.lower() == 'map':
        if r_probe is None:
            return tetalist, philist, I_sc, I_tot, I0
        else:
            return I_sc, I_tot, I0
    elif return_value.lower() in ['efield', 'fields', 'field']:
        if r_probe is None:
            return tetalist, philist, Escat, Escat + E0, E0
        else:
            return Escat, Escat + E0, E0
    else:
        d_solid_surf = r**2 * np.sin(tetalist) * dteta * dphi
        if return_value.lower() == 'int_es':
            if normalization_E0:
                env_dict = sim.dyads.getConfigDictG(wavelength, sim.struct, sim.efield)
                E0 = sim.efield.field_generator(sim.struct.geometry, 
                                                env_dict, **field_params)
                I0_norm = np.sum(np.abs(E0)**2, axis=1).max()
            else:
                I0_norm = 1
            
            return np.sum(I_sc * d_solid_surf) / I0_norm
        
        elif return_value.lower() == 'int_e0':
            return np.sum(I0 * d_solid_surf)
        
        elif return_value.lower() == 'int_etot':
            return np.sum(I_tot * d_solid_surf)
        
        else:
            raise ValueError("Parameter 'return_value' must be one of ['map', 'int_es', 'int_e0', 'int_etot'].")









# =============================================================================
# multipole modes
# =============================================================================
def density_of_multipolar_modes(sim, field_index=None, wavelength=None, return_mode_energy=True, 
                                which_moments=['p', 'm', 'qe', 'qm'], 
                                method='lu', long_wavelength_approx=False):
    """Calculate total density of multipole modes via generalized polarizability
    
    If not yet calculated, will invoke generalize pola. calculation, thus it may
    require some computation time on the first call.
    

    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`
    
    energy_density : bool, optional
        whether to return the total mode energy (True) or the accumulated 
        multipole amplitude norm (False). The default is True.
    
    wavelength : float, default: None
        Optional wavelength (alternative to `field_index`) at which to 
        calculate susceptibility matrix (in nm). 
        Either `field_index` or `wavelength` must be given.
    
    which_moments : list of str, default: ['p', 'm', 'qe', 'qm']
        which multipole moments to calculate and return. supported dipole moments: 
            - 'p': electric dipole (full)
            - 'm': magnetic dipole
            - 'qe': electric quadrupole (full)
            - 'qm': magnetic quadrupole
            - 'p1': electric dipole (first order)
            - 'pt': toroidal dipole
            - 'qe1': electric quadrupole (first order)
            - 'qet': toroidal quadrupole
    
    method : string, default: "lu"
        inversion method if generalized pola. not yet calculated. 
        One of ["lu", "numpyinv", "scipyinv", "cupy", "cuda"]
    
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation
    

    Returns
    -------
    out_list : list of float
        total density of modes for each demanded order (= sum of tensor norms 
        of all generalized polarizabilities for each multipole)
    
    
    Notes
    -----
    For details , see: 
        
    *PAPER SUBMITTED*

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
    if field_index is not None:
        from pyGDM2 import tools
        wavelength = tools.get_field_indices(sim)[field_index]['wavelength']
    
    which_moments = [wm.lower() for wm in which_moments]
    for which_moment in which_moments:
        _test_availability_generalized_polarizability(sim, which_moment, 
                                                      wavelength, method=method, 
                                                      long_wavelength_approx=long_wavelength_approx)
    exp_order = 2 if return_mode_energy else 1
    
    out_list = []
    for wm in which_moments:
        if 'p' == wm:
            out_list.append((np.sum(np.linalg.norm(sim.K_P_E[wavelength], axis=(1,2))) + 
                            np.sum(np.linalg.norm(sim.K_T_E[wavelength], axis=(1,2))))**exp_order)
        if 'p1' == wm:
            out_list.append(np.sum(np.linalg.norm(sim.K_P_E[wavelength], axis=(1,2)))**exp_order)
        if 'pt' == wm:
            out_list.append(np.sum(np.linalg.norm(sim.K_T_E[wavelength], axis=(1,2)))**exp_order)
        if 'qe' == wm:
            out_list.append((np.sum(np.linalg.norm(sim.K_QE_E[wavelength], axis=(1,2))) +
                            np.sum(np.linalg.norm(sim.K_QT_E[wavelength], axis=(1,2))))**exp_order)
        if 'qe1' == wm:
            out_list.append(np.sum(np.linalg.norm(sim.K_QE_E[wavelength], axis=(1,2)))**exp_order)
        if 'qt' == wm:
            out_list.append(np.sum(np.linalg.norm(sim.K_QT_E[wavelength], axis=(1,2)))**exp_order)
        if 'm' == wm:
            out_list.append(np.sum(np.linalg.norm(sim.K_M_E[wavelength], axis=(1,2)))**exp_order)
        if 'qm' == wm:
            out_list.append(np.sum(np.linalg.norm(sim.K_QM_E[wavelength], axis=(1,2)))**exp_order)
    
    return out_list




