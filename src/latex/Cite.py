from pylatex import Command


class Cite(Command):
    def __init__(self, citation_key):
        super().__init__("citep", arguments=citation_key)
