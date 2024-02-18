# encoding: utf-8
#
#Copyright (C) 2017-2024, P. R. Wiecha, A. Arbouet, Y. Brûlé
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
Collection of focused beam fields - hermite gauss, radial polarization, azimuthal polarization
"""

from __future__ import print_function
from __future__ import absolute_import

import multiprocessing
import warnings
import cmath
import numpy as np
import numba

import scipy.integrate as integrate
# from scipy import special
#import quadpy

## bessel functions 
# from scipy.special import jv, yv, j0
# from scipy.special import iv, kv



# =============================================================================
#               numba overloads for Bessel functions
#
# adapted for scipy>=1.4 from https://github.com/numba/numba-scipy
#
# =============================================================================
import ctypes
import scipy.special
from numba.extending import get_cython_function_address


## -- in future: add binding to complex hankel
## double complex hankel1(double, double complex)

name_to_numba_signatures = {
    'yv': [(numba.types.float64, numba.types.float64,), (numba.types.long_, numba.types.float64,)],
    'jv': [(numba.types.float64, numba.types.float64,), (numba.types.long_, numba.types.float64,)],
    
    'iv': [(numba.types.float64, numba.types.float64,), (numba.types.long_, numba.types.float64,)],
    'kv': [(numba.types.float64, numba.types.float64,), (numba.types.long_, numba.types.float64,)],
    }

name_and_types_to_pointer = {
    ('yv', numba.types.float64, numba.types.float64): ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(get_cython_function_address('scipy.special.cython_special', '__pyx_fuse_1yv')),
    ('jv', numba.types.float64, numba.types.float64): ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(get_cython_function_address('scipy.special.cython_special', '__pyx_fuse_1jv')),
    
    ('iv', numba.types.float64, numba.types.float64): ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(get_cython_function_address('scipy.special.cython_special', '__pyx_fuse_1iv')),
    ('kv', numba.types.float64, numba.types.float64): ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(get_cython_function_address('scipy.special.cython_special', '__pyx_fuse_1kv')),
    }

def _choose_kernel(name, all_signatures):
    def choice_function(*args):
        for signature in all_signatures:
            if args == signature:
                f = name_and_types_to_pointer[(name, *signature)]
                return lambda *args: f(*args)
    return choice_function

def _add_overloads():
    for name, all_signatures in name_to_numba_signatures.items():
        sc_function = getattr(scipy.special, name)
        numba.extending.overload(sc_function)(
            _choose_kernel(name, all_signatures)
        )

_add_overloads()



# =============================================================================
# helper to determine number of available CPU cores
# =============================================================================
def _get_nr_processes():
    """return available processes
    
    see: 
    https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
    """
    ## preffered method to get available processes (might fail on windows)
    try:
        import os
        return len(os.sched_getaffinity(0))
    except:
        pass
    
    ## if failed, try alternative using psutils
    try:
        import psutil
        return len(psutil.Process().cpu_affinity())
    except:
        pass
    
    ## fall back on multiprocessing value (if psutils not installed)
    import multiprocessing
    return multiprocessing.cpu_count()



#==============================================================================
# globals
#==============================================================================
DTYPE_C = np.complex64

#************************************************************************
#************************************************************************
# Definition of HG, radially and azimuthally pol. doughnut modes following
# Novotny & Hecht Principle of Nano-Optics (p.62) extended to take into
# account an interface (transmission part) by G. Colas des Francs
# Direct calculus through integrals I_ii and K_ii of the azimuthally and 
# radially polarized doghnuts (+ numba for calculation acceleration)
#************************************************************************
#************************************************************************               

@numba.njit                    
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
    
    fres = np.exp(-(np.sin(theta)/f0/np.sin(thetamax))**2)
    return fres                  
                    
# Conversion cartersian to cylindrical
@numba.njit
def _cart_cyl(x,y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y,x)
    return rho, phi   
   
# Wavevectors
@numba.jit(numba.typeof((1.0))(numba.double, numba.double, numba.double), nopython=True)                 
def _krho(n1,k0,theta):
    return n1*k0*np.sin(theta)

@numba.njit                    
def _kz1(n1,k0,theta):
    return n1*k0*np.cos(theta)

@numba.njit                    
def _kz3(n1,n3,k0,theta):
    return cmath.sqrt(n3**2 * k0**2 - _krho(n1,k0,theta)**2)

# Fresnel transmition and reflection coefficients for TE (s) and TM (p) polarization
@numba.njit                    
def _t_TE(n1,n3,k0,theta) :
    return 2.0 * _kz1(n1,k0,theta)/(_kz1(n1,k0,theta) + _kz3(n1,n3,k0,theta))

@numba.njit                    
def _t_TM(n1,n3,k0,theta) :
    return (2.0*n1*n3*_kz1(n1,k0,theta)/(n1**2 * _kz3(n1,n3,k0,theta) + n3**2 * _kz1(n1,k0,theta)))

@numba.njit                    
def _r_TE(n1,n3,k0,theta) :
    return ( _kz1(n1,k0,theta) - _kz3(n1,n3,3,k0,theta))/( _kz1(n1,k0,theta) + _kz3(n1,n3,k0,theta))

@numba.njit                    
def _r_TM(n1,n3,k0,theta) :
    return (n3**2 * _kz1(n1,k0,theta) - n1**2*_kz3(n1,k0,theta)) / (n3**2 * _kz1(n1,k0,theta) + n1**2 * _kz3(n1,n3,k0,theta))

# cos and sin theta in the outgoing media
@numba.njit
def _sintheta3(n1,n3,theta) :
    return n1/n3 * np.sin(theta)

@numba.njit
def _costheta3(n1,n3,theta) :
    ct3 = cmath.sqrt(1. - _sintheta3(n1, n3, theta)**2)
    ct3 *= np.sign(np.sign(ct3.imag) + 0.5)  # if imag<0: multiply by -1
    
    return ct3

"""
In all the following integrals (IXX_t and KXX_t) :
    Parameters
    ----------
    x,y,z : position
    k0: wavector in vaacum
    kSign: beam z-propagation direction
           -1: top to Bottom, 1 Bottom to top
    NA : numerical aperture
    n1: incident medium index
    n3: outgoing medium index 
    f : lens focal distance (mm)
    w0 : beam waist  (mm)
"""
                                     
# Electric part
@numba.njit
def _I00_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):    
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))
    rho, phi = _cart_cyl(x,y)
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)*(_t_TE(n1,n3,k0,theta) + _t_TM(n1,n3,k0,theta) * _costheta3(n1,n3,theta) )
              *scipy.special.jv(0.,kSign*_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I00_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I00_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I01_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)*_t_TM(n1,n3,k0,theta)*_sintheta3(n1,n3,theta)
              *scipy.special.jv(1.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I01_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I01_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I02_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)*(_t_TE(n1,n3,k0,theta) - _t_TM(n1,n3,k0,theta) * _costheta3(n1,n3,theta) )
              *scipy.special.jv(2.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z)) 
    return result

def _I02_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I02_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I10_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*_t_TM(n1,n3,k0,theta)*_sintheta3(n1,n3,theta)
              *scipy.special.jv(0.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I10_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I11_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*(_t_TE(n1,n3,k0,theta) + 3*_t_TM(n1,n3,k0,theta)*_costheta3(n1,n3,theta))
              *scipy.special.jv(1.,1.*_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I11_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I12_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*(_t_TE(n1,n3,k0,theta) - _t_TM(n1,n3,k0,theta)*_costheta3(n1,n3,theta))
              *scipy.special.jv(1.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I12_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I13_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*_t_TM(n1,n3,k0,theta)*_sintheta3(n1,n3,theta)
              *scipy.special.jv(2.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I13_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I13_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _I14_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*(_t_TE(n1,n3,k0,theta) - _t_TM(n1,n3,k0,theta)*_costheta3(n1,n3,theta))
              *scipy.special.jv(3.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _I14_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _I14_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

# Magnetic part
@numba.njit
def _K00_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):        
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))
    rho, phi = _cart_cyl(x,y)
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)*(_t_TM(n1,n3,k0,theta) + _t_TE(n1,n3,k0,theta) * _costheta3(n1,n3,theta) )
              *scipy.special.jv(0.,kSign*_krho(n1,k0,theta)*rho)
              * np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))    
    return result

def _K00_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K00_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K01_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)*_t_TE(n1,n3,k0,theta)*_sintheta3(n1,n3,theta)
              *scipy.special.jv(1.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))   
    return result

def _K01_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K01_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K02_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
           *np.sin(theta)*(_t_TM(n1,n3,k0,theta) - _t_TE(n1,n3,k0,theta) * _costheta3(n1,n3,theta) )
           *scipy.special.jv(2.,_krho(n1,k0,theta)*rho)
           *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _K02_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K02_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K10_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*_t_TE(n1,n3,k0,theta)*_sintheta3(n1,n3,theta)
              *scipy.special.jv(0.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _K10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K10_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K11_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*(3.*_t_TE(n1,n3,k0,theta)*_costheta3(n1,n3,theta) + _t_TM(n1,n3,k0,theta))
              *scipy.special.jv(1.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))    
    return result

def _K11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K11_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K12_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (-1.*_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*( _t_TE(n1,n3,k0,theta)*_costheta3(n1,n3,theta) - _t_TM(n1,n3,k0,theta))
              *scipy.special.jv(1., _krho(n1,k0,theta)*rho )
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))    
    return result

def _K12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K12_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K13_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*_t_TE(n1,n3,k0,theta)*_sintheta3(n1,n3,theta)
              *scipy.special.jv(2.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))
    return result

def _K13_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K13_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

@numba.njit
def _K14_t_integral(theta,x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    f0 = w0/(f*np.sin(thetamax))    
    rho, phi = _cart_cyl(x,y)    
    result = (-1.*_fw(theta,f0,thetamax)*np.sqrt(np.cos(theta))
              *np.sin(theta)**2*(_t_TE(n1,n3,k0,theta)*_costheta3(n1,n3,theta) - _t_TM(n1,n3,k0,theta))
              *scipy.special.jv(3.,_krho(n1,k0,theta)*rho)
              *np.exp(1j*n3*k0*_costheta3(n1,n3,theta)*kSign*z))   
    return result

def _K14_t(x,y,z,k0,kSign,n1,n3,NA,f,w0):
    thetamax = np.arcsin(NA/n1)
    int_func = lambda  theta: _K14_t_integral(theta, x,y,z,k0,kSign,n1,n3,NA,f,w0)
    integr, err = integrate.quad_vec(int_func, 0, thetamax, quadrature='gk15')
    return integr

def _func_calc_E_HG_00_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_state = args_list
    
    phi = np.arctan2(y,x)
 
    I_00  = _I00_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_02  = _I02_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_01  = _I01_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
 
    # Electric field
    # x-polarization
    Exx = kSign * (I_00 + I_02*np.cos(2*phi))
    Eyx = kSign * I_02 * np.sin(2*phi)
    Ezx = (-2 * 1j * I_01 * np.cos(phi) )    
    # y-polarization
    Exy = kSign * I_02 * np.sin(2*phi)
    Eyy = kSign * (I_00 - I_02*np.cos(2*phi))
    Ezy = (-2 * 1j * I_01 * np.sin(phi))
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # adding the polarization component
    Ex = (E0x * Exx  + E0y * Exy)
    Ey = (E0x * Eyx  + E0y * Eyy)
    Ez = (E0x * Ezx  + E0y * Ezy)
         
    # adding an absolute phase
    abs_phase = np.exp(1j * Aphi)
    Ex *= abs_phase
    Ey *= np.exp(1j * Dphi) * abs_phase    
      
    return prefactor * np.array([Ex, Ey, Ez])

def _func_calc_H_HG_00_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_state,Z0 = args_list
    
    phi = np.arctan2(y,x)
              
    K_00 = _K00_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_02 = _K02_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_01 = _K01_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    
    # Magnetic field
    # x-polarization
    Bxx = kSign * K_02 * np.sin(2*phi)
    Byx = kSign * (K_00 - K_02*np.cos(2*phi))
    Bzx = (-2 * 1j * K_01 * np.sin(phi))
    
    # y-polarization
    Bxy = kSign * (K_00 + K_02*np.cos(2*phi))
    Byy = kSign * K_02 * np.sin(2*phi)
    Bzy = (-2 * 1j * K_01 * np.cos(phi))        
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # adding the polarization component
    Bx = (E0x * Bxx  + E0y * Bxy)
    By = (E0x * Byx  + E0y * Byy)
    Bz = (E0x * Bzx  + E0y * Bzy)
         
    # adding an absolute phase
    abs_phase = np.exp(1j * Aphi)
    Bx *= abs_phase
    By *= np.exp(1j * Dphi) * abs_phase
    
    return prefactor * n3/Z0 * np.array([Bx, By, Bz])

def HermiteGauss00(
        pos, env_dict, wavelength, 
        theta=0, polarization_state=None,
        xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
        NA=0.5, f=100, w0=1, phase=0.0, normalize=False, returnField='E', N_cpu=-1):

    """Hermite Gaussian mode (0,0)
    
    after Novotny & Hecht p62 - Eq. (3.66)
    extended to transmission through an interface (G. Colas des Francs)
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
    
    wavelength : float
          Wavelength in nm
      
    theta : float, optional
        linear polarization angle in degrees, 0deg = 0X direction.
        either 'theta' or 'polarization_state' must be given.
        The default is 0 (x polarization).
    
    polarization_state : 4-tuple of float, optional
        either 'theta' or 'polarization_state' must be given.
        polarization state with field amplitudes and phases, tuple of 4 float:
        (E0x, E0y, Dphi, Aphi): E0X amplitde, E0Y amplitde, phase difference 
        between X and Y components (in rad), absolute phase of plane wave (in rad).
        The field is then calculated as E = (E0x, E0y*exp(i*Dphi*z), 0)*exp(i*Aphi*z).
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)
        The default is `None`.
    
    xSpot, ySpot, zSpot : float, optional
        position of beam focus in nm. The default is 0,0,0
        
    kSign : float, optional
        Direction of Beam. -1: top to Bottom, 1 Bottom to top. 
        The default is -1
              
    NA : float, optional
        lens numerical aperture. The default is 0.5.
    
    f : float, optional
        lens focal distance (in mm). The default is 100.
    
    w0 : float, optional
        beam waist before focalisation (in mm). The default is 1.
    
    phase : float, optional
        additional phase (degrees). The default is 0.
    
    normalize : bool, optional
        Normalize field amplitude at focus. If False, field is 
        normalized *before* the focus. The default is False.
                     
    returnField  : str, optional
        'B' or 'E'. The default is 'E'.
    
    N_cpu : int, optional
        numbers of CPUs to use for beam evaluation. The default is -1 (all CPUs).
    """
    if N_cpu == -1:
        N_cpu = _get_nr_processes()
    
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
    if cn2 != cn3:
        warnings.warn("Special modes only support one interface. Using ref.indices of medium 1 and 3, but results may be incorrect.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
 
    if kSign == -1 : 
        n1 = cn3
        n3 = cn1
    else:    
        n1 = cn1
        n3 = cn3
        
    if (theta is None and polarization_state is None) or (theta is not None and polarization_state is not None):
        raise ValueError("exactly one argument of 'theta' and 'polarization_state' must be given.")
    if theta is not None:
        polarization_state = (1.0 * np.cos(theta * np.pi/180.), 
                              1.0 * np.sin(theta * np.pi/180.), 
                              0, 0)
    #Vacuum impedence
    eps0 = 8.85418782e-12
    mu0  = 4e-7*np.pi
    Z0 = np.sqrt(mu0/eps0)    

    k = kSign * n1 * (2*np.pi / wavelength)
    k0 = 2*np.pi / wavelength
    prefactor = 0.5*1j*k*f*np.exp(-1j*k*f)
    
    #adding an additional phase to the beam, in degrees
    prefactor *= np.exp(1j*phase*np.pi/180.)
    
    if returnField.lower() == 'e':
        argslist = []
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
            
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_state])
     
        with multiprocessing.Pool(N_cpu) as p:
            E_list = p.map(_func_calc_E_HG_00_t, argslist)
        output = np.array(E_list, dtype=DTYPE_C)
    else:
        argslist = []
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot

            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_state, Z0])
            
        with multiprocessing.Pool(N_cpu) as p:
            B_list = p.map(_func_calc_H_HG_00_t, argslist)
        output = np.array(B_list, dtype=DTYPE_C)


    if normalize:
        return output / np.linalg.norm(output, axis=1).max()
    else:
        return output

def _func_calc_E_HG_10_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_state = args_list
    
    phi = np.arctan2(y,x)
 
    I_10 = _I10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_11 = _I11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_12 = _I12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_13 = _I13_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_14 = _I14_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
 
    # Electric field
    # x-polarization
    Exx = kSign * 1j * ( I_11 * np.cos(phi) + I_14 * np.cos(3.*phi) )
    Eyx = kSign * 1j * ( -1.* I_12 * np.sin(phi) + I_14 * np.sin(3.*phi) )
    Ezx = 2.         * (-1. * I_10 + I_13 * np.cos(2.*phi) )    
    # y-polarization
    Exy = kSign * 1j * (-1. * I_12 * np.sin(phi) + I_14 * np.sin(3.*phi) )
    Eyy = kSign * 1j * ( (I_11 + 2.*I_12) * np.cos(phi) - I_14 * np.cos(3.*phi) )
    Ezy = 2.         * I_13 * np.sin(2.*phi) 
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # adding the polarization component
    Ex = (E0x * Exx  + E0y * Exy)
    Ey = (E0x * Eyx  + E0y * Eyy)
    Ez = (E0x * Ezx  + E0y * Ezy)
         
    # adding an absolute phase
    abs_phase = np.exp(1j * Aphi)
    Ex *= abs_phase
    Ey *= np.exp(1j * Dphi) * abs_phase    
      
    return prefactor * np.array([Ex, Ey, Ez])

def _func_calc_H_HG_10_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_state,Z0 = args_list
    
    phi = np.arctan2(y,x)
    
    K_10 = _K10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_11 = _K11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_12 = _K12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_13 = _K13_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_14 = _K14_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
            
    # Magnetic field
    # x-polarization
    Bxx = kSign * 1j * ( -1.* K_12 * np.sin(phi) + K_14 * np.sin(3.*phi) )
    Byx = kSign * 1j * ( (K_11 + 2.*K_12)*np.cos(phi) - K_14 * np.cos(3.*phi) )
    Bzx = 2.         * K_13  * np.sin(2.* phi)
         
    # y-polarization
    Bxy = kSign * 1j * ( -1.* K_11 * np.cos(phi) - K_14 * np.cos(3.*phi) )
    Byy = kSign * 1j * ( K_12 * np.sin(phi) - K_14 * np.sin(3.*phi) )
    Bzy = 2.         * ( K_10 - K_13 * np.cos(2.*phi) )
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # adding the polarization component
    Bx = (E0x * Bxx  + E0y * Bxy)
    By = (E0x * Byx  + E0y * Byy)
    Bz = (E0x * Bzx  + E0y * Bzy)
         
    # adding an absolute phase
    abs_phase = np.exp(1j * Aphi)
    Bx *= abs_phase
    By *= np.exp(1j * Dphi) * abs_phase
    
    return prefactor * n3/Z0 * np.array([Bx, By, Bz])

def HermiteGauss10(
        pos, env_dict, wavelength, 
        theta=0, polarization_state=None,
        xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
        NA=0.5, f=100, w0=1, phase=0.0, normalize=False, returnField='E', N_cpu=-1):

    """Hermite Gaussian mode (1,0)
    
    after Novotny & Hecht p62 - Eq. (3.66)
    extended to transmission through an interface (G. Colas des Francs)
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
    
    wavelength : float
          Wavelength in nm
      
    theta : float, optional
        linear polarization angle in degrees, 0deg = 0X direction.
        either 'theta' or 'polarization_state' must be given.
        The default is 0 (x polarization).
    
    polarization_state : 4-tuple of float, optional
        either 'theta' or 'polarization_state' must be given.
        polarization state with field amplitudes and phases, tuple of 4 float:
        (E0x, E0y, Dphi, Aphi): E0X amplitde, E0Y amplitde, phase difference 
        between X and Y components (in rad), absolute phase of plane wave (in rad).
        The field is then calculated as E = (E0x, E0y*exp(i*Dphi*z), 0)*exp(i*Aphi*z).
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)
        The default is `None`.
    
    xSpot, ySpot, zSpot : float, optional
        position of beam focus in nm. The default is 0,0,0
        
    kSign : float, optional
        Direction of Beam. -1: top to Bottom, 1 Bottom to top. 
        The default is -1
              
    NA : float, optional
        lens numerical aperture. The default is 0.5.
    
    f : float, optional
        lens focal distance (in mm). The default is 100.
    
    w0 : float, optional
        beam waist before focalisation (in mm). The default is 1.
    
    phase : float, optional
        additional phase (degrees). The default is 0.
    
    normalize : bool, optional
        Normalize field amplitude at focus. If False, field is 
        normalized *before* the focus. The default is False.
                                  
    returnField  : str, optional
        'B' or 'E'. The default is 'E'.
    
    N_cpu : int, optional
        numbers of CPUs to use for beam evaluation. The default is -1 (all CPUs).
    """
    if N_cpu == -1:
        N_cpu = _get_nr_processes()
    
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
    if cn2 != cn3:
        warnings.warn("Special modes only support one interface. Using ref.indices of medium 1 and 3, but results may be incorrect.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
 
    if kSign == -1 : 
        n1 = cn3
        n3 = cn1
    else:    
        n1 = cn1
        n3 = cn3
        
    if (theta is None and polarization_state is None) or (theta is not None and polarization_state is not None):
        raise ValueError("exactly one argument of 'theta' and 'polarization_state' must be given.")
    if theta is not None:
        polarization_state = (1.0 * np.cos(theta * np.pi/180.), 
                              1.0 * np.sin(theta * np.pi/180.), 
                              0, 0)
    #Vacuum impedence
    eps0 = 8.85418782e-12
    mu0  = 4e-7*np.pi
    Z0 = np.sqrt(mu0/eps0)    

    k = kSign * n1 * (2*np.pi / wavelength)
    k0 = 2*np.pi / wavelength
    prefactor = 0.5/w0*1j*k*f**2*np.exp(-1j*k*f)
    
    #adding a additional phase to the beam, in degrees
    prefactor *= np.exp(1j*phase*np.pi/180.)
    
    if returnField.lower() == 'e':
        argslist = []
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot

            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_state])
              
        with multiprocessing.Pool(N_cpu) as p:
            E_list = p.map(_func_calc_E_HG_10_t, argslist)
        output = np.array(E_list, dtype=DTYPE_C)

    else :
        argslist = []
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
         
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_state, Z0])
            
        with multiprocessing.Pool(N_cpu) as p:
            B_list = p.map(_func_calc_H_HG_10_t, argslist)
        output = np.array(B_list, dtype=DTYPE_C)

    if normalize:
        return output / np.linalg.norm(output, axis=1).max()
    else:
        return output

def _func_calc_E_HG_01_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_state = args_list
    
    phi = np.arctan2(y,x)
 
    I_10 = _I10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_11 = _I11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_12 = _I12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_13 = _I13_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_14 = _I14_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
 
    # Electric field
    # x-polarization
    Exx = kSign * 1j * ( (I_11 + 2.*I_12) * np.sin(phi) + I_14 * np.sin(3.*phi) )
    Eyx = kSign *-1j * ( I_12 * np.cos(phi) + I_14 * np.cos(3.*phi) )
    Ezx = 2.         *   I_13 * np.sin(2.*phi)    
    # y-polarization
    Exy = kSign *-1j * ( I_12 * np.cos(phi) + I_14 * np.cos(3.*phi) )
    Eyy = kSign * 1j * ( I_11 * np.sin(phi) - I_14 * np.sin(3.*phi) )
    Ezy = -2.        * (I_10 + I_13 * np.cos(2.*phi) )
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # adding the polarization component
    Ex = (E0x * Exx  + E0y * Exy)
    Ey = (E0x * Eyx  + E0y * Eyy)
    Ez = (E0x * Ezx  + E0y * Ezy)
         
    # adding an absolute phase
    abs_phase = np.exp(1j * Aphi)
    Ex *= abs_phase
    Ey *= np.exp(1j * Dphi) * abs_phase   
    
    return prefactor * np.array([Ex, Ey, Ez])

def _func_calc_H_HG_01_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_state,Z0 = args_list
    phi = np.arctan2(y,x)
    
    K_10 = _K10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_11 = _K11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_12 = _K12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_13 = _K13_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_14 = _K14_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
            
    # Magnetic field
    # x-polarization
    Bxx = kSign * 1j * (-K_12 * np.cos(phi) - K_14 * np.cos(3.*phi) )
    Byx = kSign * 1j * ( K_11 * np.sin(phi) - K_14 * np.sin(3.*phi) )
    Bzx = 2.         * (-K_10 - K_13  * np.cos(2.* phi) ) 
         
    # y-polarization
    Bxy = kSign * 1j * (-(K_11 + 2.*K_12) * np.sin(phi) - K_14 * np.sin(3.*phi) )
    Byy = kSign * 1j * ( K_12 * np.cos(phi) + K_14 * np.cos(3.*phi) )
    Bzy = -2.         *  K_13 * np.sin(2.*phi)
    
    ## amplitude and polarization
    E0x = polarization_state[0]
    E0y = polarization_state[1]
    Dphi = polarization_state[2]
    Aphi = polarization_state[3]
    
    # adding the polarization component
    Bx = (E0x * Bxx  + E0y * Bxy)
    By = (E0x * Byx  + E0y * Byy)
    Bz = (E0x * Bzx  + E0y * Bzy)
         
    # adding an absolute phase
    abs_phase = np.exp(1j * Aphi)
    Bx *= abs_phase
    By *= np.exp(1j * Dphi) * abs_phase
    
    return prefactor * n3/Z0 * np.array([Bx, By, Bz])

def HermiteGauss01(
        pos, env_dict, wavelength, 
        theta=0, polarization_state=None,
        xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
        NA=0.5, f=100, w0=1, phase=0.0, normalize=False, returnField='E', N_cpu=-1):
    
    """Gaussian mode (0,1)
    
    after Novotny & Hecht p62 - Eq. (3.66)
    extended to transmission through an interface (G. Colas des Francs)
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
    
    wavelength : float
          Wavelength in nm
      
    theta : float, optional
        linear polarization angle in degrees, 0deg = 0X direction.
        either 'theta' or 'polarization_state' must be given.
        The default is 0 (x polarization).
    
    polarization_state : 4-tuple of float, optional
        either 'theta' or 'polarization_state' must be given.
        polarization state with field amplitudes and phases, tuple of 4 float:
        (E0x, E0y, Dphi, Aphi): E0X amplitde, E0Y amplitde, phase difference 
        between X and Y components (in rad), absolute phase of plane wave (in rad).
        The field is then calculated as E = (E0x, E0y*exp(i*Dphi*z), 0)*exp(i*Aphi*z).
            Dphi : 
                - positive: left hand rotating polarization
                - negative: right hand rotating polarization 
                - example: left circular pol. with (E0x=1, E0y=1, Dphi=np.pi/2., phi=0)
        The default is `None`.
    
    xSpot, ySpot, zSpot : float, optional
        position of beam focus in nm. The default is 0,0,0
        
    kSign : float, optional
        Direction of Beam. -1: top to Bottom, 1 Bottom to top. 
        The default is -1
              
    NA : float, optional
        lens numerical aperture. The default is 0.5.
    
    f : float, optional
        lens focal distance (in mm). The default is 100.
    
    w0 : float, optional
        beam waist before focalisation (in mm). The default is 1.
    
    phase : float, optional
        additional phase (degrees). The default is 0.
    
    normalize : bool, optional
        Normalize field amplitude at focus. If False, field is 
        normalized *before* the focus. The default is False.
    
    returnField  : str, optional
        'B' or 'E'. The default is 'E'.     
    
    N_cpu : int, optional
        numbers of CPUs to use for beam evaluation. The default is -1 (all CPUs).
    """
    if N_cpu == -1:
        N_cpu = _get_nr_processes()
  
    
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
    if cn2 != cn3:
        warnings.warn("Special modes only support one interface. Using ref.indices of medium 1 and 3, but results may be incorrect.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
 
    if kSign == -1 : 
        n1 = cn3
        n3 = cn1
    else:    
        n1 = cn1
        n3 = cn3
        
    if (theta is None and polarization_state is None) or (theta is not None and polarization_state is not None):
        raise ValueError("exactly one argument of 'theta' and 'polarization_state' must be given.")
    if theta is not None:
        polarization_state = (1.0 * np.cos(theta * np.pi/180.), 
                              1.0 * np.sin(theta * np.pi/180.), 
                              0, 0)
    
    #Vacuum impedence
    eps0 = 8.85418782e-12
    mu0  = 4e-7*np.pi
    Z0 = np.sqrt(mu0/eps0)    

    k = kSign * n1 * (2*np.pi / wavelength)
    k0 = 2*np.pi / wavelength
    prefactor = 0.5/w0*1j*k*f**2*np.exp(-1j*k*f)
    
    #adding a additional phase to the beam, in degrees
    prefactor *= np.exp(1j*phase*np.pi/180.)
    
    if returnField.lower() == 'e':
        argslist = []        
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
    
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor,polarization_state]) 
                        
        with multiprocessing.Pool(N_cpu) as p:
            E_list = p.map(_func_calc_E_HG_01_t, argslist)
        output = np.array(E_list, dtype=DTYPE_C)
            
    else :
        argslist = []
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
    
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor,polarization_state, Z0])
            
        with multiprocessing.Pool(N_cpu) as p:
            B_list = p.map(_func_calc_H_HG_01_t, argslist)
        output = np.array(B_list, dtype=DTYPE_C)


    if normalize:
        return output / np.linalg.norm(output, axis=1).max()
    else:
        return output


def _func_calc_E_doughnut_rad_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_direction = args_list
    
    phi = np.arctan2(y,x)
 
    I_10 = _I10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_11 = _I11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_12 = _I12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
 
    # Electric field
    Exi = kSign * 1j * ( (I_11 - I_12) * np.cos(phi) )
    Eyi = kSign * 1j * ( (I_11 - I_12) * np.sin(phi) )
    Ezi = -4.         *   I_10    
    
    return prefactor * polarization_direction * np.array([Exi, Eyi, Ezi])

def _func_calc_H_doughnut_rad_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_direction,Z0 = args_list
    
    phi = np.arctan2(y,x)
    
    K_11 = _K11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_12 = _K12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
            
    # Magnetic field
    Bxi = kSign * -1j * ( (K_11 + 3*K_12)*np.sin(phi) )
    Byi = kSign *  1j * ( (K_11 + 3*K_12)*np.cos(phi) )
    Bzi = 0.         

    return prefactor * n3/Z0 * polarization_direction * np.array([Bxi, Byi, Bzi])

def Radial_pol_doughnut(
        pos, env_dict, wavelength, 
        polarization_direction = 1.0, 
        xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
        NA=0.5, f=100, w0=1, phase=0.0, normalize=False, returnField='E', N_cpu=-1):
    """Radially polarized doughnut mode focused beam
    
    after Novotny & Hecht p67 - Eq. (3.70)
    extended to transmission through an interface (G. Colas des Francs)
    
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
    
    wavelength : float
          Wavelength in nm
    
    polarization_direction : float, optional
        Either 1 or -1. Direction of the azimuthal polarization. 
        Equivalent to a phase of pi. The default is 1.
    
    xSpot, ySpot, zSpot : float, optional
        position of beam focus in nm. The default is 0,0,0
        
    kSign : float, optional
        Direction of Beam. -1: top to Bottom, 1 Bottom to top. 
        The default is -1
              
    NA : float, optional
        lens numerical aperture. The default is 0.5.
    
    f : float, optional
        lens focal distance (in mm). The default is 100.
    
    w0 : float, optional
        beam waist before focalisation (in mm). The default is 1.
    
    phase : float, optional
        additional phase (degrees). The default is 0.
                     
    returnField  : str, optional
        'B' or 'E'. The default is 'E'.    
    
    normalize : bool, optional
        Normalize field amplitude at focus. If False, field is 
        normalized *before* the focus. The default is False.
    
    N_cpu : int, optional
        numbers of CPUs to use for beam evaluation. The default is -1 (all CPUs).
    """
    if N_cpu == -1:
        N_cpu = _get_nr_processes()
    
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
    if cn2 != cn3:
        warnings.warn("Special modes only support one interface. Using ref.indices of medium 1 and 3, but results may be incorrect.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
 
    if kSign == -1 : 
        n1 = cn3
        n3 = cn1
    else:    
        n1 = cn1
        n3 = cn3
        
    #Vacuum impedence
    eps0 = 8.85418782e-12
    mu0  = 4e-7*np.pi
    Z0 = np.sqrt(mu0/eps0)    

    k = kSign * n1 * (2*np.pi / wavelength)
    k0 = 2*np.pi / wavelength
    prefactor = 0.5/w0*1j*k*f**2*np.exp(-1j*k*f)
    
    #adding a additional phase to the beam, in degrees
    prefactor *= np.exp(1j*phase*np.pi/180.)
    
    if returnField.lower() == 'e':
        argslist = []
        for ipt in range(npts):
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_direction])
        
        with multiprocessing.Pool(N_cpu) as p:
            E_list = p.map(_func_calc_E_doughnut_rad_t, argslist)
        output = np.array(E_list, dtype=DTYPE_C)
    else :
        argslist = []
        for ipt in range(npts):
           
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_direction, Z0])
            
        with multiprocessing.Pool(N_cpu) as p:
            B_list = p.map(_func_calc_H_doughnut_rad_t, argslist)
        output = np.array(B_list, dtype=DTYPE_C)
        
    if normalize:
        return output / np.linalg.norm(output, axis=1).max()
    else:
        return output

def _func_calc_E_doughnut_azim_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_direction = args_list
    
    phi = np.arctan2(y,x)
 
    I_11 = _I11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    I_12 = _I12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
 
    # Electric field
    Exi = kSign * -1j * ( (I_11 + 3*I_12) * np.sin(phi) )
    Eyi = kSign *  1j * ( (I_11 + 3*I_12) * np.cos(phi) )
    Ezi= 0.
        
    return prefactor * polarization_direction * np.array([Exi, Eyi, Ezi])

def _func_calc_H_doughnut_azim_t(args_list):
    x,y,z, k0,kSign,n1,n3,NA,f,w0,prefactor,polarization_direction,Z0 = args_list
    
    phi = np.arctan2(y,x)
    
    K_10 = _K10_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_11 = _K11_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
    K_12 = _K12_t(x,y,z,k0,kSign,n1,n3,NA,f,w0)
            
    # Magnetic field
    Bxi = kSign * 1j * ( (K_12 - K_11) * np.cos(phi) )
    Byi = kSign * 1j * ( (K_12 - K_11) * np.sin(phi) )
    Bzi = kSign *  4 *    K_10    

    return prefactor * polarization_direction * n3/Z0 * np.array([Bxi, Byi, Bzi])


def Azimuth_pol_doughnut(
        pos, env_dict, wavelength, polarization_direction=1.0,
        xSpot=0.0, ySpot=0.0, zSpot=0.0, kSign=-1.0,
        NA=0.5, f=100, w0=1, phase=0.0, normalize=False, returnField='E', N_cpu=-1):

    """Azimuthally polarized doughnut
    
    After Novotny & Hecht p.67 - Eq. (3.70)
    Extended to include transmission through an interface (G. Colas des Francs)
    
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at:
            [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain ['eps1', 'eps2', 'eps3', 'spacing'].
    
    wavelength : float
          Wavelength in nm
    
    polarization_direction : float, optional
        Either 1 or -1. Direction of the azimuthal polarization. 
        Equivalent to a phase of pi. The default is 1.
    
    xSpot, ySpot, zSpot : float, optional
        position of beam focus in nm. The default is 0,0,0
        
    kSign : float, optional
        Direction of Beam. -1: top to Bottom, 1 Bottom to top. 
        The default is -1
              
    NA : float, optional
        lens numerical aperture. The default is 0.5.
    
    f : float, optional
        lens focal distance (in mm). The default is 100.
    
    w0 : float, optional
        beam waist before focalisation (in mm). The default is 1.
    
    phase : float, optional
        additional phase (degrees). The default is 0.
    
    normalize : bool, optional
        Normalize field amplitude at focus. If False, field is 
        normalized *before* the focus. The default is False.
    
    returnField  : str, optional
        'B' or 'E'. The default is 'E'.
        
    N_cpu : int, optional
        numbers of CPUs to use for beam evaluation. The default is -1 (all CPUs).
    """
    if N_cpu == -1:
        N_cpu = _get_nr_processes()

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
    if cn2 != cn3:
        warnings.warn("Special modes only support one interface. Using ref.indices of medium 1 and 3, but results may be incorrect.")
    
    cn1 = np.real(cn1)
    cn2 = np.real(cn2)
    cn3 = np.real(cn3)
        
    f *= 1E6  # conversion mm > nm
    w0 *= 1E6  # conversion mm > nm
        
    xm, ym, zm = np.transpose(pos)    
    npts = len(xm)
 
    if kSign == -1 : 
        n1 = cn3
        n3 = cn1
    else:    
        n1 = cn1
        n3 = cn3
        
    #Vacuum impedence
    eps0 = 8.85418782e-12
    mu0  = 4e-7*np.pi
    Z0 = np.sqrt(mu0/eps0)    

    k = kSign * n1 * (2*np.pi / wavelength)
    k0 = 2*np.pi / wavelength
    prefactor = 0.5/w0*1j*k*f**2*np.exp(-1j*k*f)
    
    #adding a additional phase to the beam, in degrees
    prefactor *= np.exp(1j*phase*np.pi/180.)
    
    if returnField.lower() == 'e':
        argslist = []
        for ipt in range(npts):
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_direction])
        with multiprocessing.Pool(N_cpu) as p:
            E_list = p.map(_func_calc_E_doughnut_azim_t, argslist)    
        output = np.array(E_list, dtype=DTYPE_C)
    else :
        argslist = []
        for ipt in range(npts):   
            x = xm[ipt] - xSpot
            y = ym[ipt] - ySpot
            z = zm[ipt] - zSpot
            argslist.append([x, y, z, k0, kSign, n1, n3, NA, f, w0,
                             prefactor, polarization_direction, Z0])
            
        with multiprocessing.Pool(N_cpu) as p:
            B_list = p.map(_func_calc_H_doughnut_azim_t, argslist)
        output = np.array(B_list, dtype=DTYPE_C)

     
    if normalize:
        return output / np.linalg.norm(output, axis=1).max()
    else:
        return output


if __name__ == "__main__":
    pass