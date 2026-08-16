================
Tables and lists
================

Tables
======

Header rows are gold on near-black; body cells take interface orange and
highlight on hover.

.. list-table:: Smithing requirements
   :header-rows: 1
   :widths: 25 15 25 35

   * - Bar
     - Level
     - Ore
     - Notes
   * - Bronze
     - 1
     - Copper + tin
     - The first bar anyone smelts.
   * - Iron
     - 15
     - Iron
     - 50% success rate without a ring of forging.
   * - Steel
     - 30
     - Iron + 2 coal
     - The bread and butter of mid-level smithing.
   * - Mithril
     - 50
     - Mithril + 4 coal
     - Slow, but profitable.

A grid table, with a caption and a stub column:

.. table:: Combat triangle
   :widths: auto

   +----------+------------+------------+
   | Style    | Strong vs. | Weak vs.   |
   +==========+============+============+
   | Melee    | Ranged     | Magic      |
   +----------+------------+------------+
   | Ranged   | Magic      | Melee      |
   +----------+------------+------------+
   | Magic    | Melee      | Ranged     |
   +----------+------------+------------+

A deliberately wide table, to confirm it scrolls inside its own container
rather than pushing the page sideways:

.. list-table::
   :header-rows: 1

   * - Column one
     - Column two
     - Column three
     - Column four
     - Column five
     - Column six
     - Column seven
     - Column eight
   * - ``value_one``
     - ``value_two``
     - ``value_three``
     - ``value_four``
     - ``value_five``
     - ``value_six``
     - ``value_seven``
     - ``value_eight``

Lists
=====

Bulleted lists use a gold pixel square, nested levels a hollow one:

- Woodcutting

  - Normal logs
  - Oak logs

    - Requires level 15

- Fishing
- Firemaking

Numbered:

#. Chop the logs.
#. Light them.
#. Repeat 12,000 times.

Option lists:

-h, --help       Show this message and exit.
-b BUILDER       Choose the Sphinx builder.
--keep-going     Do not stop on the first warning.

Definition list with classifiers:

term : classifier
    A definition list entry that carries a classifier.

Hlists
======

.. hlist::
   :columns: 3

   * Attack
   * Strength
   * Defence
   * Ranged
   * Prayer
   * Magic
   * Runecrafting
   * Construction
   * Hitpoints

Glossary
========

.. glossary::

   GE
      The Grand Exchange. Did not exist in 2009-era gameplay for long,
      but it does here.

   Tick
      600 milliseconds. The unit every mechanic is measured in.

Referencing a :term:`Tick` links back into the glossary.
