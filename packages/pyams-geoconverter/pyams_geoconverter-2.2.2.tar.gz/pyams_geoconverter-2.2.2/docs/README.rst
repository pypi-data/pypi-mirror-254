==========================
PyAMS GeoConverter package
==========================

.. contents::


What is PyAMS?
==============

PyAMS (Pyramid Application Management Suite) is a small suite of packages written for applications
and content management with the Pyramid framework.

**PyAMS** is actually mainly used to manage web sites through content management applications (CMS,
see PyAMS_content package), but many features are generic and can be used inside any kind of web
application.

All PyAMS documentation is available on `ReadTheDocs <https://pyams.readthedocs.io>`_; source code
is available on `Gitlab <https://gitlab.com/pyams>`_ and pushed to `Github
<https://github.com/py-ams>`_. Doctests are available in the *doctests* source folder.


What is PyAMS GeoConverter?
===========================

PyAMS GeoConverter is a small package which provides a single API which can be used to convert a
geospatial data file from one format to another; the default usage is to convert GeoJSON files
to ESRI shapefiles, but you can convert between all formats supported by GeoPandas package.

API also allows you to change coordinates reference system (CRS) during the conversion. All API
documentation is available via standard PyAMS Swagger endpoint.
