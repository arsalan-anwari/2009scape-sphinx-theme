# 2009scape Sphinx theme

[![PyPI](https://img.shields.io/pypi/v/sphinx-2009scape-theme?logo=pypi&logoColor=white&color=c8a145)](https://pypi.org/project/sphinx-2009scape-theme/)
[![Python](https://img.shields.io/pypi/pyversions/sphinx-2009scape-theme?logo=python&logoColor=white&color=c8a145)](https://pypi.org/project/sphinx-2009scape-theme/)
[![Sphinx](https://img.shields.io/badge/sphinx-%E2%89%A57.3-c8a145?logo=sphinx&logoColor=white)](https://www.sphinx-doc.org/)
[![Docs](https://img.shields.io/badge/docs-github%20pages-c8a145)](https://arsalan-anwari.github.io/2009scape-sphinx-theme/)
[![License](https://img.shields.io/badge/license-Apache--2.0-c8a145)](LICENSE)
[![Fonts](https://img.shields.io/badge/fonts-CC0--1.0-c8a145)](https://github.com/RuneStar/fonts)

A Sphinx theme that dresses documentation as a 2009-era RuneScape interface.
The design language is ported from
[`runescapecn`](https://github.com/alns0dev/runescapecn).

**[Live demo and full documentation →](https://arsalan-anwari.github.io/2009scape-sphinx-theme/)**

## Install

```console
$ pip install sphinx-2009scape-theme
```

```python
# docs/conf.py
html_theme = "2009scape"

html_theme_options = {
    "logo_text": "My Project",
    "github_url": "https://github.com/me/my-project",
}
```

That is the whole setup. The theme registers itself through a Sphinx entry
point, so it does not need to be listed in `extensions`.

## What you get

- **Layout**: sticky header, global-toctree sidebar with client-side
  collapsing, "on this page" scrollspy column, breadcrumbs, prev/next panels,
  mobile drawer navigation.
- **Content**: every docutils and Sphinx node styled: admonitions as interface
  panels with severity-coded edges, sunken code wells with copy buttons,
  bevelled tables, gold-edged API signatures, footnotes, glossaries, option
  lists, figures, search and index pages.
- **Fonts**: ten RuneScape faces from the CC0-licensed
  [RuneStar/fonts](https://github.com/RuneStar/fonts), bundled and served from
  the build output. No external requests at page load.
- **Highlighting**: a Pygments style matching runescapecn's code colours
  (keywords green, attributes and numbers cyan, strings yellow).
- **Tokens**: every colour, size and bevel is a CSS custom property, so the
  theme recolours from `conf.py` without forking a stylesheet.

The theme is dark by design, as the runescapecn registry is. A light palette can
be layered on through `css_variables`.

## Options

Full list with defaults in [`docs/configuration.rst`](docs/configuration.rst).
The ones most projects touch:

| Option | Default | What it does |
| --- | --- | --- |
| `logo_text` | `""` | Text beside the logo in the header |
| `logo_subtitle` | `""` | Small secondary line, e.g. a version tag |
| `github_url` / `discord_url` | `""` | Header icon links |
| `nav_links` | `[]` | Header links: `{"title": …, "doc": …}` or `{"title": …, "url": …}` |
| `announcement` | `""` | Gold banner above the header |
| `source_repository` | `""` | Enables the "Edit this page" link |
| `body_font` | `rs` | `rs`, `rs-quill`, `system`, … or a raw CSS stack |
| `base_font_size` | `20px` | Root font size |
| `scanlines` | `true` | Stone texture on panels |
| `pixelated_images` | `false` | `image-rendering: pixelated` on every image |
| `css_variables` | `{}` | Override any design token |

Pixel fonts are not ideal for long-form reading, so chrome and body copy can be
split and recolouring is a dict of tokens:

```python
html_theme_options = {
    "body_font": "system",      # readable paragraphs
    "heading_font": "rs-bold",  # RuneScape headings and interface labels
    "css_variables": {
        "rs-gold": "#7fd4ff",
        "rs-content-max-width": "52rem",
    },
}
```

Code blocks always default to a real monospace face; pixel fonts and code
indentation do not mix. The token list lives at the top of
[`static/css/2009scape.css`](src/sphinx_2009scape_theme/theme/2009scape/static/css/2009scape.css).

## Development

```console
$ git clone --recurse-submodules https://github.com/arsalan-anwari/2009scape-sphinx-theme
$ cd 2009scape-sphinx-theme
$ pip install -e .[docs,test]
$ make -C docs html          # build the demo docs
$ python -m pytest           # build-level tests
```

`docs/kitchen-sink/` renders every styled node type if a change breaks
something visually, it breaks there first.

Releases go out through [`publish.sh`](publish.sh), which runs the tests, uploads
to PyPI and pushes the built docs to GitHub Pages:

```console
$ ./publish.sh                # tests, PyPI, tag, gh-pages
$ ./publish.sh --docs-only    # just redeploy the docs
$ ./publish.sh --test-pypi    # dry run against TestPyPI
```

On the first run it also switches GitHub Pages on through the `gh` CLI, so the
repository needs no manual setup in the web UI.

## Licence

Theme code is Apache-2.0 (see [`LICENSE`](LICENSE)). The bundled RuneScape fonts
come from [RuneStar/fonts](https://github.com/RuneStar/fonts) and are CC0-1.0.

Not affiliated with Jagex or RuneScape. A developer tribute, inspired by the
game.
