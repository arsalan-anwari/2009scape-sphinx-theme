=============
Configuration
=============

Every option below goes in ``html_theme_options``. Values shown are the
defaults.

Branding
========

.. list-table::
   :header-rows: 1
   :widths: 28 18 54

   * - Option
     - Default
     - Description
   * - ``logo_text``
     - ``""``
     - Text next to the logo. Falls back to ``html_title``.
   * - ``logo_subtitle``
     - ``""``
     - Small secondary line, e.g. a version tag.
   * - ``announcement``
     - ``""``
     - Gold banner pinned above the header. HTML is allowed.
   * - ``footer_note``
     - ``""``
     - Small print on its own footer row.

Navigation
==========

.. list-table::
   :header-rows: 1
   :widths: 28 18 54

   * - Option
     - Default
     - Description
   * - ``github_url``
     - ``""``
     - Shows a GitHub icon in the header.
   * - ``discord_url``
     - ``""``
     - Shows a Discord icon in the header.
   * - ``nav_links``
     - ``[]``
     - List of ``{"title": ..., "url": ...}`` header links.
   * - ``show_breadcrumbs``
     - ``true``
     - Ancestor trail above the page title.
   * - ``show_prev_next``
     - ``true``
     - Previous/next panels at the end of each page.
   * - ``show_toc``
     - ``true``
     - Right-hand "on this page" column.
   * - ``toc_title``
     - ``"On this page"``
     - Heading for that column.
   * - ``show_source_link``
     - ``true``
     - "Show source" link, when ``html_show_sourcelink`` is on.
   * - ``back_to_top``
     - ``true``
     - Floating back-to-top button.
   * - ``globaltoc_collapse``
     - ``false``
     - Start sidebar branches collapsed. Toggling is client-side, so the
       whole tree stays reachable either way.
   * - ``globaltoc_includehidden``
     - ``true``
     - Include ``:hidden:`` toctree entries in the sidebar.
   * - ``globaltoc_maxdepth``
     - ``3``
     - Sidebar nesting depth. ``-1`` for unlimited.

Edit this page
==============

Set ``source_repository`` to add an "Edit this page" link. GitHub and GitLab
URL shapes are both recognised.

.. code-block:: python

   html_theme_options = {
       "source_repository": "https://github.com/me/my-project",
       "source_branch": "main",
       "source_directory": "docs",
   }

Typography
==========

.. list-table::
   :header-rows: 1
   :widths: 28 18 54

   * - Option
     - Default
     - Description
   * - ``body_font``
     - ``rs``
     - Body copy font. See :doc:`getting-started`.
   * - ``heading_font``
     - ``rs-bold``
     - Heading font.
   * - ``mono_font``
     - system mono
     - Code font. Code stays in a real monospace face by default, because
       pixel fonts and code indentation do not mix.
   * - ``base_font_size``
     - ``20px``
     - Root font size. Bare numbers are read as pixels.

Surface treatment
=================

.. list-table::
   :header-rows: 1
   :widths: 28 18 54

   * - Option
     - Default
     - Description
   * - ``scanlines``
     - ``true``
     - The faint stone texture on panels, cards and admonitions.
   * - ``pixelated_images``
     - ``false``
     - Render every image with ``image-rendering: pixelated``. Great for
       sprites, unkind to screenshots,hence off by default.
   * - ``css_variables``
     - ``{}``
     - Override any design token. See below.

Recolouring the theme
=====================

Every colour, size and bevel is a CSS custom property on ``:root``. Override
them without touching the stylesheets:

.. code-block:: python

   html_theme_options = {
       "css_variables": {
           "rs-gold": "#7fd4ff",
           "rs-orange": "#c8e8ff",
           "rs-content-max-width": "52rem",
           "rs-sidebar-width": "300px",
       },
   }

The leading ``--`` is optional; both ``rs-gold`` and ``--rs-gold`` work.

.. seealso::

   The full token list lives at the top of
   ``sphinx_2009scape_theme/theme/2009scape/static/css/2009scape.css``.

Custom stylesheets
==================

For anything the tokens do not cover, add your own stylesheet the usual way:

.. code-block:: python

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

Sidebar contents
================

The left sidebar renders whatever is listed in ``html_sidebars``. The default
is:

.. code-block:: python

   html_sidebars = {
       "**": [
           "components/sidebar-brand.html",
           "components/sidebar-search.html",
           "components/sidebar-nav.html",
       ],
   }

Drop templates from that list, reorder them, or add your own.
