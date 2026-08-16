"""Pygments styles matching the 2009scape palette.

The colour choices mirror ``src/components/code-block.tsx`` in the runescapecn
reference implementation: tags/keywords are RuneScape green, attributes cyan,
strings yellow, comments grey-italic and plain text the familiar interface
orange.
"""

from __future__ import annotations

from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Token,
    Whitespace,
)

GOLD = "#c9a961"
ORANGE = "#ff981f"
YELLOW = "#ffeb3b"
GREEN = "#00ff00"
CYAN = "#00ffff"
RED = "#ff0000"
GREY = "#7a7a7a"
WHITE = "#ffffff"
CODE_BG = "#111111"


class Scape2009Style(Style):
    """Dark code highlighting for the 2009scape theme."""

    name = "2009scape"

    background_color = CODE_BG
    highlight_color = "#3a3320"
    line_number_color = GREY
    line_number_background_color = "#0b0b0b"
    line_number_special_color = "#000000"
    line_number_special_background_color = GOLD

    styles = {
        Token: ORANGE,
        Text: ORANGE,
        Whitespace: "",
        Error: f"bg:#3a0000 {RED}",
        Other: ORANGE,

        Comment: f"italic {GREY}",
        Comment.Preproc: f"noitalic {GREEN}",
        Comment.Special: f"italic bold {GOLD}",

        Keyword: f"bold {GREEN}",
        Keyword.Constant: f"bold {CYAN}",
        Keyword.Pseudo: f"nobold {GREEN}",
        Keyword.Type: f"nobold {GOLD}",

        Operator: GREY,
        Operator.Word: f"bold {GREEN}",
        Punctuation: GREY,

        Name: ORANGE,
        Name.Attribute: CYAN,
        Name.Builtin: GREEN,
        Name.Builtin.Pseudo: f"italic {GREEN}",
        Name.Class: f"bold {GOLD}",
        Name.Constant: CYAN,
        Name.Decorator: f"bold {YELLOW}",
        Name.Entity: CYAN,
        Name.Exception: f"bold {RED}",
        Name.Function: GOLD,
        Name.Function.Magic: f"bold {GOLD}",
        Name.Label: CYAN,
        Name.Namespace: f"bold {GOLD}",
        Name.Tag: f"bold {GREEN}",
        Name.Variable: ORANGE,
        Name.Variable.Magic: f"bold {ORANGE}",

        Literal: YELLOW,
        String: YELLOW,
        String.Doc: f"italic {GREY}",
        String.Escape: f"bold {CYAN}",
        String.Interpol: f"bold {CYAN}",
        String.Regex: CYAN,
        String.Symbol: CYAN,

        Number: CYAN,

        Generic.Deleted: f"bg:#2a0000 {RED}",
        Generic.Emph: "italic",
        Generic.Error: RED,
        Generic.Heading: f"bold {GOLD}",
        Generic.Inserted: f"bg:#002a00 {GREEN}",
        Generic.Output: GREY,
        Generic.Prompt: f"bold {GREEN}",
        Generic.Strong: "bold",
        Generic.Subheading: f"bold {GOLD}",
        Generic.Traceback: RED,
    }


class Scape2009LightStyle(Style):
    """Parchment-toned variant, used when a light Pygments style is requested.

    The theme itself is dark by design, but Sphinx asks for a ``default``
    Pygments style when a page is rendered with a light user agent stylesheet
    (and some extensions render snippets on a pale surface).
    """

    name = "2009scape-light"

    background_color = "#e8dcc0"
    highlight_color = "#d3c298"
    line_number_color = "#6b5a3a"

    styles = {
        Token: "#2a2118",
        Text: "#2a2118",
        Whitespace: "",
        Error: "bg:#f0c0c0 #8b0000",
        Other: "#2a2118",

        Comment: "italic #6b5a3a",
        Comment.Preproc: "noitalic #1f6b1f",
        Comment.Special: "italic bold #6b4a10",

        Keyword: "bold #1f6b1f",
        Keyword.Constant: "bold #0f5f6b",
        Keyword.Pseudo: "nobold #1f6b1f",
        Keyword.Type: "nobold #7a5a10",

        Operator: "#5a4a35",
        Operator.Word: "bold #1f6b1f",
        Punctuation: "#5a4a35",

        Name: "#2a2118",
        Name.Attribute: "#0f5f6b",
        Name.Builtin: "#1f6b1f",
        Name.Class: "bold #7a5a10",
        Name.Constant: "#0f5f6b",
        Name.Decorator: "bold #8a6a00",
        Name.Exception: "bold #8b0000",
        Name.Function: "#7a5a10",
        Name.Namespace: "bold #7a5a10",
        Name.Tag: "bold #1f6b1f",
        Name.Variable: "#2a2118",

        Literal: "#8a6a00",
        String: "#8a6a00",
        String.Doc: "italic #6b5a3a",
        String.Escape: "bold #0f5f6b",
        String.Interpol: "bold #0f5f6b",
        String.Regex: "#0f5f6b",
        String.Symbol: "#0f5f6b",

        Number: "#0f5f6b",

        Generic.Deleted: "bg:#f0c0c0 #8b0000",
        Generic.Emph: "italic",
        Generic.Error: "#8b0000",
        Generic.Heading: "bold #7a5a10",
        Generic.Inserted: "bg:#c0e8c0 #1f6b1f",
        Generic.Output: "#6b5a3a",
        Generic.Prompt: "bold #1f6b1f",
        Generic.Strong: "bold",
        Generic.Subheading: "bold #7a5a10",
        Generic.Traceback: "#8b0000",
    }
