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

"""PyAMS_geoconverter.api.schema module

"""

from colander import MappingSchema, OneOf, SchemaNode, String, drop
from zipfile import ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA

from pyams_utils.rest import ObjectUploadType


ZIP_MODES = {
    'store': ZIP_STORED,
    'deflate': ZIP_DEFLATED,
    'bzip2': ZIP_BZIP2,
    'lzma': ZIP_LZMA
}


class ConverterInput(MappingSchema):
    """Converter input schema"""

    data = SchemaNode(ObjectUploadType(),
                      description="Document input data; may be provided in Base64 when "
                                  "using JSON format",
                      missing=drop)

    filename = SchemaNode(String(),
                          description="Document file name",
                          missing=drop)

    content_type = SchemaNode(String(),
                              description="Input file content type",
                              missing="application/geo+json")

    encoding = SchemaNode(String(),
                          description="Input data encoding",
                          missing='utf-8')

    input_crs = SchemaNode(String(),
                           description="Input coordinates reference system; default is WGS84",
                           missing='EPSG:4326')

    output_crs = SchemaNode(String(),
                            description="Output coordinates reference system; default is Lambert 93",
                            missing="EPSG:2154")

    output_driver = SchemaNode(String(),
                               description="Output file format",
                               missing="ESRI Shapefile")

    output_basename = SchemaNode(String(),
                                 description="Base output file name, without extension",
                                 missing=drop)

    output_mode = SchemaNode(String(),
                             description="Response output mode; set as 'json' to get data encoded "
                                         "in base64 format, or as 'attachment' to get data as "
                                         "attachment",
                             validator=OneOf(('json', 'attachment')),
                             missing="attachment")

    output_encoding = SchemaNode(String(),
                                 description="Encoding used for output file",
                                 missing='iso-8859-1')

    output_compression = SchemaNode(String(),
                                    description="Compression mode used for output file",
                                    validator=OneOf(ZIP_MODES.keys()),
                                    missing='store')


class ConverterOutput(MappingSchema):
    """Converter output schema"""

    data = SchemaNode(String(),
                      description="Document output data, encoded in Base64")

    content_type = SchemaNode(String(),
                              description="Data content-type")

    filename = SchemaNode(String(),
                          description="Output file name")


class ConverterResponse(MappingSchema):
    """Converter output response"""

    body = ConverterOutput()
