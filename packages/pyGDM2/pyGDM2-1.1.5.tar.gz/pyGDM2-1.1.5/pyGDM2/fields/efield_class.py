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
"""

from __future__ import print_function
from __future__ import absolute_import

import itertools
import warnings
import copy
import types
import cmath

import numpy as np
import numba




#==============================================================================
# globals
#==============================================================================
DTYPE_C = np.complex64



#==============================================================================
# Incident field container class
#==============================================================================
class efield(object):
    """incident electromagnetic field container class
    
    Defines an incident electric field including information about wavelengths,
    polarizations, focal spot or whatever optional parameter is supported by
    the used field generator.
    
    Parameters
    ----------
    field_generator : `callable`
        field generator function. Mandatory arguments are 
          - `struct` (instance of :class:`.structures.struct`)
          - `wavelength` (list of wavelengths)
    
    wavelengths : list
        list of wavelengths (wavelengths in nm)
    
    kwargs : list of dict or dict
        possible additional keyword arguments, passed to `field_generator`.
        Either dict or list of dicts.
          - If list of dicts, each entry must correspond exactly to one 
            parameters-set for `field-generator`.
          - If dict, maybe contain lists for configurations of the parameters. 
            In that case, all possible parameter-permutations will be generated.
    
    Examples
    --------
    >>> kwargs = dict(theta = [0.0,45,90])
    [{'theta': 0.0}, {'theta': 45.0}, {'theta': 90.0}]
    
    is equivalent to:
    
    >>> kwargs = [dict(theta=0.0), dict(theta=45.0), dict(theta=90.0)]
    [{'theta': 0.0}, {'theta': 45.0}, {'theta': 90.0}]
    
    """
    def __init__(self, field_generator, wavelengths, kwargs):
        """initialize field container"""
        self.field_generator = field_generator
        self.wavelengths = np.array(wavelengths)
        self.kwargs = copy.deepcopy(kwargs)
        _kwargs = copy.deepcopy(kwargs)
        
        ## --- generate parameter-sets for field-generator
        if type(_kwargs) == dict:
            ## --- integer parameters to list
            for key in _kwargs:
                if type(_kwargs[key]) not in [list, np.ndarray]:
                    _kwargs[key] = [_kwargs[key]]
            
            ## --- generate all permutations of kwargs for direct use in field_generator
            varNames = sorted(_kwargs)
            self.kwargs_permutations = [dict(zip(varNames, prod)) for 
                                    prod in itertools.product(*(_kwargs[varName] 
                                                for varName in varNames))]
        elif type(_kwargs) == list:
            self.kwargs_permutations = []
            for kw in _kwargs:
                self.kwargs_permutations.append(kw)
                if type(kw) != dict:
                    raise ValueError("Wrong input for 'kwargs': Must be either dict or list of dicts.")
                
        else:
            raise ValueError("Wrong input for 'kwargs': Must be either dict or list of dicts.")
        
        ## set precision to single by default
        self.setDtype(np.float32, np.complex64)
    
    
    def setDtype(self, dtypef, dtypec):
        """set dtype of arrays"""
        self.dtypef = dtypef
        self.dtypec = dtypec
    
    
    ## !!! Todo: add automatic field gradient calculation
    # def get_field_gradient():
    #     from pyGDM2 import linear
    #     gradE0 = linear.field_gradient(sim, field_index, r_qe, 
    #                                    delta=eps_dd, which_fields=['E0'])
    #     gradH0 = linear.field_gradient(sim, field_index, r_qm, 
    #                                    delta=eps_dd, which_fields=['H0'])


    def __repr__(self, verbose=False):
        out_str =  ' ----- incident field -----'
        out_str += '\n' + '   field generator: "{}"'.format(self.field_generator.__name__)
        out_str += '\n' + '   {} wavelengths between {} and {}nm'.format(
                         len(self.wavelengths), self.wavelengths.min(),
                         self.wavelengths.max(),)
        if verbose or len(self.wavelengths)<6:
            for i, wl in enumerate(self.wavelengths):
                out_str += '\n' + '      - {}: {}nm'.format(i,wl)
        out_str += '\n' + '   {} incident field configurations per wavelength'.format(
                                        len(self.kwargs_permutations))    
        if verbose or len(self.kwargs_permutations)<6:
            for i, kw in enumerate(self.kwargs_permutations):
                out_str += '\n' + '      - {}: {}'.format(i,str(kw).replace("{","").replace("}",""))
        return out_str




