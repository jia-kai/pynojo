# $File: __init__.py
# $Date: Mon Feb 27 20:18:38 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia	<jia.kai66@gmail.com>
#
# This file is part of pynojo
# 
# pynojo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pynojo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with pynojo.  If not, see <http://www.gnu.org/licenses/>.
#

# pylint: disable=C0103
"""This package provides pynojo static configurations. To access the config,
import *config* from *pynojo.config*. See also :ref:`devnotes.sysconf`."""

from pynojo.config._base import set_init_finished
from pynojo.config.all import AllConfig

config = AllConfig()

try:
    from pynojo.config.overwrite import overwrite
except ImportError:
    pass
else:
    overwrite(config)

set_init_finished()


