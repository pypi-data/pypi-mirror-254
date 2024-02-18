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

"""PyAMS_sequence.api.reference module

This module defines REST API used to search internal references.
"""

import sys

from colander import MappingSchema, SchemaNode, SequenceSchema, String, drop
from cornice import Service
from cornice.validators import colander_validator
from pyramid.httpexceptions import HTTPOk

from pyams_security.interfaces.base import USE_INTERNAL_API_PERMISSION
from pyams_security.rest import check_cors_origin, set_cors_headers
from pyams_sequence.interfaces import ISequentialIntIds, REST_REFERENCES_SEARCH_ROUTE
from pyams_sequence.sequence import get_sequence_dict
from pyams_utils.registry import query_utility
from pyams_utils.rest import BaseResponseSchema, STATUS, rest_responses


__docformat__ = 'restructuredtext'


TEST_MODE = sys.argv[-1].endswith('/test')


class ReferencesSearchQuery(MappingSchema):
    """Internal references search schema"""
    term = SchemaNode(String(),
                      description="Terms search query; can be an internal reference OID, eventually "
                                  "prefixed with a \"+\", or a text query which should "
                                  "match contents title")
    content_type = SchemaNode(String(),
                              description="Set content type to restrict references search",
                              missing=drop)


class Reference(MappingSchema):
    """Reference result schema"""
    id = SchemaNode(String(),
                    description="Reference ID")
    text = SchemaNode(String(),
                      description="Reference title")


class ReferencesList(SequenceSchema):
    """References search results"""
    result = Reference()


class ReferencesSearchResults(BaseResponseSchema):
    """References search results schema"""
    results = ReferencesList(description="References search results list")


references_service = Service(name=REST_REFERENCES_SEARCH_ROUTE,
                             pyramid_route=REST_REFERENCES_SEARCH_ROUTE,
                             description="Internal references management")


@references_service.options(validators=(check_cors_origin, set_cors_headers))
def references_options(request):  # pylint: disable=unused-argument
    """References service OPTIONS handler"""
    return ''


class ReferencesGetRequest(MappingSchema):
    """References getter request"""
    querystring = ReferencesSearchQuery()


class ReferencesGetResponse(MappingSchema):
    """References getter response"""
    body = ReferencesSearchResults()


references_get_responses = rest_responses.copy()
references_get_responses[HTTPOk.code] = ReferencesGetResponse(
    description="References search results")


@references_service.get(permission=USE_INTERNAL_API_PERMISSION,
                        schema=ReferencesGetRequest(),
                        validators=(check_cors_origin, colander_validator, set_cors_headers),
                        response_schemas=references_get_responses)
def find_references(request):
    """Returns list of references matching given query"""
    params = request.params if TEST_MODE else request.validated.get('querystring', {})
    query = params.get('term')
    if not query:
        return {
            'status': STATUS.ERROR.value,
            'message': 'Missing arguments',
            'results': []
        }
    content_type = params.get('content_type')
    sequence = query_utility(ISequentialIntIds)
    return {
        'status': STATUS.SUCCESS.value,
        'results': sorted([
            get_sequence_dict(result)
            for result in sequence.find_references(query, content_type, request)
        ], key=lambda x: x['text'])
    }
