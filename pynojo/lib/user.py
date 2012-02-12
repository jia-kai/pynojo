# $File: user.py
# $Date: Sun Feb 12 23:15:37 2012 +0800
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
"""helper functions for maintaining users"""

from sqlalchemy.orm.exc import NoResultFound

from pynojo.exc import PynojoRuntimeError
from pynojo.model import Session
from pynojo.model.user import User

def get_model(request):
    """Return an instance of :class:`pynojo.model.User`, or *None* if no user
    has logged in."""
    val = request.pynojo_cache.get(get_model, -1)
    if val is -1:
        request.pynojo_cache[get_model] = _get_model(request)
    return val


def check_login_pw(request, username, passwd, cookie_max_age = None):
    """Check user login via password authentication. Raise
    :exc:`pynojo.exc.PynojoRuntimeError` on error. If login is successful,
    corresponding cookies are set."""
    ses = Session()
    ok = True
    try:
        user = ses.query(User).filter(User.username == username).one()
    except NoResultFound:
        ok = False
    else:
        if user.auth_pw is None:
            ok = False
        else:
            ok = user.auth_pw.check(passwd)

    if not ok:
        raise PynojoRuntimeError(_('Failed to log in.'))

    request.pynojo_cache[get_model] = user
    request.set_cookie('uid', user.id, cookie_max_age)
    request.set_cookie('token', user.update_auth_code(), cookie_max_age)


def _get_model(req):
    uid = req.cookies.get('uid', -1)
    if uid is -1:
        return None

    ses = Session()
    try:
        user = ses.query(User).filter(User.id == uid).one()
    except NoResultFound:
        return None

    if user.get_auth_code() == req.cookies.get('token'):
        return user
    return None

