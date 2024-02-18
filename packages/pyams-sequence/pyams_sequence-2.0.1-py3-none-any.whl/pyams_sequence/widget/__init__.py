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

"""PyAMS_sequence.widget main module

This modules defines custom widgets used to select internal references.
"""

import json

from zope.interface import implementer_only
from zope.schema.vocabulary import SimpleTerm

from pyams_form.browser.select import SelectWidget
from pyams_form.converter import SequenceDataConverter
from pyams_form.interfaces import IDataConverter
from pyams_form.interfaces.widget import IFieldWidget
from pyams_form.widget import FieldWidget
from pyams_layer.interfaces import IFormLayer
from pyams_sequence.interfaces import REST_REFERENCES_SEARCH_PATH, REST_REFERENCES_SEARCH_ROUTE
from pyams_sequence.reference import get_reference_target
from pyams_sequence.schema import IInternalReferenceField, IInternalReferencesListField
from pyams_sequence.sequence import get_sequence_dict
from pyams_sequence.widget.interfaces import IInternalReferenceWidget, \
    IInternalReferencesListWidget
from pyams_utils.adapter import adapter_config


__docformat__ = 'restructuredtext'

from pyams_sequence import _


def reference_term_factory(value, request):
    """Reference term factory"""
    reference = get_reference_target(value, request=request)
    if reference is not None:
        reference = get_sequence_dict(reference)
        return SimpleTerm(reference['id'], title=reference['text'])
    return None


#
# Internal reference widget
#

@adapter_config(required=(IInternalReferenceField, IInternalReferenceWidget),
                provides=IDataConverter)
class InternalReferenceDataConverter(SequenceDataConverter):
    """Internal reference data converter"""

    def to_widget_value(self, value):
        """Value to widget converter"""
        if isinstance(value, (list, tuple, set)):
            value = next(iter(value))
        return super().to_widget_value(value)


@implementer_only(IInternalReferenceWidget)
class InternalReferenceWidget(SelectWidget):
    """Internal reference widget"""

    placeholder = _("No selected reference")

    @property
    def ajax_url(self):
        """AJAX URL getter"""
        return self.request.registry.settings.get(f'{REST_REFERENCES_SEARCH_ROUTE}_route.path',
                                                  REST_REFERENCES_SEARCH_PATH)

    @property
    def ajax_params(self):
        """AJAX params getter"""
        if self.field.content_type:
            return json.dumps({'content_type': self.field.content_type})
        return None

    def term_factory(self, value):
        """Selected reference terms factory"""
        return reference_term_factory(value, self.request)


@adapter_config(required=(IInternalReferenceField, IFormLayer),
                provides=IFieldWidget)
def InternalReferenceFieldWidget(field, request):  # pylint: disable=invalid-name
    """Internal reference field widget factory"""
    return FieldWidget(field, InternalReferenceWidget(request))


#
# Internal references set widget
#

@implementer_only(IInternalReferencesListWidget)
class InternalReferencesListWidget(InternalReferenceWidget):
    """Internal references list widget"""

    multiple = 'multiple'
    klass = 'sortable'


@adapter_config(required=(IInternalReferencesListField, IFormLayer),
                provides=IFieldWidget)
def InternalReferencesListFieldWidget(field, request):  # pylint: disable=invalid-name
    """Internal references list field widget factory"""
    return FieldWidget(field, InternalReferencesListWidget(request))
