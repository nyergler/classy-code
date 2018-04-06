import sphinx.highlighting
import classycode.directives

from . import formatter


def setup(app):

    app.add_directive('classy-code-block', classycode.directives.CodeBlock)
    app.add_directive('classy-literalinclude', classycode.directives.LiteralInclude)

    sphinx.highlighting.PygmentsBridge.html_formatter = \
        formatter.HtmlFormatter
