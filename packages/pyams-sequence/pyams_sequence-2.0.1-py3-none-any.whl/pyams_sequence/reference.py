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

"""PyAMS_sequence.reference module

This module provides a simple mixin class which can be used as base class to
handle internal references to contents based on their internal IDs.
"""

from hypatia.catalog import CatalogQuery
from hypatia.interfaces import ICatalog
from hypatia.query import Eq
from pyramid.events import subscriber
from zope.interface import implementer
from zope.lifecycleevent import IObjectModifiedEvent

from pyams_catalog.query import CatalogResultSet
from pyams_layer.interfaces import IPyAMSUserLayer
from pyams_sequence.interfaces import IInternalReference, ISequentialIdInfo
from pyams_sequence.workflow import get_last_version, get_version_in_state, get_visible_version
from pyams_utils.registry import get_utility
from pyams_utils.request import check_request
from pyams_utils.zodb import volatile_property
from pyams_workflow.interfaces import IWorkflowState, IWorkflowTransitionEvent

try:
    from pyams_zmi.interfaces import IAdminLayer
except ImportError:
    IAdminLayer = IPyAMSUserLayer


__docformat__ = 'restructuredtext'


def get_reference_target(reference, state=None, request=None):
    """Get target of given reference OID

    If a workflow state is provided, the function tries to return the last content
    in this state; otherwise:
     - if the current request in a management interface request, the last version is returned
     - otherwise, the last visible/published version is retrieved.
    """
    if not reference:
        return None
    catalog = get_utility(ICatalog)
    params = Eq(catalog['oid'], reference)
    results = list(CatalogResultSet(CatalogQuery(catalog).query(params)))
    if results:
        if state:
            results = list(filter(lambda x: get_version_in_state(x, state), results))
        else:
            if request is None:
                request = check_request()
            if IAdminLayer.providedBy(request):
                getter = get_last_version
            else:
                getter = get_visible_version
            results = list(map(getter, results))
        if results:
            return results[0]
    return None


@implementer(IInternalReference)
class InternalReferenceMixin:
    """Internal reference mixin class"""

    _reference = None

    @property
    def reference(self):
        """Reference getter"""
        return self._reference

    @reference.setter
    def reference(self, value):
        """Reference setter"""
        self._reference = value
        del self.target

    @volatile_property
    def target(self):
        """Default target getter"""
        return get_reference_target(self.reference)

    def get_target(self, state=None, request=None):
        """Complete target getter"""
        if request is None:
            request = check_request()
        if (not state) and not IPyAMSUserLayer.providedBy(request):
            return self.target
        return get_reference_target(self.reference, state, request)


@subscriber(IObjectModifiedEvent, context_selector=IInternalReference)
def handle_modified_reference(event):
    """Handle modified reference"""
    for description in event.descriptions:
        for attribute in description.attributes:
            if attribute == 'reference':
                del event.object.target
                return


@subscriber(IWorkflowTransitionEvent)
def handle_workflow_transition(event):
    """Handle workflow transition to update internal references

    Target is handled as a volatile property to keep references in memory.
    Reference must be updated when a content is published or retired while being in version
    greater than 1.
    """
    workflow_state = IWorkflowState(event.object, None)
    if (workflow_state is None) or (workflow_state.version_id == 1):
        return  # don't update references on first version
    sequence_info = ISequentialIdInfo(event.object, None)
    if sequence_info is not None:
        catalog = get_utility(ICatalog)
        params = Eq(catalog['link_reference'], sequence_info.hex_oid)
        for result in CatalogResultSet(CatalogQuery(catalog).query(params)):
            if IInternalReference.providedBy(result):
                del result.target
