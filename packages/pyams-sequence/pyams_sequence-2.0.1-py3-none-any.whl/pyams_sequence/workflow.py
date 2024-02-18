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

"""PyAMS_sequence.workflow module

This module defines a few helper functions which are mainly related to workflow
management.
"""

from pyams_sequence.interfaces import ISequentialIdInfo, ISequentialIntIds
from pyams_utils.registry import get_utility
from pyams_workflow.interfaces import IWorkflow, IWorkflowManagedContent, \
    IWorkflowPublicationInfo, IWorkflowVersion, IWorkflowVersions


__docformat__ = 'restructuredtext'


def get_last_version(content):
    """Check for last available version"""
    versions = IWorkflowVersions(content, None)
    if versions is not None:
        content = versions.get_last_versions()[0]
    if ISequentialIdInfo(content, None) is not None:
        return content
    return None


def get_visible_version(content):
    """Check for visible version"""
    versions = IWorkflowVersions(content, None)
    if versions is not None:
        workflow = IWorkflow(content)
        visible_versions = versions.get_versions(workflow.visible_states, sort=True)  # pylint: disable=assignment-from-no-return
        if visible_versions:
            return visible_versions[-1]
        return None
    publication_info = IWorkflowPublicationInfo(content, None)
    if publication_info is not None:
        return content if publication_info.is_visible() else None
    return content


def get_version_in_state(content, state):
    """Check for versions in given status"""
    if IWorkflowVersion.providedBy(content) or IWorkflowManagedContent.providedBy(content):
        versions = IWorkflowVersions(content).get_versions(state, sort=True)  # pylint: disable=assignment-from-no-return
        if versions:
            content = versions[-1]
    if ISequentialIdInfo(content, None) is not None:
        return content
    return None


def get_sequence_target(oid, state=None):
    """Get content matching given OID"""
    sequence = get_utility(ISequentialIntIds)
    content = sequence.query_object_from_oid(oid)
    if state and (IWorkflowVersion.providedBy(content) or IWorkflowManagedContent.providedBy(content)):
        versions = IWorkflowVersions(content).get_versions(state, sort=True)  # pylint: disable=assignment-from-no-return
        if versions:
            content = versions[0]
            return content
    return content
