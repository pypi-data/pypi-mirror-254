#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS GeoConverter.include module

This module is used for Pyramid integration
"""

__docformat__ = 'restructuredtext'

from pyams_geoconverter.interfaces import REST_CONVERTER_PATH, REST_CONVERTER_ROUTE


def include_package(config):
    """Pyramid package include"""

    # add translations
    config.add_translation_dirs('pyams_geoconverter:locales')

    config.add_route(REST_CONVERTER_ROUTE,
                     config.registry.settings.get(f'{REST_CONVERTER_ROUTE}_route.path',
                                                  REST_CONVERTER_PATH))

    config.scan()
