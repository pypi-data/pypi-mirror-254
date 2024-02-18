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

"""PyAMS_sequence.utility module

This module defines main sequence utility class, and several events handlers;.
"""

from hypatia.catalog import CatalogQuery
from hypatia.interfaces import ICatalog
from hypatia.query import Contains, Eq
from zope.interface import Invalid
from zope.intid import IntIds
from zope.schema.fieldproperty import FieldProperty

from pyams_catalog.query import CatalogResultSet
from pyams_i18n.interfaces import INegotiator
from pyams_sequence.interfaces import ISequentialIdTarget, ISequentialIntIds
from pyams_sequence.workflow import get_last_version
from pyams_utils.adapter import ContextAdapter, adapter_config
from pyams_utils.factory import factory_config


__docformat__ = 'restructuredtext'

from pyams_sequence import _  # pylint: disable=ungrouped-imports
from pyams_utils.interfaces.intids import IIndexLength
from pyams_utils.list import unique
from pyams_utils.registry import get_utility
from pyams_utils.request import check_request


@factory_config(ISequentialIntIds)
class SequentialIntIds(IntIds):
    """Sequential IntIds utility"""

    prefix = FieldProperty(ISequentialIntIds['prefix'])
    hex_oid_length = FieldProperty(ISequentialIntIds['hex_oid_length'])
    _last_oid = FieldProperty(ISequentialIntIds['last_oid'])

    @property
    def last_oid(self):
        """Last OID getter"""
        return self._last_oid

    @last_oid.setter
    def last_oid(self, value):
        """Last OID setter"""
        if value < self._last_oid:
            raise Invalid(_("Can't set last OID to value lower than current one!"))
        self._last_oid = value

    def _generateId(self):
        self._last_oid += 1
        return self._last_oid

    def register(self, ob):
        if not ISequentialIdTarget.providedBy(ob):
            return None
        return super().register(ob)

    def query_hex_oid(self, obj):
        """Query OID in hexadecimal format"""
        oid = self.queryId(obj)
        if oid is not None:
            return '{{prefix}}{{obj_prefix}}{{hex_id:0{length}x}}' \
                .format(length=self.hex_oid_length) \
                .format(prefix=self.prefix or '',
                        obj_prefix=getattr(obj, 'sequence_prefix', ''),
                        hex_id=oid)
        return None

    def get_full_oid(self, oid, obj_prefix=None):
        """Get full OID, including prefix and leading zeros"""
        if not isinstance(oid, str):
            oid = str(oid)
        if oid.startswith('+'):
            oid = oid[1:].lower()
        elif self.prefix and oid.startswith(self.prefix):
            return oid
        return '{prefix}{obj_prefix}{zeros}{hex_id}' \
            .format(prefix=self.prefix or '',
                    obj_prefix=obj_prefix or '',
                    zeros='0' * (self.hex_oid_length - len(oid)),
                    hex_id=oid.lower() if oid else 0)

    def get_short_oid(self, oid, obj_prefix=None):
        """Get short OID, including prefix with without leading zero"""
        return '{prefix}{obj_prefix} {hex_id:x}' \
            .format(prefix=self.prefix or '',
                    obj_prefix=obj_prefix or '',
                    hex_id=oid or 0)

    @staticmethod
    def get_base_oid(oid, obj_prefix=None):
        """Get base OID, containing only object prefix and OID in hexadecimal"""
        return '{obj_prefix} {hex_id:x}' \
            .format(obj_prefix=obj_prefix or '',
                    hex_id=oid or 0)

    def get_internal_id(self, oid):
        """Get internal ID, without prefix"""
        if not isinstance(oid, str):
            oid = str(oid)
        if oid.startswith('+'):
            oid = oid[1:]
        elif self.prefix and oid.startswith(self.prefix):
            oid = oid[len(self.prefix):]
        return int(oid, 16)

    def query_object_from_oid(self, oid):
        """Query object matching given OID"""
        internal_id = self.get_internal_id(oid)
        return self.queryObject(internal_id)

    def find_references(self, query, content_type=None, request=None):
        """Find internal references matching given query"""
        if not query:
            return
        if request is None:
            request = check_request()
        catalog = get_utility(ICatalog)
        if query.startswith('+'):
            params = Eq(catalog['oid'], self.get_full_oid(query))
        else:
            query_params = Eq(catalog['oid'], self.get_full_oid(query))
            negotiator = get_utility(INegotiator)
            for lang in {
                request.registry.settings.get('pyramid.default_locale_name', 'en'),
                request.locale_name,
                negotiator.server_language
            } | negotiator.offered_languages:
                index_name = 'title:{0}'.format(lang)
                if index_name in catalog:
                    index = catalog[index_name]
                    if index.check_query(query):
                        query_params |= Contains(index,
                                                 ' and '.join((w + '*' for w in query.split())))
            params = query_params
        if content_type:
            params &= Eq(catalog['content_type'], content_type)
        yield from unique(filter(lambda x: x is not None,
                                 map(get_last_version,
                                     CatalogResultSet(CatalogQuery(catalog).query(params)))))


@adapter_config(required=ISequentialIntIds,
                provides=IIndexLength)
class SequentialIntIdsIndexLengthAdapter(ContextAdapter):
    """Sequential IDs index length adapter"""

    @property
    def count(self):
        """Sequence length getter"""
        return len(self.context)
