# encoding: utf-8
#
#Copyright (C) 2017-2023, P. R. Wiecha
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
    Package providing different sets of dyadic Green's functions for pyGDM2
    
    - 2D codes benchmarked against fortran code by G. Colas des Francs
    
"""
__name__ = 'pyGDM2.propagators'
__author__ = 'Peter R. Wiecha'



## populate namespace
from pyGDM2.propagators import propagators
from pyGDM2.propagators import propagators_2D
from pyGDM2.propagators import propagators_periodic
from pyGDM2.propagators import propagators_periodic_slow

from pyGDM2.propagators.propagators import DyadsBaseClass
from pyGDM2.propagators.propagators import DyadsQuasistatic123
from pyGDM2.propagators.propagators import _G0, _G0_HE, _G_mirrorcharge_123
from pyGDM2.propagators.propagators import _G0_EE_asymptotic
from pyGDM2.propagators.propagators import G0_EE_123, Gs_EE_123, Gtot_EE_123
from pyGDM2.propagators.propagators import Gs_EE_asymptotic
from pyGDM2.propagators.propagators import G_HE_123
from pyGDM2.propagators.propagators import greens_tensor_evaluation
from pyGDM2.propagators.propagators import t_sbs_EE_123_quasistatic, t_sbs_HE_123_quasistatic




## for pygdmUI graphical user interface:
DYADS_LIST = [propagators.DyadsQuasistatic123, 
              propagators_2D.DyadsQuasistatic2D123]