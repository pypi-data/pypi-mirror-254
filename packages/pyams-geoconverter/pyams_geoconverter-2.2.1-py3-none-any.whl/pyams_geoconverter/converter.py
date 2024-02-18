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

"""PyAMS_GeoConverter.converter module

"""


import os
import tempfile
import zipfile
from io import BytesIO

import geopandas
from fiona.io import ZipMemoryFile
from fiona.meta import extensions

from pyams_file.file import get_magic_content_type
from pyams_geoconverter.api.schema import ZIP_MODES
from pyams_utils.unicode import translate_string


def convert_document(settings):
    """Convert incoming document"""
    input_data = settings.pop('data')
    content_type = settings.get('content_type') or get_magic_content_type(input_data)
    if content_type.startswith('application/zip'):
        with ZipMemoryFile(input_data) as memory_file:
            with memory_file.open() as src:
                df = geopandas.GeoDataFrame.from_features(src,
                                                          crs=settings.get('input_crs'))
    else:
        df = geopandas.read_file(BytesIO(input_data))
    df = df.to_crs(settings.get('output_crs'))
    with tempfile.TemporaryDirectory() as dirname:
        basename = settings.get('filename').rsplit('.', 1)[0]
        driver = settings['output_driver']
        if driver == 'ESRI Shapefile':
            columns = []
            for column in map(lambda x: translate_string(x, force_lower=False),
                              df.columns):
                name, index = column, 1
                while name in columns:
                    index += 1
                    name = f'{column}_{index:02}'
                columns.append(name)
            df.columns = columns
            for geom_type in df.geom_type.unique():
                df[df.geom_type == geom_type].to_file(f'{dirname}/{basename}-{geom_type}',
                                                      driver=driver,
                                                      encoding=settings.get('output_encoding'),
                                                      layer=geom_type)
        else:
            extension = extensions(driver)[0]
            df.to_file(f'{dirname}/{basename}.{extension}',
                       driver=driver,
                       encoding=settings.get('output_encoding'))
        output_data = BytesIO()
        output_zip = zipfile.ZipFile(output_data,
                                     mode='w',
                                     compression=ZIP_MODES[settings.get('output_compression')],
                                     compresslevel=9)
        for root, dirs, files in os.walk(dirname):
            for name in files:
                output_zip.write(os.path.join(root, name), name)
        output_zip.close()
        return output_data.getvalue()
