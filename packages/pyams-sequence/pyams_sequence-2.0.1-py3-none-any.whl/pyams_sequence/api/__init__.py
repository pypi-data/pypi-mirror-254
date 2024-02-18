#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_sequence.skin main module

This module provides references search function.
"""

from pyramid.view import view_config

from pyams_security.interfaces.base import USE_INTERNAL_API_PERMISSION
from pyams_sequence.interfaces import ISequentialIntIds
from pyams_sequence.sequence import get_sequence_dict
from pyams_utils.registry import get_utility

__docformat__ = 'restructuredtext'


@view_config(name='find-references.json',
             permission=USE_INTERNAL_API_PERMISSION,
             renderer='json', xhr=True)
def find_references(request):
    """Find all references matching given query"""
    query = request.params.get('term')
    if not query:
        return []
    sequence = get_utility(ISequentialIntIds)
    return sorted([
        get_sequence_dict(result)
        for result in sequence.find_references(query,
                                               request.params.get('content_type'),
                                               request)
    ], key=lambda x: x['text'])
