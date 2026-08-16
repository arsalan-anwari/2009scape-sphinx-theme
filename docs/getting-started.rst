===============
Getting started
===============

Installation
============

.. code-block:: console

   $ pip install sphinx-2009scape-theme

Or, from a checkout of this repository:

.. code-block:: console

   $ pip install -e .

Enabling the theme
==================

Set ``html_theme`` in ``conf.py``. The theme registers itself through a Sphinx
entry point, so no ``extensions`` entry is required when it is installed as a
package:

.. code-block:: python
   :caption: docs/conf.py

   html_theme = "2009scape"

When you are running the theme straight from a source checkout (no install),
add it as an extension instead and put ``src`` on ``sys.path``:

.. code-block:: python
   :caption: docs/conf.py

   import sys
   from pathlib import Path

   sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

   extensions = ["sphinx_2009scape_theme"]
   html_theme = "2009scape"

Adding a logo
=============

The header shows ``logo_text`` next to ``html_logo``. Pixel art scales best
here. The logo is rendered with ``image-rendering: pixelated``.

.. code-block:: python

   html_logo = "_static/logo.png"

   html_theme_options = {
       "logo_text": "My Project",
       "logo_subtitle": "v2.1 docs",
   }

Fonts
=====

Ten RuneScape fonts ship with the theme (from the CC0-licensed
`RuneStar/fonts <https://github.com/RuneStar/fonts>`_ project) and are served
from the build output, so documentation builds stay offline-friendly.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option value
     - Font stack
   * - ``rs``
     - RuneScape Plain 12: the default body font
   * - ``rs-bold``
     - RuneScape Bold 12: headings and interface labels
   * - ``rs-quill``
     - RuneScape Quill: scroll and quest text
   * - ``rs-quill-caps``
     - RuneScape Quill Caps
   * - ``rs-surok``
     - RuneScape Surok
   * - ``rs-barbarian``
     - RuneScape Barbarian Assault
   * - ``rs-fairy``
     - RuneScape Fairy Large
   * - ``system``
     - The reader's system UI font

Long-form prose in a pixel font is an acquired taste. If your documentation is
dense, keep the RuneScape chrome and switch just the body copy:

.. code-block:: python

   html_theme_options = {
       "body_font": "system",
       "heading_font": "rs-bold",
   }

.. tip::

   Any raw CSS font stack works too. ``"body_font": "'Inter', sans-serif"``
   is passed straight through.
