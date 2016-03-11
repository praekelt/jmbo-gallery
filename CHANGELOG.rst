Changelog
=========

2.0.3
-----
#. Fix typo in template.

2.0.2
-----
#. Fix typo in template.
#. Remove redundant LAYER suffixes.

2.0.1
-----
#. Relax explicit pin on jmbo.

2.0.0
-----
#. Stabilize on jmbo 2.0.0.

2.0.0a1
-------
#. Add tests.
#. Django 1.6 compatibility.
#. Up required jmbo to 2.0.0.

0.3
---
#. Remove dependency on `jmbo-foundry`.

0.2.7
-----
#. URL pattern for gallery image.

0.2.6
-----
#. Use correct container to resize embedded video.
#. Added mask argument to PIL.Image.paste to preserve transparancy.

0.2.5
-----
#. Give embedded video its own URL pattern.

0.2.4
-----
#. Convert the product to support South migrations. If you have an existing installation you must do `/bin/django migrate gallery 0001 --fake` once.
#. Add optional content richtext field to gallery.
#. Remove redundant tests.

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

