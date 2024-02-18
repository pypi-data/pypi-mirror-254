#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_sequence.include module

This module is used for Pyramid integration.
"""

import re

from pyams_sequence.interfaces import REST_REFERENCES_SEARCH_PATH, REST_REFERENCES_SEARCH_ROUTE


__docformat__ = 'restructuredtext'


def include_package(config):
    """Pyramid package include"""

    # add translations
    config.add_translation_dirs('pyams_sequence:locales')

    # register new REST API routes
    config.add_route(REST_REFERENCES_SEARCH_ROUTE,
                     config.registry.settings.get(f'{REST_REFERENCES_SEARCH_ROUTE}_route.path',
                                                  REST_REFERENCES_SEARCH_PATH))

    try:
        import pyams_zmi  # pylint: disable=import-outside-toplevel,unused-import
    except ImportError:
        config.scan(ignore=[re.compile(r'pyams_sequence\..*\.zmi\.?.*').search])
    else:
        config.scan()
