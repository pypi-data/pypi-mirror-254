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
#
"""
Collection of incident fields

authors: P. Wiecha, C. Majorel
"""

from __future__ import print_function
from __future__ import absolute_import

import warnings
import types
import cmath

import numpy as np
import numba




#==============================================================================
# globals
#==============================================================================
DTYPE_C = np.complex64



        

#==============================================================================
# field generator functions
#==============================================================================
def nullfield(pos, env_dict, wavelength, returnField='E', **kwargs):
    """Zero-Field
    
    all additional kwargs are ignored
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        placeholder for environment description. will be ignored in `nullfield`
    
    wavelength : float
        Wavelength in nm
    
    returnField : str
        placeholder. will be ignored in `nullfield`
    
    Returns:
    ----------
      Complex zero 3-vector at each coordinate in 'pos'
    
    """
    return np.zeros((len(pos), 3), dtype=DTYPE_C)




##----------------------------------------------------------------------
##                      INCIDENT FIELDS
##----------------------------------------------------------------------
@numba.njit(cache=True)
def _three_layer_pw(wavelength, theta_inc, polar, z_d, spacing, n1, n2, n3, x, y, z, E0=1.0):
    """oblique incident planewave, only linear polarization
    
    Oblique incidence (from bottom to top) through n1/n2/n3 layer interfaces. 
    May be used to simulate evanescent fields in the total internal 
    reflection configuration. Linear polarization.
    Amplitude = 1 for both, E and B.
    
    Original code by Ch. Girard, python implementation by C. Majorel
    
    Parameters
    ----------
    wavelength : float
        Wavelength in nm
    
    theta_inc : float, default: 0
        incident angle in the XZ plane with respect to e_z, in degrees.
         - 0deg = along Z (from neg to pos Z)
         - 90deg = along X  (from pos to neg X)
         - 180deg = along Z  (from pos to neg Z)
         - 270deg = along X  (from neg to pos X)
    
    polar : str, default: 's'
        incident linear polarization. Either 's' or 'p'. 
        At 0 degree incident angle, 's' is polarized along x, 'p' along y.
    
    z_d : float
        bottom interface position (along z) between media 1 and 2
    
    spacing : float
        spacing between bottom interface (between media 1 and 2) and 
        top interface position (between media 2 and 3)
    
    n1, n2, n3 : complex
        (complex) refractive index of each media 
    
    x, y, z : float
        x/y/z coordinates for computation of the fields
    
    E0 : float
        amplitude of E (and B) field
    
    Returns
    -------
      E0, B0:       Complex E-B-Fields at each dipole position as 
                    6 lists of the (complex) components: 
                    Ex, Ey, Ez, Bx, By, Bz
    """
    if E0 == 0.0:
        return 0.0j, 0.0j, 0.0j, 0.0j, 0.0j, 0.0j
    
    
    z_u = z_d + spacing             # z position of upper interface
    r = np.array([x, y, z]).astype(np.complex64)         # eval. position
    theta_r = theta_inc*np.pi/180.  # inc. angle in rad 
    k0 = 2*np.pi/wavelength         # wavevector in vacuum
    
    ## -- permittivities    
    eps1 = n1**2
    eps2 = n2**2
    eps3 = n3**2
    
    if theta_r > np.pi/2. and theta_r < 3*np.pi/2.:
    ## -- Different wavevectors    
        k1 = np.array([-n3*k0*cmath.sin(theta_r), 0. , -k0*cmath.sqrt(eps1-eps3*cmath.sin(theta_r)**2)]).astype(np.complex64)        ## -- transmitted wavevector in medium 1 (bottom layer)
        k2 = np.array([-n3*k0*cmath.sin(theta_r), 0. , -k0*cmath.sqrt(eps2-eps3*cmath.sin(theta_r)**2)]).astype(np.complex64)        ## -- transmitted wavevector in medium 2 (middle layer)
        k2p = np.array([-n3*k0*cmath.sin(theta_r), 0. , k0*cmath.sqrt(eps2-eps3*cmath.sin(theta_r)**2)]).astype(np.complex64)        ## -- reflected wavevector in medium 2 (middle layer)
        k3 = np.array([-n3*k0*cmath.sin(theta_r), 0. , n3*k0*cmath.cos(theta_r)]).astype(np.complex64)                               ## -- incident wavevector in medium 3 (top layer)
        k3p = np.array([-n3*k0*cmath.sin(theta_r), 0. , -n3*k0*cmath.cos(theta_r)]).astype(np.complex64)                             ## -- reflected wavevector in medium 3 (top layer)
        
    ## -- Phase terms    
        c1p = cmath.exp(1.0j*k1[2]*z_d)
        c1m = cmath.exp(-1.0j*k1[2]*z_d)
        c2p = cmath.exp(1.0j*k2[2]*z_d)
        c2m = cmath.exp(-1.0j*k2[2]*z_d)
        c2pp = cmath.exp(1.0j*k2[2]*z_u)
        c2pm = cmath.exp(-1.0j*k2[2]*z_u)
        c3pp = cmath.exp(1.0j*k3[2]*z_u)
        c3pm = cmath.exp(-1.0j*k3[2]*z_u)
        
    ## -- z - components of the wavevector/eps for magnetic modulus    
        k1gz = k1[2]/eps1
        k2gz = k2[2]/eps2
        k3gz = k3[2]/eps3               
        
    ### --- modulus electric field in s-polarized mode    
        delta = c3pm*c1p*(c2m*c2pp*(k2[2]**2+k1[2]*k3[2]+k3[2]*k2[2]+k1[2]*k2[2])+
                c2p*c2pm*(-k2[2]**2-k1[2]*k3[2]+k1[2]*k2[2]+k3[2]*k2[2]))
        
        delta3 = c3pp*c1p*(c2m*c2pp*(-k2[2]**2-k2[2]*k1[2]+k1[2]*k3[2]+k2[2]*k3[2])+
                  c2p*c2pm*(k2[2]**2-k2[2]*k1[2]+k2[2]*k3[2]-k1[2]*k3[2]))
        
        delta2 = 2.*c2m*c1p*(k1[2]*k3[2]+k3[2]*k2[2])
        
        delta2p = 2.*c2p*c1p*(k2[2]*k3[2]-k1[2]*k3[2])
        
        delta1 = 4.*k2[2]*k3[2]
        
        cep3 = delta3/delta
        ce2 = delta2/delta
        cep2 = delta2p/delta
        ce1 = delta1/delta
        
        
    ### --- modulus magnetic field in p-polarized mode
        deltam = c3pm*c1p*(c2m*c2pp*(k2gz**2+k1gz*k3gz+k3gz*k2gz+k1gz*k2gz)+
                c2p*c2pm*(-k2gz**2-k1gz*k3gz+k1gz*k2gz+k3gz*k2gz))
        
        delta3m = c3pp*c1p*(c2m*c2pp*(-k2gz**2-k2gz*k1gz+k1gz*k3gz+k2gz*k3gz)+
                  c2p*c2pm*(k2gz**2-k2gz*k1gz+k2gz*k3gz-k1gz*k3gz))
        
        delta2m = 2.*c2m*c1p*(k1gz*k3gz+k3gz*k2gz)
        
        delta2pm = 2.*c2p*c1p*(k2gz*k3gz-k1gz*k3gz)
        
        delta1m = 4.*k2gz*k3gz
        
        cmagp3 = delta3m/deltam
        cmag2 = delta2m/deltam
        cmagp2 = delta2pm/deltam
        cmag1 = delta1m/deltam


    ### --- Determination of the differents electric and magnetic field    
        if z>z_u:
            cphase3 = cmath.exp(1.0j*np.dot(k3,r))
            cphase3p = cmath.exp(1.0j*np.dot(k3p,r))
                
            if polar=='s':
                Ex = 0.
                Ey = cphase3+cep3*cphase3p
                Ez = 0.
                
                Bx = -cphase3*k3[2]/k0-(cep3*cphase3p*k3p[2]/k0)
                By = 0.
                Bz = cphase3*k3[0]/k0+(cep3*cphase3p*k3p[0]/k0)
                
            if polar=='p':
                Ex = n3*(-cphase3*k3[2]/(eps3*k0)-cmagp3*cphase3p*k3p[2]/(eps3*k0))
                Ey = 0.
                Ez = n3*(cphase3*k3[0]/(eps3*k0)+cmagp3*cphase3p*k3p[0]/(eps3*k0))
                
                Bx = 0.
                By = n3*(-cphase3-cmagp3*cphase3p)
                Bz = 0.
                
        elif z_d<z<z_u:
            cphase2 = cmath.exp(1.0j*np.dot(k2,r))
            cphase2p = cmath.exp(1.0j*np.dot(k2p,r))
                
            if polar=='s':
                Ex = 0.
                Ey = ce2*cphase2+cep2*cphase2p
                Ez = 0.
    
                Bx = -ce2*cphase2*k2[2]/k0-cep2*cphase2p*k2p[2]/k0
                By = 0.
                Bz = ce2*cphase2*k2[0]/k0+cep2*cphase2p*k2p[0]/k0
                
            if polar=='p':
                Ex = n3*(-cmag2*cphase2*k2[2]/(eps2*k0)-cmagp2*cphase2p*k2p[2]/(eps2*k0))
                Ey = 0.
                Ez = n3*(cmag2*cphase2*k2[0]/(eps2*k0)+cmagp2*cphase2p*k2p[0]/(eps2*k0))
                
                Bx = 0.
                By = n3*(-cmag2*cphase2-cmagp2*cphase2p)
                Bz = 0.
                
        else:
            cphase1 = cmath.exp(1.0j*np.dot(k1,r))
            
            if polar=='s':
                Ex = 0.
                Ey = ce1*cphase1
                Ez = 0.
                
                Bx = -ce1*cphase1*k1[2]/k0
                By = 0.
                Bz = ce1*cphase1*k1[0]/k0
            
            if polar=='p':
                Ex = n3*(-cmag1*cphase1*k1[2]/(eps1*k0))
                Ey = 0.
                # Ez = 1./n3*(cmag1*cphase1*k1[0]/(eps1*k0))  # <-- this was probably wrong
                Ez = n3*(cmag1*cphase1*k1[0]/(eps1*k0))
                
                Bx = 0.
                By = n3*(-cmag1*cphase1)
                Bz = 0.

    else :    
    ## -- Different wavevectors    
        k1 = np.array([-n1*k0*cmath.sin(theta_r), 0. , n1*k0*cmath.cos(theta_r)]).astype(np.complex64)                              ## -- incident wavevector in medium 1 (bottom layer)
        k1p = np.array([-n1*k0*cmath.sin(theta_r), 0. , -n1*k0*cmath.cos(theta_r)]).astype(np.complex64)                            ## -- reflected wavevector in medium 1 (bottom layer)
        k2 = np.array([-n1*k0*cmath.sin(theta_r), 0. , k0*cmath.sqrt(eps2-eps1*cmath.sin(theta_r)**2)]).astype(np.complex64)        ## -- transmitted wavevector in medium 2 (middle layer)
        k2p = np.array([-n1*k0*cmath.sin(theta_r), 0. , -k0*cmath.sqrt(eps2-eps1*cmath.sin(theta_r)**2)]).astype(np.complex64)      ## -- reflected wavevector in medium 2 (middle layer)
        k3 = np.array([-n1*k0*cmath.sin(theta_r), 0. , k0*cmath.sqrt(eps3-eps1*cmath.sin(theta_r)**2)]).astype(np.complex64)        ## -- transmitted wavevector in medium 3 (top layer)
        
    ## -- Phase terms    
        c1p = cmath.exp(1.0j*k1[2]*z_d)
        c1m = cmath.exp(-1.0j*k1[2]*z_d)
        c2p = cmath.exp(1.0j*k2[2]*z_d)
        c2m = cmath.exp(-1.0j*k2[2]*z_d)
        c2pp = cmath.exp(1.0j*k2[2]*z_u)
        c2pm = cmath.exp(-1.0j*k2[2]*z_u)
        c3pp = cmath.exp(1.0j*k3[2]*z_u)
        c3pm = cmath.exp(-1.0j*k3[2]*z_u)
        
    ## -- z - components of the wavevector/eps for magnetic modulus    
        k1gz = k1[2]/eps1
        k2gz = k2[2]/eps2
        k3gz = k3[2]/eps3
        
    ### --- modulus electric field in s-polarized mode    
        delta = c3pp*c1m*(c2m*c2pp*(-k2[2]**2-k3[2]*k1[2]+k2[2]*k3[2]+k2[2]*k1[2])+
                c2p*c2pm*(k1[2]*k2[2]+k3[2]*k1[2]+k3[2]*k2[2]+k2[2]**2))
        
        delta1 = c3pp*c1p*(c2m*c2pp*(k2[2]**2-k3[2]*k2[2]+k1[2]*k2[2]-k1[2]*k3[2])+
                  c2p*c2pm*(-k2[2]**2-k3[2]*k2[2]+k1[2]*k3[2]+k1[2]*k2[2]))
        
        delta2 = 2.*c3pp*c2pm*(k1[2]*k2[2]+k1[2]*k3[2])
        
        delta2p = 2.*c3pp*c2pp*(k1[2]*k2[2]-k1[2]*k3[2])
        
        delta3 = 4.*k1[2]*k2[2]
        
        cep1 = delta1/delta
        ce2 = delta2/delta
        cep2 = delta2p/delta
        ce3 = delta3/delta
        
        
    ### --- modulus magnetic field in p-polarized mode
        deltam = c3pp*c1m*(c2m*c2pp*(-k2gz**2-k3gz*k1gz+k2gz*k3gz+k2gz*k1gz)+
                c2p*c2pm*(k1gz*k2gz+k3gz*k1gz+k3gz*k2gz+k2gz**2))
        
        delta1m = c3pp*c1p*(c2m*c2pp*(k2gz**2-k3gz*k2gz+k1gz*k2gz-k1gz*k3gz)+
                  c2p*c2pm*(-k2gz**2-k3gz*k2gz+k1gz*k3gz+k1gz*k2gz))
        
        delta2m = 2.*c3pp*c2pm*(k1gz*k2gz+k1gz*k3gz)
        
        delta2pm = 2.*c3pp*c2pp*(k1gz*k2gz-k1gz*k3gz)
        
        delta3m = 4.*k1gz*k2gz
        
        cmagp1 = delta1m/deltam
        cmag2 = delta2m/deltam
        cmagp2 = delta2pm/deltam
        cmag3 = delta3m/deltam
    
    ### --- Determination of the differents electric and magnetic field    
        if z<z_d:
            cphase1 = cmath.exp(1.0j*np.dot(k1,r))
            cphase1p = cmath.exp(1.0j*np.dot(k1p,r))
                
            if polar=='s':
                Ex = 0.
                Ey = cphase1+cep1*cphase1p
                Ez = 0.
                
                Bx = -cphase1*k1[2]/k0-(cep1*cphase1p*k1p[2]/k0)
                By = 0.
                Bz = cphase1*k1[0]/k0+(cep1*cphase1p*k1p[0]/k0)
                
            if polar=='p':
                Ex = n1*(-cphase1*k1[2]/(eps1*k0)-cmagp1*cphase1p*k1p[2]/(eps1*k0))
                Ey = 0.
                Ez = n1*(cphase1*k1[0]/(eps1*k0)+cmagp1*cphase1p*k1p[0]/(eps1*k0))
                
                Bx = 0.
                By = n1*(-cphase1-cmagp1*cphase1p)
                Bz = 0.
                
        elif z_d<z<z_u:
            cphase2 = cmath.exp(1.0j*np.dot(k2,r))
            cphase2p = cmath.exp(1.0j*np.dot(k2p,r))
                
            if polar=='s':
                Ex = 0.
                Ey = ce2*cphase2+cep2*cphase2p
                Ez = 0.
                
                Bx = -ce2*cphase2*k2[2]/k0-cep2*cphase2p*k2p[2]/k0
                By = 0.
                Bz = ce2*cphase2*k2[0]/k0+cep2*cphase2p*k2p[0]/k0
            
            if polar=='p':
                Ex = n1*(-cmag2*cphase2*k2[2]/(eps2*k0)-cmagp2*cphase2p*k2p[2]/(eps2*k0))
                Ey = 0.
                Ez = n1*(cmag2*cphase2*k2[0]/(eps2*k0)+cmagp2*cphase2p*k2p[0]/(eps2*k0))
                
                Bx = 0.
                By = n1*(-cmag2*cphase2-cmagp2*cphase2p)
                Bz = 0.
                
                
        else:
            cphase3 = cmath.exp(1.0j*np.dot(k3,r))
            
            if polar=='s':
                Ex = 0.
                Ey = ce3*cphase3
                Ez = 0.
               
                Bx = -ce3*cphase3*k3[2]/k0
                By = 0.
                Bz = ce3*cphase3*k3[0]/k0
            
            if polar=='p':
                Ex = n1*(-cmag3*cphase3*k3[2]/(eps3*k0))
                Ey = 0.
                # Ez = 1./n1*(cmag3*cphase3*k3[0]/(eps3*k0))  # <-- this was probably wrong
                Ez = n1*(cmag3*cphase3*k3[0]/(eps3*k0))
                
                Bx = 0.
                By = n1*(-cmag3*cphase3)
                Bz = 0.
    
    return E0*Ex, E0*Ey, E0*Ez, E0*Bx, E0*By, E0*Bz


# =============================================================================
# interface to `_three_layer_pw`
# =============================================================================
def plane_wave(pos, env_dict, wavelength, 
               inc_angle=180, inc_plane='xz',
               theta=None,
               E_s=0.0, E_p=1.0, phase_Es=0.0, phase=0.0,
               returnField='E'):
    """generalized incident planewave
    
    supports oblique angles, arbitrary polarization states, 2 interfaces.
    Default config gives incident plane wave from top (z), 
    linear polarized along x, with amplitude 1
    
    Original code by Ch. Girard, python implementation by C. Majorel
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
        
    wavelength : float
        Wavelength in nm
    
    inc_angle : float, default: 180
        incident angle with respect to e_z, in degrees. Default is inc from top.
         - 0deg = along Z (from neg to pos Z)
         - 90deg = along X ['xz'], along Y ['yz'] (from pos to neg)
         - 180deg = along Z  (from pos to neg Z)
         - 270deg = along X ['xz'], along Y ['yz'] (from neg to pos)
    
    inc_plane : str, default: 'xz'
        plane of incidence, one of ['xz', 'yz']
        
    theta : float, default: None
        alternative specification for a linear polarization angle. 
        If given, this will override `E_s` and `E_p` as well as their respective phases.
        In degrees. 
        At normal incidence: 0deg = OX, 90deg = OY.
        If `inc_plane`=='xz': 0deg --> p-polarization; 90deg --> s-polarization
        (inverse for `inc_plane`=='yz')
        
    
    E_s, E_p : float, default: 0.0, 1.0
        Apmplitudes of s-polarized and p-polarized plane wave components.
        At 0 / 180 degrees incident angle (normal incindence), 'p' is 
        polarized along x, 's' along y. Then, at 90deg 'p' is along z.
    
    phase_Es : float, default: 0.0
        additional phase for E_s component (in rad). 
        Can be used to generate elliptic polarization.
        For instance, left circular polarization (LCP) can be obtained with:
        E_s=np.sqrt(0.5), E_p=np.sqrt(0.5), phase_Es=-np.pi/2. 
        RCP: phase_Es=+np.pi/2.
        
    phase : float, default: 0.0
        additional absolute phase for entire plane wave (in rad).
    
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B' or 'H': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                    list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]
    """
    if ('eps1' not in env_dict.keys() or 'eps2' not in env_dict.keys() or
        'eps3' not in env_dict.keys() or 'spacing' not in env_dict.keys()):
        raise ValueError("`env_dict` must contain ['eps1', 'eps2', 'eps3', 'spacing']")
    
    cn1 = env_dict['eps1']**0.5
    cn2 = env_dict['eps2']**0.5
    cn3 = env_dict['eps3']**0.5
    spacing = np.float32(env_dict['spacing'].real)
    z_d = 0   # position of lower interface
    
    ## -- convert angles 90 and 270 close to horizontal angles to avoid divergence
    if inc_angle in [-90, 90, -270, 270] and (cn1!=cn2 or cn2!=cn3):
        warnings.warn("Using interface with horizontal angle of incidence!" + 
                      "Please make sure if horizontal incidence makes sense in presence of an interface.")    
    if inc_angle in [-90, 90]:
        inc_angle += 0.05
    if inc_angle in [-270, 270]:
        inc_angle -= 0.05
    
    
    Ex = np.asfortranarray( np.zeros(len(pos)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(pos)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(pos)), dtype=DTYPE_C)
    
    if theta is not None:
        if inc_angle not in [0, 180]: 
            warnings.warn("non-normal incident angle, to avoid ambiguities, " +
                          "the polarization of a plane wave should not be " +
                          "defined via the `theta` keyword.")
        E_p = 1.0 * np.cos(theta * np.pi/180.)
        E_s = 1.0 * np.sin(theta * np.pi/180.)
    
    ## normalize incident amplitude by refractive index
    # if abs(inc_angle)<90 and np.abs(cn1)!=1: # inc from zone n1
    #     E_s = E_s / cn1**0.5
    #     E_p = E_p / cn1**0.5
    # elif abs(inc_angle)>=90 and np.abs(cn3)!=1: # inc from zone n3
    #     E_s = E_s / cn3**0.5
    #     E_p = E_p / cn3**0.5
    
    for i,R in enumerate(pos):
        if inc_plane.lower() in ['yz', 'zy']:
            y,x,z = R
        else:
            x,y,z = R
    
        ex_s,ey_s,ez_s, bx_s,by_s,bz_s = _three_layer_pw(
            wavelength, inc_angle, 's', z_d, spacing, cn1, cn2, cn3, x, y, z, E0=E_s)
    
        ex_p,ey_p,ez_p, bx_p,by_p,bz_p = _three_layer_pw(
            wavelength, inc_angle, 'p', z_d, spacing, cn1, cn2, cn3, x, y, z, E0=E_p)
        
        ## additional phases:
        ex_p = ex_p * np.exp(1j * phase)
        ey_p = ey_p * np.exp(1j * phase)
        ez_p = ez_p * np.exp(1j * phase)
        bx_p = bx_p * np.exp(1j * phase)
        by_p = by_p * np.exp(1j * phase)
        bz_p = bz_p * np.exp(1j * phase)
        ex_s = ex_s * np.exp(1j * (phase_Es + phase))
        ey_s = ey_s * np.exp(1j * (phase_Es + phase))
        ez_s = ez_s * np.exp(1j * (phase_Es + phase))
        bx_s = bx_s * np.exp(1j * (phase_Es + phase))
        by_s = by_s * np.exp(1j * (phase_Es + phase))
        bz_s = bz_s * np.exp(1j * (phase_Es + phase))
        
        ## optional scattering plane modification
        if inc_plane.lower() in ['yz', 'zy']:
            ex_s,ey_s,ez_s = -ey_s,-ex_s,-ez_s
            bx_s,by_s,bz_s = by_s,bx_s,bz_s
            
            ex_p,ey_p,ez_p = -ey_p,-ex_p,-ez_p
            bx_p,by_p,bz_p = by_p,bx_p,bz_p
        
        if returnField.lower() == 'e':
            Ex[i], Ey[i], Ez[i] = ex_s+ex_p, ey_s+ey_p, ez_s+ez_p
        else:
            Ex[i], Ey[i], Ez[i] = bx_s+bx_p, by_s+by_p, bz_s+bz_p
        
    Evec = np.transpose([Ex, Ey, Ez])
    return Evec





    


def gaussian(pos, env_dict, wavelength, 
             theta=None, polarization_state=None, 
                 xSpot=0.0, ySpot=0.0, zSpot=0.0, 
                 NA=-1.0, spotsize=-1.0, kSign=-1.0, 
                 paraxial=False, phase=0.0, E0=complex(1,0),
                 returnField='E'):
    """Simple, normal incident (along Z) focused Gaussian Beam Field
    
    For more advanced options, use fields from `focused_beams` module.
    
    obligatory "einKwargs" are one of 'theta' or 'polarization_state' and 
    one of 'NA' or 'spotsize'
    
    polarization is defined by one of the two kwargs:
     - theta: linear polarization angle in degrees, theta=0 --> along X. 
              Amplitude = 1 for both, E and B 
     - polarization_state. tuple (E0x, E0y, Dphi, phi): manually 
              define x and y amplitudes, phase difference and 
              absolute phase of plane wave.
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
    
    wavelength : float
        Wavelength in nm
     
    theta : float, default: None
        either 'theta' or 'polarization_state' must be given.
        linear polarization angle in degrees, 0deg = 0X direction
    
    polarization_state : 4-tuple of float, default: None
        either 'theta' or 'polarization_state' must be given.
        polarization state with field amplitudes and phases, tuple of 4 float:
        (E0x, E0y, Dphi, Aphi): E0X amplitde, E0Y amplitde, phase difference 
        between X and Y components (in rad), absolute phase of plane wave (in rad).
        The field is then calculated as E = (E0x, E0y*exp(i*Dphi*z), 0)*exp(i*Aphi*z).
        Note that this means the handedness depends on the propagation direction (*kSign*)!
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (kSign=-1, E0x=1, E0y=1, Dphi=np.pi/2., phi=0)
        
      xSpot,ySpot,zSpot : float, default: 0,0,0
          x/y/z coordinates of focal point
      
      NA : float
          Numerical aperture to calculate beamwaist
      
      spotsize : float (optional)
          Gaussian beamwaist (overrides "NA")
      
      kSign : float, default: -1
          Direction of Beam. -1: top to Bottom, 1 Bottom to top
      
      paraxial : bool, default: False
          Use paraxial Gaussian beam: No longitudinal fields.
          If "False", longitudinal components are obtained using Maxwell 
          equation div(E)=0 as condition
         
      phase : float, default: 0
          additional phase of the beam, in degrees
      
      E0 : complex or function, default: complex(1,0)
          Either complex value or function of r=(x, y) (normalized to units of waist!).
          In case of a function, it needs to return the  complex amplitude at 
          the given position relative to beam axis (pos. in units of waist).
    
      returnField : str, default: 'E'
          if 'E': returns electric field; if 'B' or 'H': magnetic field
    
    Returns
    -------
      E0:       Complex E-Field at each dipole position
      
    
    Notes
    -----
     - paraxial correction : 
         see: Novotny & Hecht. "Principles of nano-optics". Cambridge University Press (2006)

    
    """
    if (theta is None and polarization_state is None) or (theta is not None and polarization_state is not None):
        raise ValueError("exactly one argument of 'theta' and 'polarization_state' must be given.")
    if theta is not None:
        polarization_state = (1.0 * np.cos(theta * np.pi/180.), 
                              1.0 * np.sin(theta * np.pi/180.), 
                              0, 0)
    
    xm, ym, zm = np.transpose(pos)
    
    if 'eps_env' in env_dict.keys():
        cn1 = cn2 = env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        # spacing = env_dict['spacing']**0.5
        if cn1 != cn2 or cn2 != cn3:
            warnings.warn("`gaussian` only supports vacuum environment so far. " +
                          "A simulation with interface might not yield correct results.")
    
    Ex = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    
    
    ## beamwaist
    if spotsize == NA == -1:
        raise ValueError("Focused Beam Error! Either spotsize or NA must be given.")
    elif spotsize == -1:
        w0 = 2*wavelength/(NA*np.pi)
    else:
        w0 = spotsize
    
    ## waist, curvature and gouy-phase
    def w(z, zR, w0):
        return w0 * np.sqrt(1 + (z/zR)**2)
    
    def R(z, zR):
        return z*( 1 + (zR/z)**2 )
    
    def gouy(z, zR):
        return np.arctan2(z,zR)
    
    ## constant parameters
    k = kSign*cn2 * (2*np.pi / wavelength)    #incidence from positive Z
    zR = np.pi*w0**2 / wavelength
    
    r2 = (xm-xSpot)**2+(ym-ySpot)**2
    z = zm-zSpot
    
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    
    ##  --------- Electric field --------- 
    r = np.transpose([xm-xSpot, ym-ySpot])
    waist = w(z,zR,w0)
    if isinstance(E0, complex):
        _E0 = E0
    elif isinstance(E0, types.FunctionType):
        _E0 = E0(r / waist[:,None])
    else:
        raise Exception("Wrong type for complex amplitude `E0`. Must be `complex` or `function`.")
    E = _E0 * (w0 / waist * np.exp(-r2 / waist**2 ) * 
            np.exp(1j * (k*z + k*r2/(2*R(z,zR)) - gouy(z, zR)) )) * np.exp(1j*phase*np.pi/180.)
    
    if returnField.lower() == 'e':
        abs_phase = np.exp(1j * Aphi)     # add an absolute phase
        Ex = E * E0x * abs_phase
        Ey = E * E0y * np.exp(1j * Dphi) * abs_phase
    else:
    ##  --------- Magnetic field --------- 
        abs_phase = -1*np.exp(1j * Aphi)     # add an absolute phase
        Ex = -1*E * E0y*np.exp(1j * Dphi) * abs_phase
        Ey = E * E0x * abs_phase        
    
    ## obtained longitudinal component using condition div(E)==0
    if paraxial:
        Ez = np.zeros(len(E))   # <-- paraxial gaussian beam: No longitudinal E-component
    else:
        Ez = (-1j * 2 / (k * w(z,zR,w0)**2)) * \
                ((xm-xSpot) * Ex + (ym-ySpot) * Ey)
    
    Evec = np.transpose([Ex, Ey, Ez]).astype(DTYPE_C)
    return Evec 




def dipole_electric(pos, env_dict, wavelength, 
                    x0,y0,z0, mx,my,mz, returnField='E', 
                    R_farfield_approx=-1):
    """field emitted by an electric dipole at (x0,y0,z0) with complex amplitude (mx,my,mz)
    
    mandatory kwargs along with `wavelength` are: `x0`, `y0`, `z0`, `mx`, `my`, `mz`
    
    To take into account a dielectric interface, `dipole_electric` uses a 
    mirror-charge approximation in the (quasistatic) near-field and an 
    asymptotic approximation for the far-field. Can handle only a single interface
    (hence cases with n1 != n2 = n3).
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain either "eps_env" or ["eps1", "eps2"].
    
    wavelength : float
        Wavelength in nm
    
    x0,y0,z0 : float
        x/y/z coordinates of electric dipole position
          
    mx,my,mz : float
        x/y/z amplitude of elec. dipole vector
          
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B' or 'H': magnetic field
          
    R_farfield_approx : float, default: -1
        optional emitter-observer distance (in nm) starting from which an asymptotic 
        farfield approximation will be used (to be used with caution!).
        `-1`: Do not use far-field approximation. 
    
    Returns
    -------
    E0/H0:   Complex field at each position ( (Ex,Ey,Ez)-tuples )
    
    Notes
    -----
    
    for free-space propagators, see e.g. 
    G. S. Agarwal, *Phys. Rev. A*, 11(230), (1975), Eqs. (4.5)/(4.6)
    
    """
    from pyGDM2.propagators import Gtot_EE_123 as GEE
    from pyGDM2.propagators import Gs_EE_asymptotic as GEE_ff
    from pyGDM2.propagators import G_HE_123 as GHE
    
    if 'eps_env' in env_dict.keys():
        eps1 = eps2 = eps3 = env_dict['eps_env']
        spacing = 5000
    else:
        eps1 = env_dict['eps1']
        eps2 = env_dict['eps2']
        eps3 = env_dict['eps3']
        spacing = np.float32(env_dict['spacing'].real)
        if eps2 != eps3:
            warnings.warn("dipole_electric only supports a single interface " + 
                          "(between `n1`/`n2`). " +
                          "The simulation might not be a good approximation.")
    
    
    R1 = np.array([x0, y0, z0])  # emitter location
    p = np.array([mx, my, mz])   # emitter dipole moment
    
    Ex = np.zeros(len(pos), dtype=DTYPE_C)
    Ey = np.zeros(len(pos), dtype=DTYPE_C)
    Ez = np.zeros(len(pos), dtype=DTYPE_C)
    
    ## calc propagator
    for i,R2 in enumerate(pos):
        if returnField.lower() == 'e':
            ## --- emitted electric field
            if np.linalg.norm(R2-R1) <= R_farfield_approx or R_farfield_approx == -1:
                ## mirror-charge NF approximation
                xx, yy, zz, xy, xz, yx, yz, zx, zy \
                        = GEE(R1, R2, wavelength, eps1, eps2, eps3, spacing)
            else:
                ## asymptotic farfield approximation:
                xx, yy, zz, xy, xz, yx, yz, zx, zy \
                        = GEE_ff(R1, R2, wavelength, eps1, eps2, eps3, spacing)
                
        else:
            ## --- emitted magnetic field
            xx, yy, zz, xy, xz, yx, yz, zx, zy \
                    = GHE(R1, R2, wavelength, eps1, eps2, eps3, spacing)
        
        ## propagate the dipole
        G = np.array([[xx,xy,xz],
                      [yx,yy,yz],
                      [zx,zy,zz]])
        E = np.matmul(G, p)
        
        Ex[i] = E[0]
        Ey[i] = E[1]
        Ez[i] = E[2]
    
    return np.transpose([Ex, Ey, Ez])


def dipole_magnetic(pos, env_dict, wavelength, 
                    x0,y0,z0, mx,my,mz, returnField='E', 
                    R_farfield_approx=-1):
    """field emitted by a magnetic dipole at (x0,y0,z0) with complex amplitude (mx,my,mz)
    
    mandatory kwargs along with `wavelength` are: `x0`, `y0`, `z0`, `mx`, `my`, `mz`
    
    To take into account a dielectric interface, `dipole_magnetic` uses a 
    mirror-charge approximation in the (quasistatic) near-field and an 
    asymptotic approximation for the far-field. Can handle only a single interface
    (hence cases with n1 != n2 = n3).
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain either "eps_env" or ["eps1", "eps2"].
    
    wavelength : float
        Wavelength in nm
    
    x0,y0,z0 : float
        x/y/z coordinates of electric dipole position
          
    mx,my,mz : float
        x/y/z amplitude of elec. dipole vector
          
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B' or 'H': magnetic field
          
    R_farfield_approx : float, default: -1
        optional emitter-observer distance (in nm) starting from which an asymptotic 
        farfield approximation will be used (to be used with caution!).
        `-1`: Do not use far-field approximation. 
    
    Returns
    -------
    E0/H0:   Complex field at each position ( (Ex,Ey,Ez)-tuples )
    
    Notes
    -----
    
    for free-space propagators, see e.g. 
    G. S. Agarwal, *Phys. Rev. A*, 11(230), (1975), Eqs. (4.5)/(4.6)
    
    """
    from pyGDM2.propagators import Gtot_EE_123 as GEE
    from pyGDM2.propagators import Gs_EE_asymptotic as GEE_ff
    from pyGDM2.propagators import G_HE_123 as GHE
    
    if 'eps_env' in env_dict.keys():
        eps1 = eps2 = eps3 = env_dict['eps_env']
        spacing = 5000
    else:
        eps1 = env_dict['eps1']
        eps2 = env_dict['eps2']
        eps3 = env_dict['eps3']
        spacing = np.float32(env_dict['spacing'].real)
        if eps2 != eps3:
            warnings.warn("dipole_electric only supports a single interface " + 
                          "(between `n1`/`n2`). " +
                          "The simulation might not be a good approximation.")
    
    
    R1 = np.array([x0, y0, z0])  # emitter location
    p = np.array([mx, my, mz])   # emitter dipole moment
    
    Ex = np.zeros(len(pos), dtype=DTYPE_C)
    Ey = np.zeros(len(pos), dtype=DTYPE_C)
    Ez = np.zeros(len(pos), dtype=DTYPE_C)
    
    ## calc propagator
    for i,R2 in enumerate(pos):
        if returnField.lower() == 'e':
            ## --- emitted electric field
            ## GEH(R1, R2) = GHE(R2, R1)
            xx, yy, zz, xy, xz, yx, yz, zx, zy \
                    = GHE(R2, R1, wavelength, eps1, eps2, eps3, spacing)
                
        else:
            ## --- emitted magnetic field
            ## GEE(R1, R2) = GHH(R1, R2)
            if np.linalg.norm(R2-R1) <= R_farfield_approx or R_farfield_approx == -1:
                ## mirror-charge NF approximation
                xx, yy, zz, xy, xz, yx, yz, zx, zy \
                        = GEE(R1, R2, wavelength, eps1, eps2, eps3, spacing)
            else:
                ## asymptotic farfield approximation:
                xx, yy, zz, xy, xz, yx, yz, zx, zy \
                        = GEE_ff(R1, R2, wavelength, eps1, eps2, eps3, spacing)
        
        ## propagate the dipole
        G = np.array([[xx,xy,xz],
                      [yx,yy,yz],
                      [zx,zy,zz]])
        E = np.matmul(G, p)
        
        Ex[i] = E[0]
        Ey[i] = E[1]
        Ez[i] = E[2]
    
    return np.transpose([Ex, Ey, Ez])






if __name__ == "__main__":
    pass
