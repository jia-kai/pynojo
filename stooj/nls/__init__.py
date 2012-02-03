# $File: __init__.py
# $Date: Fri Feb 03 14:43:18 2012 +0800
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
"""Nativ Language Support for stooj. See also :ref:`devnotes-nls`."""

from stooj.exception import StoojInnerError
from stooj.nls.config import TRANS_LIST


class Translator:
    """the class which actually implements the translation of message
    identifiers to translatied message strings"""

    _tr = None	# gettext.GNUTranslations class

    def __init__(self, lang):
        """
        :param lang: name of the language. If it is None,
                     :class:`gettext.NullTranslations` is used. Otherwise, if
                     no corresponding .mo file found,
                     :exc:`stooj.exception.StoojInnerError` would be raised.
        :type lang: str or None
        """
        import gettext
        if lang is None:
            self._tr = gettext.NullTranslations()
        else:
            from os.path import dirname, join
            locale_dir = join(dirname(__file__), 'locale')
            try:
                self._tr = gettext.translation('stooj', locale_dir, [lang])
            except IOError:
                raise StoojInnerError(
                        'attempt to load unimplmented translation: {0}' .
                        format(lang))

    def get_translation(self, msgid, *args, **kargs):
        """Return a Unicode string translation of message identifier *msgid*,
        with *args* and *kargs* passed to :meth:`str.format` on the
        result. See also :meth:`get_plural_translation`."""
        return self._tr.ugettext(msgid).format(*args, **kargs)

    def get_plural_translation(self, singular, plural, n, *args, **kargs):
        """Return a Unicode string translation based on two message identifiers
        and the number *n*. When *n* is 1, *singular* is used for lookup in the
        catalog; otherwise *plural* is used. See also
        :meth:`get_translation`."""
        return self._tr.ungettext(singular, plural, n).format(*args, **kargs)


def get_translator(request):
    """Return an instance of :class:`Translator` according to the locale
    implied by pyramid request *request*."""
    # pylint: disable=W0212
    if request._stooj_translator_cache is None:
        request._stooj_translator_cache = _get_translator(request)
    return request._stooj_translator_cache



_trans_list_tag2translator = dict()
_trans_list_offers = list()
_trans_list_default_translator = Translator(None)
def _init_trans_list_vars():
    global _trans_list_tag2translator, _trans_list_offers
    for i in TRANS_LIST:
        tr = Translator(i.locale_dir)
        _trans_list_offers.extend(i.lang_tag)
        for j in i.lang_tag:
            _trans_list_tag2translator[j] = tr


# initialize here, rather than on the first access in _get_translator, to avoid
# dealing with thread safety stuff
_init_trans_list_vars()

def _get_translator(req):
    tag = req.accept_language.best_match(_trans_list_offers)
    if tag is None:
        return _trans_list_default_translator
    return _trans_list_tag2translator[tag]


def init(request_factory):
    """Initialize NLS. *request_factory* is a pyramid request factory class to
    be configured.  Two methods named *_* and *_pl* will be added to it, which
    can be used for translation and plural translation, respectively. See
    :meth:`Translator.get_translation` and
    :meth:`Translator.get_plural_translation`.
    """

    request_factory._stooj_translator_cache = None

    request_factory._ = lambda self, *args, **kargs: \
            get_translator(self).get_translation(*args, **kargs)

    request_factory._pl = lambda self, *args, **kargs: \
            get_translator(self).get_plural_translation(*args, **kargs)

