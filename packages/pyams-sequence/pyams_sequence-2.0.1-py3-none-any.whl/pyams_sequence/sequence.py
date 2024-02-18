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

"""PyAMS_sequence.sequence module

This module defines adapters for sequences targets objects.
"""

from persistent import Persistent
from pyramid.events import subscriber
from zope.interface import Interface
from zope.lifecycleevent import IObjectAddedEvent, IObjectRemovedEvent
from zope.schema.fieldproperty import FieldProperty

from pyams_catalog.interfaces import IBeforeObjectIndexEvent
from pyams_i18n.interfaces import II18n
from pyams_sequence.interfaces import ISequentialIdInfo, ISequentialIdTarget, ISequentialIntIds
from pyams_utils.adapter import ContextRequestViewAdapter, adapter_config, get_annotation_adapter
from pyams_utils.factory import factory_config
from pyams_utils.interfaces.tales import ITALESExtension
from pyams_utils.registry import get_utility, query_utility


__docformat__ = 'restructuredtext'


def get_sequence_dict(content, attribute='title', request=None):
    """Get OID and label matching given content"""
    sequence = get_utility(ISequentialIntIds)
    info = ISequentialIdInfo(content)
    i18n = II18n(content, None)
    return {
        'id': info.hex_oid,
        'text': '{} ({})'.format(i18n.query_attribute(attribute, request=request)
                                 if i18n is not None else getattr(content, attribute, None),
                                 sequence.get_short_oid(info.oid))
    }


@factory_config(ISequentialIdInfo)
class SequentialIdInfo(Persistent):
    """Sequential ID info"""

    oid = FieldProperty(ISequentialIdInfo['oid'])
    hex_oid = FieldProperty(ISequentialIdInfo['hex_oid'])

    def get_full_oid(self):
        """Full OID getter"""
        sequence = get_utility(ISequentialIntIds)
        return sequence.get_full_oid(self.oid)

    def get_short_oid(self):
        """Short OID getter"""
        sequence = get_utility(ISequentialIntIds)
        return sequence.get_short_oid(self.oid)

    def get_base_oid(self):
        """Base OID getter"""
        sequence = get_utility(ISequentialIntIds)
        return sequence.get_base_oid(self.oid)

    @property
    def public_oid(self):
        """Public OID getter"""
        return self.get_short_oid()


SEQUENCE_INFO_KEY = 'pyams_sequence.info'


@adapter_config(required=ISequentialIdTarget,
                provides=ISequentialIdInfo)
def sequential_id_info_factory(context):
    """Sequential ID info factory adapter"""
    return get_annotation_adapter(context, SEQUENCE_INFO_KEY, ISequentialIdInfo,
                                  notify=False, locate=False)


@subscriber(IBeforeObjectIndexEvent, context_selector=ISequentialIdTarget)
@subscriber(IObjectAddedEvent, context_selector=ISequentialIdTarget)
def handle_added_intid_target(event):
    """Generate content OID before indexing"""
    target = event.object
    sequence = query_utility(ISequentialIntIds, name=getattr(target, 'sequence_name', ''))
    if sequence is not None:
        info = ISequentialIdInfo(target)
        if not info.oid:  # Objects cloned inside a workflow may share the same ID...
            info.oid = sequence.register(target)
            info.hex_oid = sequence.query_hex_oid(target)


@subscriber(IObjectRemovedEvent, context_selector=ISequentialIdTarget)
def handle_removed_intid_target(event):
    """Handle removed sequential ID target"""
    target = event.object
    sequence = query_utility(ISequentialIntIds, name=getattr(target, 'sequence_name', ''))
    if sequence is not None:
        info = ISequentialIdInfo(target)
        if info.oid:
            sequence.unregister(target)


@adapter_config(name='oid',
                required=(Interface, Interface, Interface),
                provides=ITALESExtension)
class OIDTalesExtension(ContextRequestViewAdapter):
    """tales:oid(context) TALES extension"""

    def render(self, context=None):
        """TALES extension renderer"""
        if context is None:
            context = self.context
        info = ISequentialIdInfo(context, None)
        if info is not None:
            return info.public_oid
        return ''
