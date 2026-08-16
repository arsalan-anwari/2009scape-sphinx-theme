"""Sphinx configuration for the theme's own documentation."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

project = "2009scape Sphinx Theme"
copyright = "2026, Arsalan Anwari"
author = "Arsalan Anwari"
release = "1.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_2009scape_theme",
]

templates_path = []
exclude_patterns = ["_build"]
todo_include_todos = True

html_theme = "2009scape"
html_static_path = ["_static"]
html_title = "2009scape Theme"
html_short_title = "2009scape"

html_theme_options = {
    "logo_text": "2009scape",
    "logo_subtitle": "sphinx theme",
    "github_url": "https://github.com/arsalan-anwari/2009scape-sphinx-theme",
    "source_repository": "https://github.com/arsalan-anwari/2009scape-sphinx-theme",
    "source_branch": "main",
    "source_directory": "docs",
    "toc_title": "On this page",
    "footer_note": (
        "Not affiliated with Jagex or RuneScape. A developer tribute, "
        "inspired by the game."
    ),
    "nav_links": [
        {"title": "Kitchen sink", "doc": "kitchen-sink/index"},
    ],
}
