==========
Typography
==========

Headings
========

The page title above is ``h1``. This section is ``h2``.

Subsection
----------

That was ``h3``. Headings use RuneScape Bold 12 in gold, uppercased, with the
same drop shadow the game uses for interface labels.

Sub-subsection
~~~~~~~~~~~~~~

``h4`` and below shift to interface orange.

Level five
^^^^^^^^^^

Level six
"""""""""

Inline markup
=============

Body copy is RuneScape Plain 12. It carries **bold text**, *emphasis in
yellow*, ``inline literals`` in a sunken well, :kbd:`Ctrl+C` keys, and
:guilabel:`GUI labels` boxed in gold.

External links look like `this one <https://github.com/RuneStar/fonts>`_ and
carry an arrow; internal links such as :doc:`../configuration` do not.

Footnotes sit at the bottom of the page [#note]_ and citations work the same
way [CIT2009]_.

.. [#note] Footnote bodies are muted and rail-marked.
.. [CIT2009] A citation, for completeness.

Block quotes
============

   Congratulations! You've just advanced a Firemaking level.

   Every player, eventually

Rubrics and centred text
========================

.. rubric:: Rubric heading

.. centered:: Centred interface text

Definition lists
================

Stone
   A grey rock. Mine it.

Bronze bar
   Smelted from copper and tin ore. Requires level 1 Smithing.

Field lists
===========

:Version: 1.0.0
:Authors: Arsalan Anwari
:Status: Release
:Requires: Sphinx 7.3 or newer

Line blocks
===========

| A line block preserves
|     its indentation
| and its line breaks.

Horizontal rule
===============

Below is a ``transition`` node:

----

And content resumes after it.

Topics
======

.. topic:: Topic panel

   A ``topic`` directive renders as a stone panel, same treatment as
   ``.. contents::``.

Versions
========

.. versionadded:: 1.0.0
   Initial release.

.. versionchanged:: 1.0.0
   Nothing has changed yet, but this is what it looks like.

.. deprecated:: 1.0.0
   And this is a deprecation.
