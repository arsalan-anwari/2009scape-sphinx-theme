"""A Sphinx theme with the look and feel of 2009-era RuneScape.

The visual language (palette, pixel fonts, bevelled borders, stone panels) is
ported from the ``runescapecn`` shadcn registry, which is vendored under
``vendor/runescapecn`` in this repository for reference.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from sphinx.errors import ExtensionError

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

__version__ = "1.0.1"
__all__ = ["__version__", "setup"]

THEME_PATH = (Path(__file__).parent / "theme" / "2009scape").resolve()

_CSS_VARIABLE_OPTIONS = ("css_variables",)

FONT_STACKS = {
    "rs": "'RuneScape Plain 12', 'RuneScape Plain 11', monospace",
    "rs-bold": "'RuneScape Bold 12', 'RuneScape Plain 12', monospace",
    "rs-quill": "'RuneScape Quill', 'RuneScape Quill 8', serif",
    "rs-quill-caps": "'RuneScape Quill Caps', 'RuneScape Quill', serif",
    "rs-surok": "'RuneScape Surok', serif",
    "rs-barbarian": "'RuneScape Barbarian Assault', sans-serif",
    "rs-fairy": "'RuneScape Fairy Large', 'RuneScape Fairy', serif",
    "system": (
        "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', "
        "Arial, sans-serif"
    ),
}


def _resolve_font(value: str) -> str:
    """Map a font alias to a CSS font stack, passing through raw stacks."""
    value = (value or "").strip()
    if not value:
        return ""
    return FONT_STACKS.get(value, value)


def _css_variable_block(variables: dict[str, str]) -> str:
    """Render a mapping into the body of a CSS rule."""
    declarations = []
    for name, value in variables.items():
        name = name.strip()
        if not name.startswith("--"):
            name = f"--{name}"
        declarations.append(f"    {name}: {value};")
    return "\n".join(declarations)


def _edit_page_url(app: Sphinx, pagename: str, context: dict[str, Any]) -> str:
    """Build a "view/edit this page" URL from the ``source_*`` theme options."""
    options = app.builder.theme_options if app.builder else {}
    repository = str(options.get("source_repository", "") or "").rstrip("/")
    if not repository:
        return ""

    branch = str(options.get("source_branch", "") or "main")
    directory = str(options.get("source_directory", "") or "").strip("/")
    suffix = context.get("page_source_suffix") or ".rst"

    path = f"{pagename}{suffix}"
    if directory:
        path = f"{directory}/{path}"

    if "github.com" in repository:
        return f"{repository}/blob/{branch}/{path}"
    if "gitlab" in repository:
        return f"{repository}/-/blob/{branch}/{path}"
    return f"{repository}/{branch}/{path}"


def _update_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> None:
    """Expose derived values (fonts, CSS overrides, edit URL) to templates."""
    options = app.builder.theme_options if app.builder else {}

    overrides: dict[str, str] = {}
    for option in _CSS_VARIABLE_OPTIONS:
        value = options.get(option) or {}
        if isinstance(value, str):
            value = {}
        if not isinstance(value, dict):
            msg = (
                f"html_theme_options[{option!r}] must be a mapping of CSS "
                f"custom properties, got {type(value).__name__}."
            )
            raise ExtensionError(msg)
        overrides.update(value)

    for option, variable in (
        ("body_font", "--rs-font-body"),
        ("heading_font", "--rs-font-heading"),
        ("mono_font", "--rs-font-mono"),
    ):
        stack = _resolve_font(str(options.get(option, "") or ""))
        if stack:
            overrides[variable] = stack

    body_font = str(options.get("body_font", "") or "").strip()
    if body_font and not body_font.startswith("rs"):
        overrides.setdefault("--rs-font-smoothing", "antialiased")

    base_size = str(options.get("base_font_size", "") or "").strip()
    if base_size:
        if base_size.isdigit():
            base_size = f"{base_size}px"
        overrides["--rs-font-size-base"] = base_size

    context["rs_css_overrides"] = _css_variable_block(overrides)
    context["rs_edit_page_url"] = _edit_page_url(app, pagename, context)
    context["rs_theme_version"] = __version__


def _add_assets(app: Sphinx) -> None:
    """Register the theme's JavaScript, but only when the theme is in use."""
    if app.config.html_theme != "2009scape":
        return
    app.add_js_file("js/2009scape.js", loading_method="defer")


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("7.3")
    app.add_html_theme("2009scape", str(THEME_PATH))
    app.connect("builder-inited", _add_assets)
    app.connect("html-page-context", _update_context)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
