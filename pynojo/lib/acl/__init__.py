# $File: __init__.py
# $Date: Mon Mar 05 19:45:19 2012 +0800
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
"""access limiter, see also :ref:`perm-model.acl`"""

__all__ = ['check']

from pkgutil import walk_packages
for loader, module_name, is_pkg in walk_packages(__path__, __name__ + '.'):
    __import__(module_name, globals(), locals(), [], -1)

from pynojo.lib.acl._base import Base
from pynojo.model.acl import ACLMdl

def check(request, acl_id):
    """Check whether the ACL with id *acl_id* allows the access request."""
    return Base.from_id(acl_id).check(request)

