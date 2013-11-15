Changelog
=========

next
----
#. Convert the product to support South migrations. If you have an existing installation you must do `/bin/django migrate gallery 0001 --fake` once.
#. Add optional content richtext field to gallery.

0.2.3
-----
#. Cache templates.

0.2.2
-----
#. Do not assume the presence of jquery.
#. Friendlier url to detail page.

0.2.1
-----
#. Bulk image upload form

0.2
---
#. Refactor embedded video so it can be used in a gallery.
#. Finer grained photo sizes. Run `jmbo-foundry` load_photosizes to activate these new photo sizes.
#. Videos launch the native player on mobile devices.

0.1
---
#. Add dependency on `jmbo-foundry`.
#. Port templates from `jmbo-foundry`.

0.0.3
-----
#. Clean up detail view.

