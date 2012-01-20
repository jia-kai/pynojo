# $File: i18n.py
# $Date: Fri Jan 20 10:48:12 2012 +0800
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

class StrTranslator:
    """i18n class for stooj"""
    def __init__(self, lang):
        pass

    def get_translate(self, str, *args, **kargs):
        """return the translation of ``str``, with ``args`` and ``kargs`` passed
        to str.format"""
        # XXX: not implemented
        return str.format(*args, **kargs)

translators = StrTranslator('').get_translate # XXX: translator for each language

def init(conf):
    """Initialize i18n support for the pyramid configurator ``conf``.
    The request passed to view callables will include an attribute
    called ``_`` used for translation"""
    
    from pyramid.request import Request
    class _Request(Request):
        @property
        def _(self):
            global translators
            return translators #XXX

    conf.set_request_factory(_Request)

