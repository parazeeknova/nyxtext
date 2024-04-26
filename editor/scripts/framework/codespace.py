# Codespace :

import pygments.lexers
from chlorophyll import CodeView


class Codespace:
    def __init__(self, tab_view):
        self.codespace_init = tab_view.add("CodeSpace")
        self.tab_view = tab_view
        codeview = CodeView(
            self.codespace_init,
            lexer=pygments.lexers.PythonLexer,
            color_scheme="dracula",
        )
        codeview.pack(fill="both", expand=True)
