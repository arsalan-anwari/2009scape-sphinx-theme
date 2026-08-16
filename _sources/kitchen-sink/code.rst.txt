====
Code
====

Code blocks are sunken wells with a copy button that appears on hover. The
Pygments palette follows the runescapecn code sample colours: keywords green,
attributes and numbers cyan, strings yellow, comments grey.

Python
======

.. code-block:: python

   from dataclasses import dataclass


   @dataclass
   class Player:
       """A logged-in account."""

       name: str
       combat_level: int = 3

       def greet(self) -> str:
           # Welcome message shown on login.
           return f"Welcome to 2009scape, {self.name}!"

With line numbers and an emphasised line:

.. code-block:: python
   :linenos:
   :emphasize-lines: 3

   def smelt(ore, coal=0):
       if ore == "iron" and coal == 0:
           raise ValueError("iron needs coal")
       return f"{ore} bar"

With a caption:

.. code-block:: javascript
   :caption: static/js/login.js

   const login = async (username, password) => {
     const response = await fetch("/api/login", {
       method: "POST",
       body: JSON.stringify({ username, password }),
     });
     return response.json();
   };

Other languages
===============

.. code-block:: console

   $ sphinx-build -b html docs docs/_build/html

.. code-block:: yaml

   theme:
     name: 2009scape
     options:
       logo_text: My Project
       scanlines: true

.. code-block:: diff

     html_theme = "alabaster"
   - html_theme = "alabaster"
   + html_theme = "2009scape"

.. code-block:: html

   <div class="rs-panel">
     <p class="rs-badge">Members</p>
   </div>

Literal blocks
==============

A plain literal block, introduced with a double colon::

   Woodcutting  99
   Fishing      99
   Firemaking   99

Doctest
=======

.. doctest::

   >>> from sphinx_2009scape_theme import __version__
   >>> __version__
   '1.0.0'

Parsed literals
===============

.. parsed-literal::

   $ pip install sphinx-2009scape-theme==\ |release|
