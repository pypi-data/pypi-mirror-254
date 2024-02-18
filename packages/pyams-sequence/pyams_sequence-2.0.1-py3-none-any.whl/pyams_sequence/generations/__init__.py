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

"""PyAMS_sequence.generations main module

This module is checking for registered utilities on site upgrade.
"""
from pyams_catalog.generations import check_required_indexes
from pyams_catalog.index import FieldIndexWithInterface, KeywordIndexWithInterface
from pyams_sequence.interfaces import IInternalReference, IInternalReferencesList, \
    ISequentialIdInfo, ISequentialIntIds
from pyams_site.generations import check_required_utilities
from pyams_site.interfaces import ISiteGenerations
from pyams_utils.registry import utility_config


__docformat__ = 'restructuredtext'

REQUIRED_UTILITIES = ((ISequentialIntIds, '', None, 'Sequential IDs'),)

REQUIRED_INDEXES = [
    ('oid', FieldIndexWithInterface, {
        'interface': ISequentialIdInfo,
        'discriminator': 'hex_oid'
    }),
    ('link_reference', FieldIndexWithInterface, {
        'interface': IInternalReference,
        'discriminator': 'reference'
    }),
    ('link_references', KeywordIndexWithInterface, {
        'interface': IInternalReferencesList,
        'discriminator': 'references'
    })
]


@utility_config(name='PyAMS sequence', provides=ISiteGenerations)
class CatalogGenerationsChecker:
    """Catalog generations checker"""

    order = 50
    generation = 1

    def evolve(self, site, current=None):  # pylint: disable=no-self-use,unused-argument
        """Check for required utilities"""
        check_required_utilities(site, REQUIRED_UTILITIES)
        check_required_indexes(site, REQUIRED_INDEXES)
