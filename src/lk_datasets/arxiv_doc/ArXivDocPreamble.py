from pylatex import Command, Package
from pylatex.utils import NoEscape


class ArXivDocPreamble:
    @staticmethod
    def fill_preamble(doc, version):

        # ACL-compatible setup
        doc.packages.append(Package("times"))
        doc.packages.append(Package("textcomp"))
        doc.packages.append(Package("lastpage"))
        doc.packages.append(Package("hyperref"))
        doc.packages.append(Package("acl"))

        doc.preamble.append(
            Command(
                "title",
                "Sri Lanka Document Datasets:"
                + " A Large-Scale, Multilingual Resource for"
                + f" Law, News, and Policy ({version})",
            )
        )
        email = "nuwans@alumni.stanford.edu"
        doc.preamble.append(
            Command(
                "author",
                NoEscape(
                    r"Nuwan I. Senaratna\\"
                    r"Independent Researcher\\"
                    r"\vspace{0.25em}\texttt{\href{mailto:%s}{%s}}"
                    % (email, email)
                ),
            )
        )
        doc.preamble.append(Command("date", NoEscape(r"\today")))
        doc.append(NoEscape(r"\maketitle"))
