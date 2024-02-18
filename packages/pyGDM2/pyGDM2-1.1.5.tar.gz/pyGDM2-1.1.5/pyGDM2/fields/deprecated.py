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
legacy incident fields for backward compatibility
"""

from __future__ import print_function
from __future__ import absolute_import

import warnings
import numpy as np
from pyGDM2.fields.regular import _three_layer_pw


#==============================================================================
# globals
#==============================================================================
DTYPE_C = np.complex64


        

#==============================================================================
# field generator functions
#==============================================================================


##----------------------------------------------------------------------
## deprecated functions for backwards compatibilitiy
##     (may be removed in future version)
##----------------------------------------------------------------------
def planewave(pos, env_dict, wavelength,
              theta=None, polarization_state=None, 
              kSign=-1, returnField='E', deprecationwarning=True, **kwargs):
    """Normally incident (along Z) planewave in homogeneous environment
    
    *DEPRECATED* - Use :func:`.plane_wave` instead.
    
    polarization is defined by one of the two kwargs:
     - theta: linear polarization angle in degrees, theta=0 --> along X. 
              Amplitude = 1 for both, E and B 
     - polarization state. tuple (E0x, E0y, Dphi, phi): manually 
              define x and y amplitudes, phase difference and 
              absolute phase of plane wave.
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain either "eps_env" or ["eps2"].
    
    wavelength : float
        Wavelength in nm
    
    theta : float, default: None
        either 'theta' or 'polarization_state' must be given.
        linear polarization angle in degrees, 0deg = 0X direction.
    
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
                - example: left circular pol. with (1, 1, np.pi/2., 0) and kSign=-1
    
    kSign : int, default: -1
        sign of wavenumber. 
        +1: propagation from bottom to top (towards increasing z)
        -1: propagation from top to bottom (towards smaller z, default)
        either kSign or k0 must be given.
    
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B' or 'H': magnetic field
    
    deprecationwarning : bool, default: True
        whether or not to emit a deprecation warning
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                     list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]
    """
    ## --------- deprecation warning
    if deprecationwarning:
        warnings.warn("`planewave` is deprecated and supports only normal incidence/homogeneous environments. " +
                      "It is recommended to using `plane_wave` instead (with underscore in function name).",
                      DeprecationWarning)
    
    
    
    if (theta is None and polarization_state is None) or (theta is not None and polarization_state is not None):
        raise ValueError("exactly one argument of 'theta' and 'polarization_state' must be given.")
    
    if kSign not in [-1, 1]:
        raise ValueError("planewave: kSign must be either +1 or -1!")
    
    xm, ym, zm = np.transpose(pos)
    
    if 'eps_env' in env_dict.keys():
        n_env = np.ones(len(zm), dtype=np.complex64) * env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        spacing = env_dict['spacing']**0.5
        if cn1 != cn3 or cn2 != cn3:
            warnings.warn("`planewave` only supports a homogeneous environment. " +
                          "The simulation will not be correct. " + 
                          "Consider using `plane_wave` or `evanescent_planewave`.")
        n_env = np.ones(len(zm), dtype=np.complex64)
        n_env[zm<0] = n_env[zm<0]*cn1
        n_env[np.logical_and(zm>=0, zm<spacing)] = n_env[np.logical_and(zm>=0, zm<spacing)]*cn2
        n_env[zm>=spacing] = n_env[zm>=spacing]*cn3
    
    if theta is not None:
        polarization_state = (1.0 * np.cos(theta * np.pi/180.), 
                              1.0 * np.sin(theta * np.pi/180.), 
                              0, 0)
    
    
    ## constant parameters
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # kz = kSign*cn2 * (2*np.pi / wavelength)    #incidence from positive Z
    kz = kSign*n_env * (2*np.pi / wavelength)    #incidence from positive Z
    
    ## amplitude and polarization
    ##  --------- Electric field --------- 
    E = np.ones((len(zm), 3), dtype=DTYPE_C)
    if returnField.lower() == 'e':
        abs_phase = np.exp(1j * (kz*zm + Aphi))     # absolute phase
        E.T[0] *= E0x * abs_phase
        E.T[1] *= E0y*np.exp(1j * Dphi) * abs_phase
        E.T[2] *= 0 * abs_phase
    ##  --------- Magnetic field --------- 
    else:
        abs_phase = -1*np.exp(1j * (kz*zm + Aphi))     # absolute phase
        E.T[0] *= -1*E0y*np.exp(1j * Dphi) * abs_phase
        E.T[1] *= E0x * abs_phase
        E.T[2] *= 0 * abs_phase
    
    return E
    

    
def focused_planewave(pos, env_dict, wavelength, 
                      theta=None, polarization_state=None, 
                      xSpot=0.0, ySpot=0.0, 
                      NA=-1.0, spotsize=-1.0, kSign=-1, phase=0.0,
                      consider_substrate_reflection=False, returnField='E'):
    """Normally incident (along Z) planewave with gaussian intensity profile
    
    *DEPRECATED* - Use :func:`.gaussian` instead.
    
    focused at (x0,y0)
    
    polarization is defined by one of the two kwargs:
      - theta: linear polarization angle in degrees, theta=0 --> along X. 
              Amplitude = 1 for both, E and B 
      - polarization state. tuple (E0x, E0y, Dphi, phi): manually 
              define x and y amplitudes, phase difference and 
              absolute phase of plane wave.
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain either "eps_env" or ["eps2"].
    
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
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)
    
    xSpot, ySpot : float, float, default: 0, 0
        focal spot position (in nm)
    
    kSign : int, default: -1
        sign of wavenumber. 
        +1: propagation from bottom to top (towards increasing z)
        -1: propagation from top to bottom (towards smaller z, default)
       
    phase : float, default: 0
          additional phase of the beam, in degrees
          
    consider_substrate_reflection : bool, default: False
        Whether to consider the reflection / transmission coefficient at the
        substrate for adjusting the field amplitude
        
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                      list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]
    """
    ## --------- deprecation warning
    warnings.warn("`focuses_planewave` is deprecated. " +
                  "It is recommended to using `gaussian` instead .",
                  DeprecationWarning)
    
    
    E = planewave(pos, env_dict, wavelength, 
                  theta=theta, polarization_state=polarization_state, kSign=kSign, 
                  consider_substrate_reflection=consider_substrate_reflection, 
                  returnField=returnField, deprecationwarning=False)
    
    
    xm, ym, zm = np.transpose(pos)
    
    ## beamwaist
    if spotsize == NA == -1:
        raise ValueError("Focused Beam Error! Either spotsize or NA must be given.")
    elif spotsize == -1:
        w0 = 2*wavelength/(NA*np.pi)
    else:
        w0 = spotsize
    
    I_gaussian =  np.exp( -1.0 * (((xm-xSpot)**2 + (ym-ySpot)**2) / (w0**2)))
    
    E = np.prod([E.T,[I_gaussian]], axis=0).T
    
    return np.asfortranarray(E, dtype=DTYPE_C)



def evanescent_planewave(pos, env_dict, wavelength, 
                         theta_inc=0, polar='p', inc_plane='xz', 
                         returnField='E'):
    """oblique incident planewave, only linear polarization
    
    *DEPRECATED* - Use :func:`.plane_wave` instead.
    
    Oblique incidence (from bottom to top) through n1/n2/n3 layer interfaces. 
    May be used to simulate evanescent fields in the total internal 
    reflection configuration. Linear polarization.
    Amplitude = 1 for both, E and B.
    
    Original fortran code by Ch. Girard, python implementation by C. Majorel
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
        
    wavelength : float
        Wavelength in nm
    
    theta_inc : float, default: 0
        incident angle in the XZ plane with respect to e_z, in degrees.
         - 0deg = along Z (from neg to pos Z)
         - 90deg = along X  (from pos to neg X)
         - 180deg = along Z  (from pos to neg Z)
         - 270deg = along X  (from neg to pos X)
    
    polar : str, default: 'p'
        incident linear polarization. Either 's' or 'p'. 
        At 0 / 180 degrees incident angle (normal incindence), 'p' is 
        polarized along x, 's' along y. Then, at 90deg 'p' is along z.
    
    inc_plane : str, default: 'xz'
        plane of incidence, one of ['xz', 'yz']
    
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B' or 'H': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                    list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]
    """
    ## --------- deprecation warning
    warnings.warn("`evanescent_planewave` is deprecated. " +
                  "It is recommended to use `plane_wave` instead .",
                  DeprecationWarning)
    
    
    
    if polar.lower() not in ['s', 'p']:
        raise ValueError("'polar' must be either 's' or 'p'.")
        
    if ('eps1' not in env_dict.keys() or 'eps2' not in env_dict.keys() or
        'eps3' not in env_dict.keys() or 'spacing' not in env_dict.keys()):
        raise ValueError("`env_dict` must contain ['eps1', 'eps2', 'eps3', 'spacing']")
    
    z_d = 0   # position of lower interface
    
    cn1 = env_dict['eps1']**0.5
    cn2 = env_dict['eps2']**0.5
    cn3 = env_dict['eps3']**0.5
    spacing = np.float32(env_dict['spacing'].real)
    
    ## -- convert angles 90 and 270 close to horizontal angles to avoid divergence
    if theta_inc in [-90, 90, -270, 270] and (cn1!=cn2 or cn2!=cn3):
        warnings.warn("Using interface with horizontal angle of incidence!" + 
                      "Please make sure if horizontal incidence makes sense in presence of an interface.")    
    if theta_inc in [-90, 90]:
        theta_inc += 0.05
    if theta_inc in [-270, 270]:
        theta_inc -= 0.05
    
    
    Ex = np.asfortranarray( np.zeros(len(pos)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(pos)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(pos)), dtype=DTYPE_C)
    
    for i,R in enumerate(pos):
        if inc_plane.lower() in ['yz', 'zy']:
            y,x,z = R
        else:
            x,y,z = R
        ex,ey,ez, bx,by,bz = _three_layer_pw(wavelength, theta_inc, polar.lower(), 
                                             z_d, spacing, cn1, cn2, cn3, x, y, z)
        if inc_plane.lower() in ['yz', 'zy']:
            ex,ey,ez = ey,ex,ez
            bx,by,bz = by,bx,bz
        
        if returnField.lower() == 'e':
            Ex[i], Ey[i], Ez[i] = ex, ey, ez
        else:
            Ex[i], Ey[i], Ez[i] = bx, by, bz
        
    Evec = np.transpose([Ex, Ey, Ez])
    return Evec




#************************************************************************
#************************************************************************
# Definition of HG, radially or azimuthally pol. doughnut modes following
#        Novotny & Hecht Principle of Nano-Optics - p62
#
# Implementation by A. Arbouet, CEMES-CNRS, 2021
#
#************************************************************************
#************************************************************************               
def _fw(theta, f0, thetamax):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    theta : angle
    f0: lens filling factor (Novotny p62) f0 = w0/ (f sin theta max) 
    thetamax: max. angle allowed in lens
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    
    fres = np.exp(-(np.sin(theta)/(f0*np.sin(thetamax)))**2)
    return fres                  
                    
# conversion cartersian to cylindrical
def _cart_cyl(x,y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y,x)
    return rho,phi   
    
def _I00(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax)) 
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)*(1+np.cos(theta))*special.j0(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)*(1+np.cos(theta))*special.j0(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 
          
def _I01(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*special.j1(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*special.j1(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 

def _I02(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax))
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)*(1-np.cos(theta))*special.jv(2,k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)*(1-np.cos(theta))*special.jv(2,k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 
          

def _I10(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**3*special.j0(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**3*special.j0(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 


def _I11(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax))     
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*(1+3*np.cos(theta))*special.j1(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*(1+3*np.cos(theta))*special.j1(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 


def _I12(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax))     
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*(1-np.cos(theta))*special.j1(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*(1-np.cos(theta))*special.j1(k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 

def _I13(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax)) 
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**3*special.jv(2,k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**3*special.jv(2,k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 

def _I14(x,y,z,k,n,NA,f,w0):

    """ Novotny & Hecht Principle of Nano-Optics - p62

    Parameters
    ----------
    NA : numerical aperture
    
    Returns
    -------     
    
    Notes
    -----
         add notes
    
    """
    import scipy.integrate as integrate
    import scipy.special as special
    
    thetamax = np.arcsin(NA/n)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    real = integrate.quad(lambda theta: np.real(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*(1-np.cos(theta))*special.jv(3,k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    imag = integrate.quad(lambda theta: np.imag(_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
                         *np.sin(theta)**2*(1-np.cos(theta))*special.jv(3,k*rho*np.sin(theta))
                         *np.exp(1j*k*z*np.cos(theta))), 0, thetamax)
    
    return real[0] + 1j*imag[0] 


def HermiteGauss00_hom(pos, env_dict, wavelength, #theta=None, polarization_state=None, 
             xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
             NA=0.5, f=100, w0=1, returnField='E'):

    """Gaussian TEM mode (0,0)
    
    Focal fields - Expressions from Novotny & Hecht - Principle of Nano-Optics (3.6)
    Generalized to take into account the presence of an interface
    
    Authors: A. Arbouet, Y. Brûlé, G. Colas-des-Francs, 2021
    
    fixed polarization version, homogeneous medium
    
    Parameters
    ----------
    pos : np.array
            list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
                    Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
                    description of environment. Must contain either "eps_env" or ["eps2"].
    
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
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)

    xSpot, ySpot, zSpot : float, float, float, default: 0, 0, 0
                                       focal spot position (in nm)

    kSign : int, default: -1
               sign of wavenumber. 
               +1: propagation from bottom to top (towards increasing z)
               -1: propagation from top to bottom (towards smaller z, default) 

    NA : float, default: 0.5
              lens numerical aperture (NA = n sin thetamax),

    f : float, default: 100
              lens focal distance (mm)

    w0 : float, default: 1 
              beam waist  (mm)

    returnField : str, default: 'E'
              if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                      list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]    

    """
    
    
    if 'eps_env' in env_dict.keys():
        cn1 = cn2 = env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        # spacing = env_dict['spacing']**0.5
#        if cn1 != cn2 or cn2 != cn3:
    if np.imag(cn1) != 0 or np.imag(cn2) != 0 or np.imag(cn3) != 0:
        warnings.warn("Special modes only support real refractive index")
    if cn1 != cn2 or cn2 != cn3:
        warnings.warn("Special modes don't take reflection / transmission at interfaces into account. Results might be inaccurate.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
 
    if kSign == -1 : 
        n = cn2
    else:    
        n = cn1
    k = kSign * n * (2*np.pi / wavelength)
    prefactor = 0.5*1j*k*f*np.sqrt(cn1/cn2)*np.exp(-1j*k*f)

    Ex = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bx = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    By = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bz = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    
    for ipt in range(npts):
        
        x = xm[ipt] - xSpot
        y = ym[ipt] - ySpot
        z = zm[ipt] - zSpot
       
        rho, phi = _cart_cyl(x, y)
           
        I_00 = _I00(x,y,z,k,n,NA,f,w0)
        I_02 = _I02(x,y,z,k,n,NA,f,w0)
        I_01 = _I01(x,y,z,k,n,NA,f,w0)
     
# Novotny (3.66)
# Electric field
        Ex[ipt] = prefactor * (I_00 + I_02*np.cos(2*phi))
        Ey[ipt] = prefactor * I_02 * np.sin(2*phi)
        Ez[ipt] = prefactor * (-2 * 1j * I_01 * np.cos(phi) )    

# Magnetic field

    if returnField == 'B':
        output = np.asfortranarray(np.transpose([Bx, By, Bz]))
    else :
        output = np.asfortranarray(np.transpose([Ex, Ey, Ez]))
    ## --- return as fortran array to avoid copying of arrays in memory
    return output


def HermiteGauss10_hom(pos, env_dict, wavelength, #theta=None, polarization_state=None, 
             xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
             NA=0.5, f=100, w0=1, returnField='E'):

    """Gaussian TEM mode (1,0)
    
    Focal fields - Expressions from Novotny & Hecht - Principle of Nano-Optics (3.6)
    Generalized to take into account the presence of an interface
    
    Authors: A. Arbouet, Y. Brûlé, G. Colas-des-Francs, 2021
    
    fixed polarization version, homogeneous medium
    
    Parameters
    ----------
    pos : np.array
            list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
                    Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
                    description of environment. Must contain either "eps_env" or ["eps2"].
    
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
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)

    xSpot, ySpot, zSpot : float, float, float, default: 0, 0, 0
                                       focal spot position (in nm)

    kSign : int, default: -1
               sign of wavenumber. 
               +1: propagation from bottom to top (towards increasing z)
               -1: propagation from top to bottom (towards smaller z, default) 

      NA : float, default: 0.5
              lens numerical aperture (NA = n sin thetamax),

      f :     float, default: 100
              lens focal distance (mm)

      w0 : float, default: 1 
              beam waist  (mm)

      returnField : str, default: 'E'
              if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                      list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]    

    """
    
    if 'eps_env' in env_dict.keys():
        cn1 = cn2 = env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        # spacing = env_dict['spacing']**0.5
#        if cn1 != cn2 or cn2 != cn3:
    if np.imag(cn1) != 0 or np.imag(cn2) != 0 or np.imag(cn3) != 0:
        warnings.warn("Special modes only support real refractive index")
    if cn1 != cn2 or cn2 != cn3:
        warnings.warn("Special modes don't take reflection / transmission at interfaces into account. Results might be inaccurate.")
    
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)

    if kSign == -1 : 
        n = cn2
    else:    
        n = cn1
    k = kSign * n * (2*np.pi / wavelength)
    prefactor = 0.5*1j*k*f**2*np.sqrt(cn1/cn2)*np.exp(-1j*k*f)/w0

    Ex = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bx = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    By = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bz = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    
    for ipt in range(npts):
        
        x = xm[ipt] - xSpot
        y = ym[ipt] - ySpot
        z = zm[ipt] - zSpot
    
        rho, phi = _cart_cyl(x, y)
           
        I_11 = _I11(x,y,z,k,n,NA,f,w0)
        I_14 = _I14(x,y,z,k,n,NA,f,w0)
        I_12 = _I12(x,y,z,k,n,NA,f,w0)
        I_10 = _I10(x,y,z,k,n,NA,f,w0)
        I_13 = _I13(x,y,z,k,n,NA,f,w0)
     
# Novotny (3.66)
# Electric field
        Ex[ipt] = prefactor * ( 1j*I_11*np.cos(phi) + 1j * I_14*np.cos(3*phi))
        Ey[ipt] = prefactor * (-1j*I_12*np.sin(phi) + 1j * I_14*np.sin(3*phi))
        Ez[ipt] = prefactor * (-2 * I_10 + 2 * I_13 * np.cos(2*phi) )    

# Magnetic field

    if returnField == 'B':
        output = np.asfortranarray(np.transpose([Bx, By, Bz]))
    else :
        output = np.asfortranarray(np.transpose([Ex, Ey, Ez]))
    ## --- return as fortran array to avoid copying of arrays in memory
    return output


def HermiteGauss01_hom(pos, env_dict, wavelength, #theta=None, polarization_state=None, 
             xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
             NA=0.5, f=100, w0=1, returnField='E'):

    """Gaussian TEM mode (0,1)
    
    Focal fields - Expressions from Novotny & Hecht - Principle of Nano-Optics (3.6)
    Generalized to take into account the presence of an interface
    
    Authors: A. Arbouet, Y. Brûlé, G. Colas-des-Francs, 2021
    
    fixed polarization version, homogeneous medium
    
    
    Parameters
    ----------
    pos : np.array
            list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
                    Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
                    description of environment. Must contain either "eps_env" or ["eps2"].
    
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
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)

    xSpot, ySpot, zSpot : float, float, float, default: 0, 0, 0
                                       focal spot position (in nm)

    kSign : int, default: -1
               sign of wavenumber. 
               +1: propagation from bottom to top (towards increasing z)
               -1: propagation from top to bottom (towards smaller z, default) 

      NA : float, default: 0.5
              lens numerical aperture (NA = n sin thetamax),

      f :     float, default: 100
              lens focal distance (mm)

      w0 : float, default: 1 
              beam waist  (mm)

      returnField : str, default: 'E'
              if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                      list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]    

    """
    
    
    if 'eps_env' in env_dict.keys():
        cn1 = cn2 = env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        # spacing = env_dict['spacing']**0.5
#        if cn1 != cn2 or cn2 != cn3:
    if np.imag(cn1) != 0 or np.imag(cn2) != 0 or np.imag(cn3) != 0:
        warnings.warn("Special modes only support real refractive index")
    if cn1 != cn2 or cn2 != cn3:
        warnings.warn("Special modes don't take reflection / transmission at interfaces into account. Results might be inaccurate.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
    if kSign == -1 : 
        n = cn2
    else:    
        n = cn1
    k = kSign * n * (2*np.pi / wavelength)
    prefactor = 0.5*1j*k*f**2*np.sqrt(cn1/cn2)*np.exp(-1j*k*f)/w0

    Ex = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bx = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    By = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bz = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    
    for ipt in range(npts):
        
        x = xm[ipt] - xSpot
        y = ym[ipt] - ySpot
        z = zm[ipt] - zSpot
    
        rho, phi = _cart_cyl(x, y)
           
        I_11 = _I11(x,y,z,k,n,NA,f,w0)
        I_14 = _I14(x,y,z,k,n,NA,f,w0)
        I_12 = _I12(x,y,z,k,n,NA,f,w0)
        I_13 = _I13(x,y,z,k,n,NA,f,w0)
        
# Novotny (3.66)
# Electric field
        Ex[ipt] = prefactor * ( 1j*(I_11 + 2*I_12)*np.sin(phi) + 1j * I_14*np.sin(3*phi))
        Ey[ipt] = prefactor * (-1j*I_12*np.cos(phi) - 1j * I_14*np.cos(3*phi))
        Ez[ipt] = prefactor * ( 2 * I_13 * np.sin(2*phi) )    

# Magnetic field

    if returnField == 'B':
        output = np.asfortranarray(np.transpose([Bx, By, Bz]))
    else :
        output = np.asfortranarray(np.transpose([Ex, Ey, Ez]))
    ## --- return as fortran array to avoid copying of arrays in memory
    return output
                 

def Radial_pol_doughnut_hom(pos, env_dict, wavelength, #theta=None, polarization_state=None, 
                        xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
                        NA=0.5, f=100, w0=1, returnField='E'):

    """radially polarized doughnut mode

    Focal fields - Expressions from Novotny & Hecht - Principle of Nano-Optics (3.6)
    Generalized to take into account the presence of an interface
    
    Authors: A. Arbouet, Y. Brûlé, G. Colas-des-Francs, 2021
    
    fixed polarization version, homogeneous medium
    
    
    Parameters
    ----------
    pos : np.array
            list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
                    Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
                    description of environment. Must contain either "eps_env" or ["eps2"].
    
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
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)

    xSpot, ySpot, zSpot : float, float, float, default: 0, 0, 0
                                       focal spot position (in nm)

    kSign : int, default: -1
               sign of wavenumber. 
               +1: propagation from bottom to top (towards increasing z)
               -1: propagation from top to bottom (towards smaller z, default) 

      NA : float, default: 0.5
              lens numerical aperture (NA = n sin thetamax),

      f :     float, default: 100
              lens focal distance (mm)

      w0 : float, default: 1 
              beam waist  (mm)

      returnField : str, default: 'E'
              if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                      list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]    

    """
    
    
    if 'eps_env' in env_dict.keys():
        cn1 = cn2 = env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        # spacing = env_dict['spacing']**0.5
#        if cn1 != cn2 or cn2 != cn3:
    if np.imag(cn1) != 0 or np.imag(cn2) != 0 or np.imag(cn3) != 0:
        warnings.warn("Special modes only support real refractive index")
    if cn1 != cn2 or cn2 != cn3:
        warnings.warn("Special modes don't take reflection / transmission at interfaces into account. Results might be inaccurate.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
    if kSign == -1 : 
        n = cn2
    else:    
        n = cn1
    k = kSign * n * (2*np.pi / wavelength)
    prefactor = 0.5*1j*k*f**2*np.sqrt(cn1/cn2)*np.exp(-1j*k*f)/w0

    Ex = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bx = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    By = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bz = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    
    for ipt in range(npts):
        
        x = xm[ipt] - xSpot
        y = ym[ipt] - ySpot
        z = zm[ipt] - zSpot
    
        rho, phi = _cart_cyl(x, y)
           
        I_10 = _I10(x,y,z,k,n,NA,f,w0)
        I_11 = _I11(x,y,z,k,n,NA,f,w0)
        I_12 = _I12(x,y,z,k,n,NA,f,w0)
     
# Novotny (3.66)
# Electric field
        Ex[ipt] = prefactor * ( 1j*(I_11 - I_12)*np.cos(phi) )
        Ey[ipt] = prefactor * ( 1j*(I_11 - I_12)*np.sin(phi))
        Ez[ipt] = prefactor * ( -4 * I_10)    

# Magnetic field

    if returnField == 'B':
        output = np.asfortranarray(np.transpose([Bx, By, Bz]))
    else :
        output = np.asfortranarray(np.transpose([Ex, Ey, Ez]))
    ## --- return as fortran array to avoid copying of arrays in memory
    return output    


def Azimuth_pol_doughnut_hom(pos, env_dict, wavelength, #theta=None, polarization_state=None, 
             xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
             NA=0.5, f=100, w0=1, returnField='E'):
    """Azimuthally polarized doughnut mode

    Focal fields - Expressions from Novotny & Hecht - Principle of Nano-Optics (3.6)
    Generalized to take into account the presence of an interface
    
    Authors: A. Arbouet, Y. Brûlé, G. Colas-des-Francs, 2021
    
    fixed polarization version, homogeneous medium
    
    
    Parameters
    ----------
    pos : np.array
            list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
                    Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
                    description of environment. Must contain either "eps_env" or ["eps2"].
    
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
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)

    xSpot, ySpot, zSpot : float, float, float, default: 0, 0, 0
                                       focal spot position (in nm)

    kSign : int, default: -1
               sign of wavenumber. 
               +1: propagation from bottom to top (towards increasing z)
               -1: propagation from top to bottom (towards smaller z, default) 

      NA : float, default: 0.5
              lens numerical aperture (NA = n sin thetamax),

      f :     float, default: 100
              lens focal distance (mm)

      w0 : float, default: 1 
              beam waist  (mm)

      returnField : str, default: 'E'
              if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                      list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]    

    """
    
    
    if 'eps_env' in env_dict.keys():
        cn1 = cn2 = env_dict['eps_env']**0.5
    else:
        cn1 = env_dict['eps1']**0.5
        cn2 = env_dict['eps2']**0.5
        cn3 = env_dict['eps3']**0.5
        # spacing = env_dict['spacing']**0.5
#        if cn1 != cn2 or cn2 != cn3:
    if np.imag(cn1) != 0 or np.imag(cn2) != 0 or np.imag(cn3) != 0:
        warnings.warn("Special modes only support real refractive index")
    if cn1 != cn2 or cn2 != cn3:
        warnings.warn("Special modes don't take reflection / transmission at interfaces into account. Results might be inaccurate.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
    if kSign == -1 : 
        n = cn2
    else:    
        n = cn1
    k = kSign * n * (2*np.pi / wavelength)
    prefactor = 0.5*1j*k*f**2*np.sqrt(cn1/cn2)*np.exp(-1j*k*f)/w0

    Ex = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ey = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Ez = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bx = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    By = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    Bz = np.asfortranarray( np.zeros(len(xm)), dtype=DTYPE_C)
    
    for ipt in range(npts):
        
        x = xm[ipt] - xSpot
        y = ym[ipt] - ySpot
        z = zm[ipt] - zSpot
    
        rho, phi = _cart_cyl(x, y)
           
        # I_10 = _I10(x,y,z,k,n,NA,f,w0)
        I_11 = _I11(x,y,z,k,n,NA,f,w0)
        I_12 = _I12(x,y,z,k,n,NA,f,w0)
     
# Novotny (3.66)
# Electric field
        Ex[ipt] = prefactor * ( 1j*(I_11 + 3 * I_12)*np.sin(phi) )
        Ey[ipt] = prefactor * (-1j*(I_11 + 3 * I_12)*np.cos(phi))
        Ez[ipt] = 0    

# Magnetic field

    if returnField == 'B':
        output = np.asfortranarray(np.transpose([Bx, By, Bz]))
    else :
        output = np.asfortranarray(np.transpose([Ex, Ey, Ez]))
    ## --- return as fortran array to avoid copying of arrays in memory
    return output 






if __name__ == "__main__":
    pass
