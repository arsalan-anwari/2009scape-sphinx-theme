====================
2009scape for Sphinx
====================

A Sphinx theme that dresses your documentation as a 2009-era RuneScape
interface: pixel fonts, bevelled stone panels, gold headings and the familiar
orange body text.

The visual language is ported from the `runescapecn <https://github.com/alns0dev/runescapecn>`_
shadcn registry.

.. note::

   The theme is dark by design. RuneScape's interface never had a light mode,
   and neither does this. Every colour is a CSS custom property, so a light
   palette can be layered on with ``css_variables`` if you disagree.

Quick start
===========

.. code-block:: console

   $ pip install sphinx-2009scape-theme

.. code-block:: python
   :caption: docs/conf.py

   html_theme = "2009scape"

   html_theme_options = {
       "logo_text": "My Project",
       "github_url": "https://github.com/me/my-project",
   }

That is the whole setup. Read :doc:`configuration` for the full option list, or
:doc:`kitchen-sink/index` to see every element rendered.

.. toctree::
   :maxdepth: 2
   :caption: Guide

   getting-started
   configuration

.. toctree::
   :maxdepth: 2
   :caption: Reference

   kitchen-sink/index
   api
