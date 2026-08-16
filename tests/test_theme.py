"""Build-level tests for the 2009scape theme."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from sphinx.application import Sphinx

CONF = """
project = "Test"
copyright = "2026, Test"
extensions = ["sphinx_2009scape_theme"]
html_theme = "2009scape"
html_theme_options = {options}
"""

INDEX = """
Title
=====

Intro paragraph with ``literal`` text.

.. note::

   A note.

.. code-block:: python

   value = 1

.. toctree::

   page
"""

PAGE = """
Second page
===========

Section
-------

Body text.
"""


def build(tmp_path: Path, options: str = "{}") -> str:
    """Build a two-page project and return the rendered ``page.html``."""
    src = tmp_path / "src"
    src.mkdir()
    (src / "conf.py").write_text(CONF.format(options=options), encoding="utf-8")
    (src / "index.rst").write_text(INDEX, encoding="utf-8")
    (src / "page.rst").write_text(PAGE, encoding="utf-8")

    out = tmp_path / "out"
    app = Sphinx(
        srcdir=str(src),
        confdir=str(src),
        outdir=str(out),
        doctreedir=str(tmp_path / "doctrees"),
        buildername="html",
        warningiserror=True,
    )
    app.build()
    return (out / "page.html").read_text(encoding="utf-8")


def test_builds_without_warnings(tmp_path: Path) -> None:
    assert "<title>" in build(tmp_path)


def test_page_chrome_is_present(tmp_path: Path) -> None:
    html = build(tmp_path)

    for marker in (
        'class="rs-header"',
        'class="rs-sidebar"',
        'class="rs-main"',
        'class="rs-toc"',
        'class="rs-footer"',
        "data-rs-globaltoc",
        "js/2009scape.js",
    ):
        assert marker in html, f"missing {marker}"


def test_breadcrumbs_and_prev_next(tmp_path: Path) -> None:
    html = build(tmp_path)

    assert 'class="rs-breadcrumbs"' in html
    assert 'class="rs-page-nav"' in html
    assert "rs-page-nav__link--prev" in html


def test_stylesheets_are_linked(tmp_path: Path) -> None:
    html = build(tmp_path)

    for sheet in ("css/fonts.css", "css/2009scape.css", "css/layout.css", "css/content.css"):
        assert sheet in html, f"missing {sheet}"


def test_fonts_are_copied(tmp_path: Path) -> None:
    build(tmp_path)
    fonts = tmp_path / "out" / "_static" / "fonts"

    assert (fonts / "otf" / "RuneScape-Plain-12.otf").exists()
    assert (fonts / "ttf" / "RuneScape-Plain-12.ttf").exists()


def test_pygments_style_is_ours(tmp_path: Path) -> None:
    build(tmp_path)
    pygments_css = (tmp_path / "out" / "_static" / "pygments.css").read_text(
        encoding="utf-8"
    )

    assert ".highlight { background: #111111" in pygments_css
    assert "#0f0" in pygments_css.lower()


def test_css_variable_overrides_are_injected(tmp_path: Path) -> None:
    html = build(tmp_path, options='{"css_variables": {"rs-gold": "#123456"}}')

    style = re.search(r"<style>(.*?)</style>", html, re.S)
    assert style is not None
    assert "--rs-gold: #123456;" in style.group(1)


def test_body_font_alias_resolves_to_a_stack(tmp_path: Path) -> None:
    html = build(tmp_path, options='{"body_font": "system"}')

    assert "--rs-font-body: system-ui" in html
    assert "--rs-font-smoothing: antialiased;" in html


def test_base_font_size_accepts_bare_numbers(tmp_path: Path) -> None:
    html = build(tmp_path, options='{"base_font_size": "17"}')

    assert "--rs-font-size-base: 17px;" in html


def test_toggles_reach_the_body_element(tmp_path: Path) -> None:
    html = build(tmp_path, options='{"scanlines": False, "pixelated_images": True}')

    assert 'data-rs-scanlines="false"' in html
    assert 'data-rs-pixelated-images="true"' in html


def test_toc_can_be_disabled(tmp_path: Path) -> None:
    html = build(tmp_path, options='{"show_toc": False}')

    assert "rs-page--no-toc" in html
    assert 'class="rs-toc"' not in html


def test_edit_this_page_url(tmp_path: Path) -> None:
    html = build(
        tmp_path,
        options=(
            '{"source_repository": "https://github.com/me/proj", '
            '"source_branch": "trunk", "source_directory": "docs"}'
        ),
    )

    assert "https://github.com/me/proj/blob/trunk/docs/page.rst" in html


def test_css_variables_rejects_a_non_mapping(tmp_path: Path) -> None:
    from sphinx.errors import ExtensionError

    with pytest.raises((ExtensionError, Exception)):
        build(tmp_path, options='{"css_variables": ["not", "a", "mapping"]}')
