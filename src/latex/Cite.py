from pylatex import Command


class Cite(Command):
    def __init__(self, citation_key):
        super().__init__("cite", arguments=citation_key)
