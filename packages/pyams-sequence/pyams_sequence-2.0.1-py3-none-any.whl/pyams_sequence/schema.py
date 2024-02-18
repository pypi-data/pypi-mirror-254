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

"""PyAMS_sequence.schema module

This module defines custom schema fields associated with sequences.
"""

from zope.interface import Attribute, implementer
from zope.schema import List, TextLine
from zope.schema.interfaces import IList, ITextLine

__docformat__ = 'restructuredtext'


class IInternalReferenceField(ITextLine):
    """Internal reference field interface"""

    content_type = Attribute("Requested target content type")


@implementer(IInternalReferenceField)
class InternalReferenceField(TextLine):
    """Internal reference field"""

    def __init__(self, *args, content_type=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.content_type = content_type


class IInternalReferencesListField(IList):
    """Internal references list field interface"""

    content_type = Attribute("Requested target content type")


@implementer(IInternalReferencesListField)
class InternalReferencesListField(List):
    """Internal references list field"""

    def __init__(self, content_type=None, value_type=None, unique=False, **kwargs):
        super().__init__(value_type=TextLine(),
                         unique=True,
                         **kwargs)
        self.content_type = content_type
