from pylatex import NewLine

from latex.Cite import Cite


class Paragraph:
    def __init__(self, items):
        assert isinstance(items, list)
        assert isinstance(
            items[0], (str, Cite)
        ), f"Invalid item type: {type(items[0])}"
        self.items = items

    def fill_doc(self, doc):
        str_items = []
        for item in self.items:
            if isinstance(item, str):
                str_items.append(item)
            else:
                doc.append(" ".join(str_items))
                str_items = []
                doc.append(item)
        if str_items:
            doc.append(" ".join(str_items))
        doc.append(NewLine())
        doc.append(NewLine())

    @staticmethod
    def fill_doc_from_list(doc, items_list):
        for items in items_list:
            Paragraph(items).fill_doc(doc)
