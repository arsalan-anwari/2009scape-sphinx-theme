===========
Admonitions
===========

Admonitions are RuneScape interface panels: a black border, a bevelled stone
face, a title bar and a coloured left edge that encodes severity.

Informational
=============

.. note::

   Notes are cyan, the colour the game uses for system messages.

.. seealso::

   :doc:`../configuration` covers every theme option.

.. hint::

   Hints and tips share the green accent.

.. tip::

   Press ``/`` anywhere to jump to the search box.

.. important::

   Important notices take the gold accent.

Warnings
========

.. attention::

   Attention, caution and warning all use the yellow edge.

.. caution::

   Mind the gap between the bank and the furnace.

.. warning::

   Wilderness beyond this point. Bring nothing you cannot lose.

Failures
========

.. error::

   Errors and dangers take the red edge.

.. danger::

   You will be dealt damage.

Generic and to-do
=================

.. admonition:: Custom title

   An ``.. admonition::`` with its own title falls back to the gold accent.

.. todo::

   The ``sphinx.ext.todo`` directive is styled too.

Nested content
==============

.. warning::

   Admonitions hold arbitrary content:

   .. code-block:: python

      raise RuntimeError("out of runes")

   - Including lists,
   - and tables:

   .. list-table::
      :header-rows: 1

      * - Rune
        - Cost
      * - Air
        - 5 gp
      * - Blood
        - 400 gp
