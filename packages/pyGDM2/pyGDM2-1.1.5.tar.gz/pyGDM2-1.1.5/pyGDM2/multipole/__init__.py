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
    Package providing tools around the multipole expansion of pyGDM2 simulations
    
    - free-space multipole propagators by C. Majorel
    - generalized polarizabilities: contributions by A. Patoux
    
"""
__name__ = 'pyGDM2.multipole'
__author__ = 'Peter R. Wiecha'



## populate namespace
from pyGDM2.multipole import main
from pyGDM2.multipole import processing
from pyGDM2.multipole import polarizabilities
from pyGDM2.multipole import propagators

from pyGDM2.multipole.main import multipole_decomposition_exact

from pyGDM2.multipole.processing import extinct, _multipole_extinct
from pyGDM2.multipole.processing import scs, _multipole_scs
from pyGDM2.multipole.processing import farfield, _multipole_farfield
from pyGDM2.multipole.processing import _multipole_nearfield
from pyGDM2.multipole.processing import density_of_multipolar_modes

from pyGDM2.multipole.polarizabilities import generalized_polarizability
from pyGDM2.multipole.polarizabilities import extract_effective_polarizability
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_m
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_p
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_qe
from pyGDM2.multipole.polarizabilities import eval_generalized_polarizability_qm
