from pylatex.utils import NoEscape


class ArXivDocEnd:
    @staticmethod
    def fill_end(doc):
        doc.append(NoEscape(r"\bibliographystyle{acl_natbib}"))
        doc.append(NoEscape(r"\bibliography{latex/references}"))
