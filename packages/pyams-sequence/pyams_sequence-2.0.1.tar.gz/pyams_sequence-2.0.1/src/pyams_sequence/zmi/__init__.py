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

"""PyAMS_sequence.zmi main module

This module defines SequentialIntIds utility management views.
"""

from zope.interface import Interface

from pyams_form.ajax import ajax_form_config
from pyams_form.field import Fields
from pyams_layer.interfaces import IPyAMSLayer
from pyams_security.interfaces.base import MANAGE_SYSTEM_PERMISSION
from pyams_sequence.interfaces import ISequentialIntIds
from pyams_utils.adapter import adapter_config
from pyams_utils.interfaces.intids import IIndexLength
from pyams_zmi.form import AdminModalEditForm
from pyams_zmi.interfaces import IAdminLayer, IObjectLabel
from pyams_zmi.interfaces.table import ITableElementEditor
from pyams_zmi.table import TableElementEditor


__docformat__ = 'restructuredtext'

from pyams_sequence import _  # pylint: disable=ungrouped-imports


@adapter_config(required=(ISequentialIntIds, IAdminLayer, Interface),
                provides=IObjectLabel)
def sequence_label(context, request, view):
    """Sequence label getter"""
    return request.localizer.translate(_("Sequences manager"))


@adapter_config(required=(ISequentialIntIds, IAdminLayer, Interface),
                provides=ITableElementEditor)
class SequentialIntIdsEditor(TableElementEditor):
    """Sequential IDs editor adapter"""


@ajax_form_config(name='properties.html', context=ISequentialIntIds, layer=IPyAMSLayer)
class SequentialIntIdsPropertiesEditForm(AdminModalEditForm):
    """Sequential IDs properties edit form"""

    title = _("Sequences generator")
    legend = _("Properties")

    fields = Fields(IIndexLength) + Fields(ISequentialIntIds)

    _edit_permission = MANAGE_SYSTEM_PERMISSION
