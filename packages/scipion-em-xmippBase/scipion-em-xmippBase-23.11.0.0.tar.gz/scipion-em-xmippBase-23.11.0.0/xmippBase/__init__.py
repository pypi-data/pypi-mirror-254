#!/usr/bin/env python3
# ***************************************************************************
# * Authors:		Alberto García (alberto.garcia@cnb.csic.es)
# *
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307 USA
# *
# * All comments concerning this program package may be sent to the
# * e-mail address 'scipion@cnb.csic.es'
# ***************************************************************************/

import pwem
import subprocess, os
import pyworkflow.utils as pwutils

_references = ['delaRosaTrevin2013', 'Jimenez2022']
_currentBinVersion = '3.23.11.0'
__version__ = _currentBinVersion[2:] + ".0"  # Set this to ".0" on each xmipp binary release, otherwise increase it --> ".1", ".2", ...
        # X.Y.M = version of the xmipp release associated.
        # sv = Set this to ".0" on each xmipp  release.
        # For not release version (hotfix) increase it --> ".1", ".2", ...

class Plugin(pwem.Plugin):
        pass

