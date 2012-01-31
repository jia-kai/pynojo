# $File: __init__.py
# $Date: Tue Jan 31 23:59:25 2012 +0800
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
"""
This module define the views for stooj.

The following globals will be added to Chameleon templates:
    * *layout*: global layout macro
    * *_*: translation function for l10n
"""

from pyramid.events import subscriber, BeforeRender
from stooj.nls import get_translator

_layout_macro = None
@subscriber(BeforeRender)
def _add_global(event):
    global _layout_macro
    if _layout_macro is None:
        from pyramid.renderers import get_renderer
        _layout_macro = get_renderer('template/layout.pt').implementation()
    event['layout'] = _layout_macro
    event['_'] = get_translator(event['request'])

