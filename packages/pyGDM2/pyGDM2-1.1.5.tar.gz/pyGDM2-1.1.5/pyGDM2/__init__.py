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
    pyGDM2 - a full-field electrodynamical solver python toolkit.
    Based on the Green Dyadic Method.
    
    Contributors:
        - P.R. Wiecha (maintainer)
        - Ch. Girard
        - A. Arbouet
        - C. Majorel
        - A. Patoux
        - G. Colas des Francs
        - Y. Brûlé
    
"""
__name__ = 'pyGDM2'
__version__ = '1.1.5'
__date__ = "01/25/2024"   # MM/DD/YYY
__author__ = 'Peter R. Wiecha'

__all__ = ["core", "materials", "structures", "fields", 
           "propagators", "propagators_2D", "propagators_periodic",
           "linear", "nonlinear", 
           "tools", "visu", 
           "EO"]


# make modules available at package level
# from pyGDM2 import core
# from pyGDM2 import materials
# from pyGDM2 import structures
# from pyGDM2 import fields
# from pyGDM2 import propagators
# from pyGDM2 import linear
# from pyGDM2 import multipole
# from pyGDM2 import nonlinear
# from pyGDM2 import electron
# from pyGDM2 import tools
# from pyGDM2 import visu



## compatibility with deprecated transition modules:
from pyGDM2 import core as core_py
from pyGDM2 import fields as fields_py
from pyGDM2 import linear as linear_py

