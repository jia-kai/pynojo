# $File: user.py
# $Date: Thu Feb 09 17:41:00 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
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
# pylint: disable=C0111

"""models for users and user groups"""

from pynojo.config import config
from pynojo.model._base import *

_AUTH_CODE_LEN = 9

class _Tablename:
    User = 'user'
    UserGroup = 'ugrp'
    MapUserGrpAndGrpPerm = 'ugrpperm'


class User(Base):
    __tablename__ = _Tablename.User

    id = Column(Integer, primary_key = True)

    username = Column(String(config.user.USERNAME_LEN_MAX),
            index = True, unique = True)
    """username for login, immutable"""

    dispname = Column(String(config.user.DISPNAME_LEN_MAX))
    """display name"""

    grp_id = Column(Integer, ForeignKey(_Tablename.UserGroup + '.id'))
    """id of the group that the user belongs to"""

    group = relationship('UserGroup', uselist = False,
                backref = backref('users', lazy = 'dynamic',
                    cascade = "all, delete-orphan"))
    """the group that the user belongs to; a relationship to
    :class:`UserGroup`"""


    # pylint: disable=C0322
    # I do not know why pylint thinks it is an operator...
    auth_pw = None
    """User authentication via password. This attribute is a relationship to
    :class:`UserAuthPW <pynojo.model.user_auth_pw.UserAuthPW>`; defined by
    backref in :attr:`UserAuthPW.user
    <pynojo.model.user_auth_pw.UserAuthPW.user>`."""


    _auth_code = Column('authcode', BINARY(_AUTH_CODE_LEN))

    def get_auth_code(self):
        """Return an ascii authentication code string, which can be set to
        cookie and later used for authentication.  See also
        :meth:`update_auth_code`."""
        if self._auth_code is None:
            return self.update_auth_code()
        from base64 import b64encode
        return b64encode(self._auth_code, '-_')

    def update_auth_code(self):
        """Update the authentication code, invalidating the previously
        generated one. Return the new authentication code."""
        from pynojo.lib import gen_random_str
        self._auth_code = gen_random_str(_AUTH_CODE_LEN)
        return self.get_auth_code()



class UserGroup(Base):
    __tablename__ = _Tablename.UserGroup

    id = Column(Integer, primary_key = True)

    name = Column(String(config.user.GRPNAME_LEN_MAX), index = True)
    """name of the group"""

    users = None
    """users belonging to this group; defined by backref in :attr:`User.group`.
    Note that dynamic loading is used."""

    _perms = relationship('MapUserGrpAndGrpPerm', collection_class = set,
            cascade = "all, delete-orphan")

    perms = association_proxy('_perms', 'perm')
    """permissions of this group. It just behaves like a Python *set*.
    Available permissions are defined in :class:`pynojo.permdef.UserGroup`."""




class MapUserGrpAndGrpPerm(Base):
    """Many-to-many map between user groups and user group permissions. Usually
    this model is not directly used, use :attr:`UserGroup.perms` instead."""
    __tablename__ = _Tablename.MapUserGrpAndGrpPerm

    def __init__(self, perm):
        self.perm = perm

    grp_id = Column(Integer, ForeignKey(_Tablename.UserGroup + '.id'), 
            index = True, primary_key = True)

    perm = Column(SmallInteger, index = True, primary_key = True)


