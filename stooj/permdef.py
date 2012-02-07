# $File: permdef.py
# $Date: Tue Feb 07 14:52:21 2012 +0800
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

# pylint: disable=W0622,C0103,E1101,W0212


"""Definitions of various permission enumerations"""

import __builtin__

from stooj.lib.enum import get_base
Base = get_base()

class PermDesciption(object):
    """Literal description for a permission."""

    __slots__ = ('_title', '_desc')

    def __init__(self, title, desc):
        """*title* and *desc* are callables, which, when get invoked,
        should return the translated description message in the current
        locale. """
        self._title = title
        self._desc = desc

    @property
    def title(self):
        """title of this permission"""
        return self._title()

    @property
    def desc(self):
        """the description."""
        return self._desc()

_ = lambda *args, **kargs: lambda: __builtin__._(*args, **kargs)
_pl = lambda *args, **kargs: lambda: __builtin__._pl(*args, **kargs)


class UserGroup(Base):
    """User group permissions. See the source for detailed descriptions."""

    ADD_PROB = Base.enum(PermDesciption(_('Adding Problem'), _(
        'Capability of adding problems to the database and managing problems '
        'added by that user.  The newly added problems will not have '
        'associated problem group, and thus not displayed. The administrator '
        'should move it to some problem group to make it available to other '
        'users.')))
