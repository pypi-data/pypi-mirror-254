======================
PyAMS_sequence package
======================

Introduction
------------

PyAMS_sequence is a package used to get sequential identifiers. In PyAMS framework, these
identifiers are actually used to identify contents for which several contents may share the
same ID.

This package is composed of a set of utility functions, usable into any Pyramid application.

    >>> from pprint import pprint

    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> config = setUp(hook_zca=True)
    >>> config.registry.settings['zodbconn.uri'] = 'memory://'

    >>> from pyramid_zodbconn import includeme as include_zodbconn
    >>> include_zodbconn(config)
    >>> from cornice import includeme as include_cornice
    >>> include_cornice(config)
    >>> from cornice_swagger import includeme as include_swagger
    >>> include_swagger(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)
    >>> from pyams_site import includeme as include_site
    >>> include_site(config)
    >>> from pyams_i18n import includeme as include_i18n
    >>> include_i18n(config)
    >>> from pyams_catalog import includeme as include_catalog
    >>> include_catalog(config)
    >>> from pyams_security import includeme as include_security
    >>> include_security(config)
    >>> from pyams_viewlet import includeme as include_viewlet
    >>> include_viewlet(config)
    >>> from pyams_form import includeme as include_form
    >>> include_form(config)
    >>> from pyams_skin import includeme as include_skin
    >>> include_skin(config)
    >>> from pyams_sequence import includeme as include_sequence
    >>> include_sequence(config)

An ISequentialIntIds instance is created automatically on instance upgrade:

    >>> from pyams_site.generations import upgrade_site
    >>> request = DummyRequest()
    >>> app = upgrade_site(request)
    Upgrading PyAMS timezone to generation 1...
    Upgrading PyAMS security to generation 2...
    Upgrading PyAMS sequence to generation 1...

    >>> from zope.traversing.interfaces import BeforeTraverseEvent
    >>> from pyams_utils.registry import handle_site_before_traverse
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))

    >>> from pyams_utils.registry import get_utility
    >>> from pyams_sequence.interfaces import ISequentialIntIds
    >>> seq = get_utility(ISequentialIntIds)
    >>> seq
    <pyams_sequence.utility.SequentialIntIds object at 0x...>
    >>> seq.prefix = 'AMS:'
    >>> seq.last_oid
    0
    >>> seq.last_oid = 10
    >>> seq.last_oid
    10
    >>> seq.last_oid = 0
    Traceback (most recent call last):
    ...
    zope.interface.exceptions.Invalid: Can't set last OID to value lower than current one!


Getting content ID
------------------

Let's try to register a simple object:

    >>> obj = object()
    >>> seq.register(obj) is None
    True

Let's declare and create a sequence target:

    >>> from zope.interface import implementer
    >>> from persistent import Persistent
    >>> from zope.location import Location
    >>> from pyams_sequence.interfaces import ISequentialIdTarget

    >>> @implementer(ISequentialIdTarget)
    ... class MyTarget(Persistent, Location):
    ...     """Target class"""
    ...     title = 'Content title'

    >>> obj = MyTarget()
    >>> app['obj1'] = obj

    >>> from zope.lifecycleevent import ObjectAddedEvent
    >>> config.registry.notify(ObjectAddedEvent(obj, app))

    >>> from pyams_sequence.interfaces import ISequentialIdInfo
    >>> info = ISequentialIdInfo(obj)
    >>> info.oid
    11
    >>> info.hex_oid
    'AMS:000000000b'
    >>> info.get_full_oid()
    'AMS:0000000011'
    >>> info.get_short_oid()
    'AMS: b'
    >>> info.get_base_oid()
    ' b'
    >>> info.public_oid
    'AMS: b'

SequentialIntIds utility also provides other utility methods:

    >>> seq.query_hex_oid(None) is None
    True
    >>> seq.get_full_oid('+b')
    'AMS:000000000b'
    >>> seq.get_full_oid('AMS: b')
    'AMS: b'
    >>> seq.get_internal_id('+b')
    11
    >>> seq.get_internal_id('AMS:b')
    11

    >>> seq.query_object_from_oid(info.hex_oid) is obj
    True


Looking for contents
--------------------

    >>> from pyams_sequence.api import find_references

    >>> request = DummyRequest()
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))
    >>> pprint(find_references(request))
    []

    >>> request = DummyRequest(params={'term': '+b'})
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))
    >>> pprint(find_references(request))
    [{'id': 'AMS:000000000b', 'text': 'Content title (AMS: b)'}]

    >>> request = DummyRequest(params={'term': 'b'})
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))
    >>> pprint(find_references(request))
    [{'id': 'AMS:000000000b', 'text': 'Content title (AMS: b)'}]

A REST API is also available to look for internal references:

    >>> from pyams_sequence.api.rest import find_references
    >>> request = DummyRequest(params={'term': '+b'})
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))
    >>> pprint(find_references(request))
    {'results': [{'id': 'AMS:000000000b', 'text': 'Content title (AMS: b)'}],
     'status': 'success'}


Sequences schema
----------------

Internal references fields are available, to easily search and reference other internal
objects using their internal ID:

    >>> from pyams_sequence.reference import InternalReferenceMixin
    >>> class Content(InternalReferenceMixin):
    ...     """Content class with internal reference"""

    >>> content = Content()
    >>> content.reference = info.hex_oid

    >>> hasattr(content, '_v_target')
    False
    >>> content.target is obj
    True
    >>> hasattr(content, '_v_target')
    True
    >>> content._v_target is obj
    True
    >>> content.get_target() is obj
    True

Updating the internal reference automatically removes volatile property:

    >>> content.reference = None
    >>> hasattr(content, '_v_target')
    False

    >>> content.reference = info.hex_oid

    >>> from pyams_sequence.interfaces import IInternalReference
    >>> from zope.lifecycleevent import ObjectModifiedEvent, Attributes
    >>> config.registry.notify(ObjectModifiedEvent(content, Attributes(IInternalReference, 'reference')))


Internal reference widget
-------------------------

A dedicated form widget is available to handle selection of internal references:

    >>> from zope.interface import alsoProvides

    >>> from pyams_form.form import EditForm
    >>> from pyams_form.field import Fields
    >>> from pyams_form.testing import TestRequest
    >>> from pyams_layer.interfaces import IPyAMSLayer

    >>> from pyams_sequence.interfaces import IInternalReference

    >>> class TestForm(EditForm):
    ...     fields = Fields(IInternalReference)

    >>> request = TestRequest()
    >>> alsoProvides(request, IPyAMSLayer)

    >>> form = TestForm(content, request)
    >>> form.update()

    >>> 'reference' in form.widgets
    True
    >>> print(form.widgets['reference'].render())
    <select id="form-widgets-reference"
            name="form.widgets.reference"
            class="form-control select2 select-widget required internalreferencefield-field"
            size="1"
            data-placeholder="No selected reference"
            data-ajax--url="/api/sequence/references"
            data-minimum-input-length="2">
            <option></option>
            <option id="form-widgets-reference-0"
                    value="AMS:000000000b"
                    selected="selected">Content title (AMS: b)</option>
    </select>
    <input name="form.widgets.reference-empty-marker" type="hidden" value="1" />

You can filter internal references using a "content_type" field attribute; this should then
match a catalog keyword index with this name:

    >>> from zope.interface import Interface
    >>> from zope.schema.fieldproperty import FieldProperty
    >>> from pyams_sequence.schema import InternalReferenceField

    >>> class IAnotherContent(Interface):
    ...     reference = InternalReferenceField(title="Reference with content type",
    ...                                        content_type='MyContent',
    ...                                        required=True)

    >>> class AnotherTestForm(EditForm):
    ...     fields = Fields(IAnotherContent)

    >>> @implementer(IAnotherContent)
    ... class AnotherContent:
    ...     reference = FieldProperty(IAnotherContent['reference'])

    >>> another_content = AnotherContent()

    >>> form = AnotherTestForm(another_content, request)
    >>> form.update()
    >>> print(form.widgets['reference'].render())
    <select id="form-widgets-reference"
            name="form.widgets.reference"
            class="form-control select2 select-widget required internalreferencefield-field"
            size="1"
            data-placeholder="No selected reference"
            data-ajax--url="/api/sequence/references"
            data-ajax--params='{"content_type": "MyContent"}'
            data-minimum-input-length="2">
            <option></option>
    </select>
    <input name="form.widgets.reference-empty-marker" type="hidden" value="1" />

Select options list is actually empty in this test because we don't have a testing catalog
with "content_type" name!


Workflow related functions
--------------------------

Sequences have been designed with workflow in mind. But workflow related functions should
return correct results even when working with contents which are not managed by a workflow:

    >>> from pyams_sequence.workflow import get_last_version, get_visible_version, \
    ...     get_version_in_state, get_sequence_target

    >>> get_last_version(obj) is obj
    True
    >>> get_last_version(None) is None
    True
    >>> get_visible_version(obj) is obj
    True
    >>> get_visible_version(None) is None
    True
    >>> get_version_in_state(obj, 'draft') is obj
    True
    >>> get_version_in_state(None, 'draft') is None
    True
    >>> get_sequence_target('AMS:0123456789', 'draft') is None
    True


Tests cleanup:

    >>> from zope.lifecycleevent import ObjectRemovedEvent
    >>> del app['obj1']
    >>> config.registry.notify(ObjectRemovedEvent(obj, app))
    >>> seq.query_object_from_oid(info.hex_oid) is None
    True

    >>> tearDown()
