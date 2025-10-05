from pylatex import Enumerate, Section
from pylatex.utils import NoEscape, bold, italic
from utils import File

from utils_future import Latex


class ArXivDocSectionDatasets:

    @staticmethod
    def fill_subsection_dataset(enumer, summary):
        title = Latex.clean(summary["doc_class_label"]).title()
        description = Latex.clean(summary["doc_class_description"])
        n_docs = summary["n_docs"]
        dataset_size_humanized = File.humanize_size(summary["dataset_size"])
        date_str_min = summary["date_str_min"]
        date_str_max = summary["date_str_max"]
        url_source_list = summary.get("url_source_list", [])
        if len(url_source_list) == 1:
            url_source = url_source_list[0]
            url_source = f"\\href{{{url_source}}}{{{url_source}}}"

        else:
            url_source = "multiple sources"
        url_data = summary["url_data"]
        url_data = url_data.replace("_", r"\_")
        url_data_label = summary["doc_class_label"].replace("_", "\\_")
        data_link = f"\\href{{{url_data}}}{{{url_data_label}}}"

        enumer.add_item(
            NoEscape(
                bold(title)
                + ": "
                + description
                + italic(
                    f" {n_docs:,} documents,"
                    + f" {dataset_size_humanized},"
                    + f" from {date_str_min} to {date_str_max}."
                )
                + f" Source: {url_source}."
                + f" Dataset: {data_link}."
            )
        )

    @staticmethod
    def fill_section_datasets(doc, version, summary_list):
        n = len(summary_list)
        with doc.create(Section("Datasets")):
            doc.append(
                f"As of {version}, Sri Lanka Document Datasets"
                + f" consists of {n} datasets."
            )
            with doc.create(Enumerate()) as enumer:
                for summary in summary_list:
                    ArXivDocSectionDatasets.fill_subsection_dataset(
                        enumer, summary
                    )
