import os
import shutil

from pylatex import Document
from utils import File, Log, Time, TimeFormat

from lk_datasets.arxiv_doc.ArXivDocEnd import ArXivDocEnd
from lk_datasets.arxiv_doc.ArXivDocPreamble import ArXivDocPreamble
from lk_datasets.arxiv_doc.ArXivDocSection0Abstract import (
    ArXivDocSection0Abstract,
)
from lk_datasets.arxiv_doc.ArXivDocSection1Introduction import (
    ArXivDocSection1Introduction,
)
from lk_datasets.arxiv_doc.ArXivDocSection2RelatedWork import (
    ArXivDocSection2RelatedWork,
)
from lk_datasets.arxiv_doc.ArXivDocSection3Datasets import (
    ArXivDocSection3Datasets,
)
from lk_datasets.arxiv_doc.ArXivDocSection4DataCollectionPipeline import (
    ArXivDocSection4DataCollectionPipeline,
)
from lk_datasets.arxiv_doc.ArXivDocSection5LicensingAndAccess import (
    ArXivDocSection5LicensingAndAccess,
)
from lk_datasets.arxiv_doc.ArXivDocSection6ConclusionAndFutureWork import (
    ArXivDocSection6ConclusionAndFutureWork,
)
from lk_datasets.LKDatasetsGlobalReadMe import LKDatasetsGlobalReadMe

log = Log("ArXivDoc")


class ArXivDoc(
    ArXivDocPreamble,
    ArXivDocSection0Abstract,
    ArXivDocSection1Introduction,
    ArXivDocSection2RelatedWork,
    ArXivDocSection3Datasets,
    ArXivDocSection4DataCollectionPipeline,
    ArXivDocSection5LicensingAndAccess,
    ArXivDocSection6ConclusionAndFutureWork,
    ArXivDocEnd,
):
    DOC_ID = "lk_datasets"
    PATH_PREFIX = os.path.join("latex", DOC_ID)
    TEX_PATH = PATH_PREFIX + ".tex"
    PDF_PATH = PATH_PREFIX + ".pdf"

    def __init__(self):
        lk_datasets_global_readme = LKDatasetsGlobalReadMe()
        self.summary_list = lk_datasets_global_readme.summary_list
        self.global_summary = lk_datasets_global_readme.global_summary
        self.version = TimeFormat("v%Y%m%d").format(Time.now())

    def build(self):
        doc = Document(
            documentclass="article",
            document_options=["10pt", "a4paper"],
        )

        self.fill_preamble(doc, self.version)
        self.fill_abstract(doc, self.version, self.global_summary)

        self.fill_section_introduction(doc)
        self.fill_section_related_work(doc)

        self.fill_section_datasets(doc, self.version, self.summary_list)

        self.fill_section_data_collection_pipeline(doc)
        self.fill_section_licensing_and_access(doc)
        self.fill_section_conclusion_and_future_work(doc)

        self.fill_end(doc)

        doc.generate_tex(self.PATH_PREFIX)
        assert os.path.exists(self.TEX_PATH)
        log.info(f"Wrote {File(self.TEX_PATH)}")

        shutil.copy(
            os.path.join("latex", "references.bib"),
            os.path.join(self.PATH_PREFIX + ".bib"),
        )
        doc.generate_pdf(self.PATH_PREFIX, clean=False)
        os.system(f"bibtex {self.PATH_PREFIX}")
        doc.generate_pdf(self.PATH_PREFIX, clean=False)
        doc.generate_pdf(self.PATH_PREFIX, clean=True, clean_tex=False)
        assert os.path.exists(self.PDF_PATH)
        log.info(f"Generated {File(self.PDF_PATH)}")
