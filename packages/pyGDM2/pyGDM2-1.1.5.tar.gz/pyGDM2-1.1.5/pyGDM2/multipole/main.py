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


#==============================================================================
# GLOBAL PARAMETERS
#==============================================================================
DTYPE_C = np.complex64



#==============================================================================
# EXCEPTIONS
#==============================================================================



# =============================================================================
# CONSISTENCY TESTS
# =============================================================================


# =============================================================================
# MODULE FUNCTIONS
# =============================================================================
def multipole_decomposition_exact(sim, field_index, r0=None, epsilon=0.01, 
                                  which_moments=['p', 'm', 'qe', 'qm'],
                                  long_wavelength_approx=False):
    """exact multipole decomposition of the nanostructure optical response
    
    ** ------- FUNCTION STILL UNDER TESTING ------- **
    
    Multipole decomposition of electromagnetic field inside nanostructure for 
    electric and magnetic dipole and quadrupole moments.


    Parameters
    ----------
    sim : :class:`.core.simulation`
        simulation description
    
    field_index : int
        index of evaluated self-consistent field to use for calculation. Can be
        obtained for specific parameter-set using :func:`.tools.get_closest_field_index`
    
    r0 : array, default: None
        [x,y,z] position of multipole decomposition development. 
        If `None`, use structure's center of gravity
    
    epsilon : float, default: 0.01
        additional step on r0 (in nm) to avoid numerical divergence of the Bessel terms
        
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
    
    long_wavelength_approx : bool, default: False
        if True, use long wavelength approximation
            
    
    Returns
    -------
    list of multipole moments. Default:
        
    p : 3-vector
        electric dipole moment
    
    m : 3-vector
        magnetic dipole moment
    
    Qe : 3x3 tensor
        electric quadrupole moment
        
    Qm : 3x3 tensor
        magnetic quadrupole moment
    
    
    Notes
    -----
    For details about the method, see: 
    
    Alaee, R., Rockstuhl, C. & Fernandez-Corbaton, I. *An electromagnetic 
    multipole expansion beyond the long-wavelength approximation.*
    Optics Communications 407, 17–21 (2018)
    """
# =============================================================================
#     Exception handling
# =============================================================================
    if sim.E is None: 
        raise ValueError("Error: Scattered field inside the structure not yet " +
                         "evaluated. Run `scatter` or calculate generalized polarizabilities first.")
    
    which_moments = [wm.lower() for wm in which_moments]
    
# =============================================================================
#     preparation
# =============================================================================
    ## structure
    geo = sim.struct.geometry
    if r0 is None:
        r0 = np.average(geo, axis=0)
        sim.r0 = r0
    if np.abs(np.linalg.norm(geo - r0, axis=1)).min() > epsilon:
        epsilon = 0
    r = geo - r0 + epsilon                   # epsilon: avoid divergence of 1/kr when r=0
    norm_r = np.linalg.norm(r, axis=1)
    
    ## illumination properties
    field_params = sim.E[field_index][0]
    wavelength = field_params['wavelength']
    sim.struct.setWavelength(wavelength)
    eps_env = sim.dyads.getEnvironmentIndices(wavelength, r0[None,:])[0]  # assume structure is fully in one environment
    n_env = eps_env**0.5
    k = 2*np.pi*n_env / wavelength
    kr = k * norm_r
    
    ## electric polarization density of structure
    alpha_tensor = sim.dyads.getPolarizabilityTensor(wavelength, sim.struct)
    E = sim.E[field_index][1]
    P = np.matmul(alpha_tensor, E[...,None])[...,0]
    rP = np.einsum('ij, ij->i', r, P)
    
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
    
# =============================================================================
#     multipole calculation
# =============================================================================
    ## ----------- dipole moments
    ## electric dipole
    if 'p' in which_moments or 'p1' in which_moments or 'pt' in which_moments:
        p1 = np.sum(P * j0kr[..., None], axis=0)
        
        ## "toroidal" dipole
        p2 = k**2 * f_pt * np.sum((  f_ptA * rP[...,None]*r 
                                   + f_ptB * norm_r[..., None]**2 * P) * j2kr[..., None], 
                                  axis=0)
        
        p = p1 + p2
    
    ## magnetic dipole
    if 'm' in which_moments:
        m = -1j*k * f_m * np.sum(np.cross(r, P) * j1kr[..., None], axis=0)
    
    ## ----------- quadrupole moments
    ## electric quadrupole
    if 'qe' in which_moments or 'qe1' in which_moments or 'qet' in which_moments:
        Qe1 = np.zeros((3,3), dtype=np.complex64)
        Qe2 = np.zeros((3,3), dtype=np.complex64)
        for i_a in range(3):
            for i_b in range(3):
                
                ## diagonal term
                if i_a==i_b:
                    rP_delta = rP
                else:
                    rP_delta = 0
                
                ## electric quadrupole
                Qe1[i_a, i_b] = np.sum(
                    (
                       3 * (r[:,i_b]*P[...,i_a] + r[:,i_a]*P[...,i_b])
                     - 2*(rP_delta)
                     ) * j1kr)
                
                ## "toroidal" quadrupole
                Qe2[i_a, i_b] = np.sum(
                      (fqe2A*r[:,i_a]*r[:,i_b]*rP 
                      + norm_r**2 * (  fqe2B * (r[:,i_a]*P[:,i_b] + r[:,i_b]*P[:,i_a]) 
                                     + fqe2C * rP_delta)) * j3kr)
                
        Qe1 = f_qe * Qe1
        Qe2 = f_qe * fqe2 * k**2 * Qe2
        Qe = Qe1 + Qe2
    
    ## magnetic quadrupole
    if 'qm' in which_moments:
        Qm = np.zeros((3,3), dtype=np.complex64)
        for i_a in range(3):
            for i_b in range(3):
                Qm[i_a, i_b] = np.sum(
                    (r[:,i_a] * np.cross(r, P)[...,i_b] + 
                     r[:,i_b] * np.cross(r, P)[...,i_a]) * j2kr)
                
        Qm = -1j * k * f_qm * Qm
    
# =============================================================================
#     return results
# =============================================================================
    return_list = []
    for _m in which_moments:
        if _m.lower() == "p1":
            return_list.append(p1)
        if _m.lower() == "pt":
            return_list.append(p2)
        if _m.lower() == "p":
            return_list.append(p)
            
        if _m.lower() == "m":
            return_list.append(m)
            
        if _m.lower() == "qe1":
            return_list.append(Qe1)
        if _m.lower() == "qet":
            return_list.append(Qe2)
        if _m.lower() == "qe":
            return_list.append(Qe)
            
        if _m.lower() in ["qm"]:
            return_list.append(Qm)
    
    return return_list

