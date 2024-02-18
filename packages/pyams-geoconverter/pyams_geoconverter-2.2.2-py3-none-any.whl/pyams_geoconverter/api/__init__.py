#
# Copyright (c) 2015-2023 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_GeoConverter.api module

"""

import base64
import json
import mimetypes
import sys

from cornice import Service
from cornice.validators import colander_body_validator
from pyramid.httpexceptions import HTTPBadRequest, HTTPOk, HTTPServerError
from pyramid.response import Response

from pyams_file.file import get_magic_content_type
from pyams_geoconverter.api.schema import ConverterInput, ConverterResponse
from pyams_geoconverter.converter import convert_document
from pyams_geoconverter.interfaces import REST_CONVERTER_ROUTE
from pyams_security.interfaces.base import USE_INTERNAL_API_PERMISSION
from pyams_security.rest import check_cors_origin, set_cors_headers
from pyams_utils.rest import http_error, rest_responses


TEST_MODE = sys.argv[-1].endswith('/test')


converter_service = Service(name=REST_CONVERTER_ROUTE,
                            pyramid_route=REST_CONVERTER_ROUTE,
                            description="PyAMS GeoConverter service")


@converter_service.options(validators=(check_cors_origin, set_cors_headers))
def converter_options(request):
    """Converter options endpoint"""
    return ''


converter_post_responses = rest_responses.copy()
converter_post_responses[HTTPOk.code] = ConverterResponse(
    description="Converter response")


@converter_service.post(content_type=('application/json',
                                      'multipart/form-data'),
                        schema=ConverterInput(),
                        validators=(check_cors_origin, colander_body_validator,
                                    set_cors_headers),
                        permission=USE_INTERNAL_API_PERMISSION,
                        require_csrf=False,
                        response_schemas=converter_post_responses)
def converter_post(request):
    """Convert incoming document"""
    settings = request.params.copy() if TEST_MODE else request.validated.copy()
    try:
        data = request.json.pop('data', None)
        if isinstance(data, dict):
            data = json.dumps(data).encode(settings.get('encoding'))
        elif isinstance(data, str):
            data = base64.b64decode(data)
    except json.JSONDecodeError:
        data = request.params.get('data')
        if data is not None:
            settings.setdefault('filename', data.filename)
            data = data.file.read()
    if not data:
        return http_error(request, HTTPBadRequest, "Missing input file")
    settings['data'] = data
    try:
        output = convert_document(settings)
    except Exception as e:
        return http_error(request, HTTPServerError, f"File conversion error: {str(e)}")
    content_type = get_magic_content_type(output)
    extension = mimetypes.guess_extension(content_type)
    filename = settings.get('output_basename') or settings.get('filename').rsplit('.', 1)[0]
    if settings.get('output_mode') == 'attachment':
        result = Response(body=output,
                          content_type=content_type,
                          content_disposition=f'attachment; filename="{filename}{extension}"')
    else:
        result = {
            'data': base64.b64encode(output),
            'content_type': content_type,
            'filename': f"{filename}{extension}"
        }
    return result
