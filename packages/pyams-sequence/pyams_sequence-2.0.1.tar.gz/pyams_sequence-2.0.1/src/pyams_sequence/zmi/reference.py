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

"""PyAMS_*** module

"""

__docformat__ = 'restructuredtext'

from pyramid.interfaces import IRequest

from pyams_sequence.interfaces import ISequentialIdInfo
from pyams_sequence.reference import get_reference_target
from pyams_utils.adapter import adapter_config
from pyams_utils.interfaces.text import IHTMLRenderer
from pyams_utils.text import BaseHTMLRenderer
from pyams_zmi.utils import get_object_label


@adapter_config(name='reference-label',
                required=(str, IRequest),
                provides=IHTMLRenderer)
class ReferenceRenderer(BaseHTMLRenderer):
    """Convert internal reference to text using target label"""

    def render(self, **kwargs):
        target = get_reference_target(self.context)
        if target is not None:
            label = get_object_label(target, self.request, None)
            oid = ISequentialIdInfo(target).public_oid
            return '{} ({})'.format(label or '--', oid)
