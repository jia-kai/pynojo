# $File: user.py
# $Date: Wed Feb 15 23:21:31 2012 +0800
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
# pylint: disable=C0111
"""handling requests about users, such as login/logout/register"""

from pyramid.view import view_config
from pynojo.view import mkroute

@view_config(route_name = mkroute(pattern = 'user/login', name = 'user.login'))
def login(request):
    return None

@view_config(route_name = mkroute(pattern = 'user/register',
    name = 'user.register'), renderer = 'user.mako')
def register(request):
    return {}
