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
fast electron fields

authors: A. Arbouet, P. Wiecha
"""

from __future__ import print_function
from __future__ import absolute_import

import warnings

import numpy as np



#==============================================================================
# globals
#==============================================================================
DTYPE_C = np.complex64




        

#==============================================================================
# field generator functions
#==============================================================================
def fast_electron(pos, env_dict, wavelength, 
                  electron_kinetic_energy, x0, y0, 
                  kSign = -1, avoid_div_lim_distance=10.0,
                  returnField='E'):
    
    """Electric field created by a fast electron moving along (OZ) 
    
    The electron beam crosses the (OXY) plane in (x0, y0)
       
    Parameters
    ----------
    pos : np.array
        list of 3-tuple coordinates to evaluate field at: [[x1,y1,z1], [x2,y2,z2], ... ]
    
    env_dict : dict
        Must be compatible with `sim.dyads.getConfigDictG` typed numba dict.
        description of environment. Must contain either "eps_env" or ["eps1", "eps2"].
    
    wavelength : float
        Wavelength in nm
    
    electron_kinetic_energy : float
        electron kinetic energy (keV)
    
    x0, y0 : float
        position of the electron beam (nm)
    
    kSign : int, default: -1
        sign of wavenumber. 
        +1: electron propagation from bottom to top (towards increasing z)
        -1: electron propagation from top to bottom (towards smaller z, default)
        either kSign or k0 must be given.
    
    avoid_div_lim_distance : float, default: 10.0
        set a min. distance (in nm) between the location where the E-field 
        is computed and the electron trajectory to avoid divergence  
    
    returnField : str, default: 'E'
        if 'E': returns electric field; if 'B': magnetic field
    
    Returns
    -------
      E0 (B0):       Complex E-(B-)Field at each dipole position as 
                     list of (complex) 3-tuples: [(Ex1, Ey1, Ez1), ...]
    """
    from scipy import special
    
    if 'eps_env' in env_dict.keys():
        n2 = n2 = n3 = env_dict['eps_env']**0.5
    else:
        # n1 = env_dict['eps1']**0.5
        n2 = env_dict['eps2']**0.5
        n3 = env_dict['eps3']**0.5
        # spacing = np.float32(env_dict['spacing'].real)
        if n2 != n3:
            warnings.warn("fast_electron only supports a single interface " + 
                          "(between `n1`/`n2`). " +
                          "The simulation might not be a good approximation.")
    
    ## constant parameters
    qe = 4.80321E-10     # elementary charge (Franklin)    
    Eo_el = 511.0        # electron rest mass (keV)	   
    c = 2.99792458E10    # Speed of light (cm/s)   

    gamma = 1. + electron_kinetic_energy/Eo_el  # Gamma = Lorentz factor
    f = np.sqrt(1.-1./gamma**2.)                # speed of electrons in units of c
    kz =  n2*(2.*np.pi/wavelength)            
    

    Ex = np.zeros(len(pos), dtype=DTYPE_C)
    Ey = np.zeros(len(pos), dtype=DTYPE_C)
    Ez = np.zeros(len(pos), dtype=DTYPE_C)
    for ipos, rp in enumerate(pos):
        xpos = rp[0] - x0
        ypos = rp[1] - y0   
        zpos = rp[2]    
        ##  --------- Electric field --------- 
        R = np.sqrt(xpos**2 + ypos**2)
        if (R > avoid_div_lim_distance):
            if returnField.lower() == 'e':
                U = kz*R / (f*gamma)
                phase = np.exp(1j*kSign*kz*zpos/f)
                factor = qe * kz * 1E7 / (np.pi * c * f**2. * gamma * n2**2.)
                Er = phase * factor * special.kv(1, U)
                Ex[ipos] = - Er * xpos/R
                Ey[ipos] = - Er * ypos/R
                Ez[ipos] = kSign*factor*1j * special.kv(0, U)/gamma
        ##  --------- Magnetic field --------- 
            else:
                ## !!! TODO
                raise NotImplementedError("fast-electron magnetic field not yet implemented.")
                
        else:
            Ex[ipos] = 0.0
            Ey[ipos] = 0.0
            Ez[ipos] = 0.0
    
    return np.transpose([Ex, Ey, Ez])




if __name__ == "__main__":
    pass
