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
    Package providing different field generators 
    as illumination sources for pyGDM2
    
    - fast electron fields by A. Arbouet
    - focused vectorbeams by A. Arbouet, Y. Brûlé and G. Colas des Francs
    
"""
__name__ = 'pyGDM2.fields'
__author__ = 'Peter R. Wiecha'



## populate namespace
from pyGDM2.fields import efield_class
from pyGDM2.fields import regular
from pyGDM2.fields import focused_beams
from pyGDM2.fields import electron
from pyGDM2.fields import deprecated

from pyGDM2.fields.efield_class import efield

from pyGDM2.fields.regular import nullfield
from pyGDM2.fields.regular import plane_wave, gaussian
from pyGDM2.fields.regular import dipole_electric, dipole_magnetic

from pyGDM2.fields.focused_beams import HermiteGauss00, HermiteGauss01, HermiteGauss10
from pyGDM2.fields.focused_beams import Radial_pol_doughnut, Azimuth_pol_doughnut

from pyGDM2.fields.electron import fast_electron

from pyGDM2.fields.deprecated import planewave, focused_planewave, evanescent_planewave


## for pygdmUI graphical user interface:
FIELDS_LIST = [plane_wave, gaussian, 
               dipole_electric, dipole_magnetic,
               focused_planewave, 
               HermiteGauss00, HermiteGauss01, HermiteGauss10,
               Radial_pol_doughnut, Azimuth_pol_doughnut,
               fast_electron]