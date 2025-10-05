from pylatex import Command, NoEscape


class Footnote(Command):
    def __init__(self, footnote_text):
        super().__init__(
            "footnote",
            arguments=NoEscape(
                f"\\href{{{footnote_text}}}{{{footnote_text}}}"
            ),
        )
