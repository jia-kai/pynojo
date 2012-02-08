# $File: pkg.py
# $Date: Fri Feb 03 14:17:53 2012 +0800
#
# Copyright (C) 2012 the stooj development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
#
# This file is part of stooj
# 
# stooj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# stooj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with stooj.  If not, see <http://www.gnu.org/licenses/>.
#

# pylint: disable=C0111
from stooj.config._base import ConfigBase

class PkgInfo(ConfigBase):
    """package information"""

    NAME = 'stooj'

    COPYRIGHT = '2012, stooj development team'

    VERSION = '0.1'
    """the short X.Y version"""

    RELEASE = '0.1-alpha'
    """the full version, including alpha/beta/rc tags"""
