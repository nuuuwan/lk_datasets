from pylatex.utils import NoEscape
from utils import File

from latex import Paragraph


class ArXivDocSectionAbstract:
    @staticmethod
    def fill_abstract(doc, version, global_summary):
        n_docs = global_summary["n_docs"]
        all_dataset_size_humanized = File.humanize_size(
            global_summary["all_dataset_size"]
        )
        n_datasets = global_summary["n_datasets"]

        doc.append(NoEscape(r"\begin{abstract}"))

        Paragraph(
            [
                "We present a collection of open, machine-readable document"
                + " datasets covering parliamentary proceedings,"
                + " legal judgments, government publications, news, and"
                + " tourism statistics from Sri Lanka.",
                "",
                f"As of {version},"
                + f" the collection currently comprises {n_docs:,} documents "
                + f"({all_dataset_size_humanized}) across"
                + f" {n_datasets} datasets "
                "in Sinhala, Tamil, and English,"
                + " updated daily and mirrored on GitHub and Hugging Face.",
                "",
                "These datasets aim to support research in computational"
                + " linguistics, legal analytics, socio-political studies,"
                + " and multilingual natural language processing.",
                "",
                "We describe the sources, collection pipeline,"
                + " formats, and potential use cases,"
                + " while discussing licensing and ethical considerations.",
            ]
        ).fill_doc(doc)
        doc.append(NoEscape(r"\end{abstract}"))
