Changelog
=========

2.2.1
-----
 - updated REST API route name and path configuration setting name
 - added filename to shapefile archive contents

2.2.0
-----
 - added argument to set output file encoding; default is "iso-8859-1" to be compliant with
   default driver which is ESRI Shapefile

2.1.0
-----
 - added argument to set output file compression mode

2.0.3
-----
 - updated test on incoming data when using multipart/form-data content type

2.0.2
-----
 - removed test of Content-Type header (which is removed when application is
   deployed behind Apache with mod_wsgi)

2.0.1
-----
 - updated Swagger API description
 - renamed columns in case of shapefile conversion

2.0.0
-----
 - migrated to Pyramid 2.0

1.0.0
-----
 - initial release
