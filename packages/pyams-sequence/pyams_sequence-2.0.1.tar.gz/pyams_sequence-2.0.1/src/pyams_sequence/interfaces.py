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

"""PyAMS sequence.interfaces module

This module defines public sequence utility interfaces.
"""

from zope.annotation import IAttributeAnnotatable
from zope.interface import Attribute, Interface
from zope.schema import Int, TextLine

from pyams_sequence.schema import InternalReferenceField, InternalReferencesListField


__docformat__ = 'restructuredtext'

from pyams_sequence import _


REST_REFERENCES_SEARCH_ROUTE = 'pyams_sequence.rest.references'
'''References search API route name'''

REST_REFERENCES_SEARCH_PATH = '/api/sequence/references'
'''References search API default path'''


class ISequentialIntIds(Interface):
    """Sequential IntIds utility interface"""

    prefix = TextLine(title=_("Hexadecimal prefix"),
                      description=_("Prefix used to generate hexadecimal ID"),
                      required=False,
                      max_length=10)

    hex_oid_length = Int(title=_("Hexadecimal ID length"),
                         description=_("Full length of hexadecimal ID, not including prefix"),
                         min=0,
                         max=20,
                         default=10)

    last_oid = Int(title=_("Last OID"),
                   description=_("Last used sequence; WARNING: you can change this to a higher "
                                 "value, but never to a lower one!"),
                   required=True,
                   default=0)

    def query_hex_oid(self, obj):
        """Generate an hexadecimal ID for the given sequence"""

    def get_full_oid(self, oid, obj_prefix=None):
        """Get full ID based on partial OID"""

    def get_short_oid(self, oid, obj_prefix=None):
        """Get short ID based on given numeric object ID"""

    def get_base_oid(self, oid, obj_prefix=None):
        """Get base ID (without prefix) based on given numeric object ID"""

    def get_internal_id(self, oid):
        """Get internal ID matching given OID"""

    def query_object_from_oid(self, oid):
        """Query object with given OID"""

    def find_references(self, query, content_type=None, request=None):
        """Find references matching given query"""


class ISequentialIdInfo(Interface):
    """Sequential ID info interface"""

    oid = Int(title=_("Sequential ID"),
              required=False)

    hex_oid = TextLine(title=_("Unique ID"),
                       required=False)

    public_oid = TextLine(title=_("Unique ID"),
                          readonly=True)

    def get_full_oid(self):
        """Get full OID"""

    def get_short_oid(self):
        """Get short OID"""

    def get_base_oid(self):
        """Get base OID"""


class ISequentialIdTarget(IAttributeAnnotatable):
    """Marker interface used to identify contents requiring sequential IDs"""

    sequence_name = TextLine(title=_("Sequence name"),
                             description=_("Name of registered sequence utility used to get "
                                           "unique IDs"),
                             required=False)

    sequence_prefix = TextLine(title=_("Hexadecimal prefix"),
                               description=_("Prefix used to generate hexadecimal ID, placed "
                                             "after utility prefix. Generally defined at class "
                                             "level..."),
                               required=False)


class IInternalReference(IAttributeAnnotatable):
    """Internal link interface"""

    reference = InternalReferenceField(title=_("Internal reference"),
                                       description=_("Internal link target reference. You can "
                                                     "search a reference using '+' followed by "
                                                     "internal number, of by entering text "
                                                     "matching content title."),
                                       required=True)

    target = Attribute("Internal reference target")

    def get_target(self, state=None, request=None):
        """Get target from internal reference"""


class IInternalReferencesList(IAttributeAnnotatable):
    """Internal references list"""

    references = InternalReferencesListField(title=_("Internal references"),
                                             description=_("List of internal references"),
                                             required=False)

    use_references_for_views = Attribute("Boolean attribute used to specify if internal references should "
                                         "be used as views context references")

    def get_targets(self, state=None):
        """Get iterator over targets from internal references"""
