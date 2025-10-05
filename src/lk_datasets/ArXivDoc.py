import os

from pylatex import Command, Document, Itemize, Package, Section, Subsection
from pylatex.utils import NoEscape
from utils import File, Log

from latex import Cite, Paragraph
from lk_datasets.LKDatasetsGlobalReadMe import LKDatasetsGlobalReadMe
from utils_future import Latex

log = Log("ArXivDoc")


class ArXivDoc(File):
    PATH_PREFIX = os.path.join("latex", "arxiv")
    TEX_PATH = PATH_PREFIX + ".tex"
    PDF_PATH = PATH_PREFIX + ".pdf"

    def __init__(self):
        super().__init__(self.TEX_PATH)
        lk_datasets_global_readme = LKDatasetsGlobalReadMe()
        self.summary_list = lk_datasets_global_readme.summary_list
        self.global_summary = lk_datasets_global_readme.global_summary

    @staticmethod
    def fill_preamble(doc):

        doc.packages.append(Package("geometry", options="margin=1in"))
        doc.packages.append(Package("lmodern"))
        doc.packages.append(Package("fontenc", options="T1"))
        doc.packages.append(Package("inputenc", options="utf8"))
        doc.packages.append(Package("microtype"))
        doc.packages.append(Package("url"))
        doc.packages.append(Package("natbib", options="numbers"))
        doc.packages.append(Package("url"))
        doc.packages.append(Package("hyperref"))

        doc.preamble.append(
            Command(
                "title",
                "Sri Lanka Document Datasets:"
                + " A Large-Scale, Multilingual Resource for"
                + " Law, News, and Policy",
            )
        )
        email = "nuwans@alumni.stanford.edu"
        doc.preamble.append(
            Command(
                "author",
                NoEscape(
                    r"Nuwan I. Senaratna\\"
                    r"\vspace{0.25em}\texttt{\href{mailto:%s}{%s}}"
                    % (email, email)
                ),
            )
        )
        doc.preamble.append(Command("date", NoEscape(r"\today")))
        doc.append(NoEscape(r"\maketitle"))

    @staticmethod
    def fill_abstract(doc, global_summary):
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
                f"The collection currently comprises {n_docs:,} documents "
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

    @staticmethod
    def fill_section_introduction(doc):

        with doc.create(Section("Introduction")):
            Paragraph.fill_doc_from_list(
                doc,
                [
                    [
                        "Sri Lanka’s digital record of law, policy, and media is",
                        "fragmented across numerous government and private",
                        "sources. Much of this information exists as PDFs or web",
                        "pages, often lacking machine-readable structure or public",
                        "archival consistency. This fragmentation limits access for",
                        "citizens, journalists, and researchers interested in the",
                        "island’s governance, history, and socio-economic trends.",
                    ],
                    [
                        "The Sri Lanka Document Datasets initiative aims to bridge",
                        "this gap by collecting, cleaning, and organizing key public",
                        "documents into standardized, machine-readable formats.",
                        "It unifies diverse materials—from Hansards and court",
                        "judgements to news articles and tourism reports—under a",
                        "common data framework. All datasets are openly licensed",
                        "and continuously updated to ensure reproducibility and",
                        "public transparency.",
                    ],
                    [
                        "This effort is particularly significant for data-driven",
                        "research in low-resource contexts. By providing structured",
                        "data in Sinhala, Tamil, and English, the project supports",
                        "the development of natural language processing models,",
                        "cross-lingual studies, and digital humanities research.",
                        "The datasets also enable policy analysis, legal precedent",
                        "tracking, and media monitoring in a transparent, open",
                        "science environment.",
                    ],
                    [
                        "In this paper, we describe the scope and structure of these",
                        "datasets, outline the scraping and curation processes, and",
                        "highlight their potential applications in AI, governance,",
                        "and public knowledge. Our goal is to create a living data",
                        "archive that strengthens civic engagement and academic",
                        "research through open, verifiable information.",
                    ],
                ],
            )

    @staticmethod
    def fill_section_related_work(doc):

        with doc.create(Section("Related Work")):
            Paragraph.fill_doc_from_list(
                doc,
                [
                    [
                        "The study of open datasets has been central to the",
                        "development of natural language processing (NLP)",
                        "and computational social science. Large corpora such",
                        "as Common Crawl",
                        Cite("commoncrawl2020"),
                        ", Wikipedia",
                        "Dumps",
                        Cite("wikidumps2018"),
                        ", and OpenWebText",
                        Cite("openwebtext2019"),
                        "have powered models that",
                        "generalize across domains. However, these resources",
                        "are dominated by data from high-resource languages",
                        "and global institutions.",
                    ],
                    [
                        "Regional initiatives have sought to address this",
                        "imbalance by creating domain-specific collections.",
                        "Examples include the Indian Kanoon legal corpus",
                        Cite("indiankanoon2018"),
                        ", the OpenSubtitles",
                        "multilingual dataset",
                        Cite("opensubtitles2016"),
                        ", and the African News Corpus",
                        Cite("africannews2021"),
                        ". Such datasets have",
                        "improved representation for under-resourced",
                        "languages and enabled comparative linguistic",
                        "research.",
                    ],
                    [
                        "In South Asia, efforts remain scattered and often",
                        "focus on individual media outlets or institutions.",
                        "Sri Lanka, in particular, lacks consolidated and",
                        "machine-readable documentation of its public",
                        "records. Prior datasets were either limited in size,",
                        "language coverage, or temporal continuity",
                        Cite("sltalk2023"),
                        Cite("srilankanlp2022"),
                        ".",
                    ],
                    [
                        "The Sri Lanka Document Datasets aim to fill this gap",
                        "by aggregating diverse sources—parliamentary",
                        "debates, court judgements, gazettes, press releases,",
                        "and news—into a unified, open, and multilingual",
                        "repository. This complements global initiatives by",
                        "providing a structured view of a unique national",
                        "information ecosystem.",
                    ],
                ],
            )

    @staticmethod
    def fill_subsection_dataset(doc, summary):
        title = Latex.clean(summary["doc_class_label"]).title()
        description = Latex.clean(summary["doc_class_description"])
        with doc.create(Subsection(title)):
            doc.append(description)
            with doc.create(Itemize()) as itemize:
                itemize.add_item(
                    "Time Updated: " + f'{summary["time_updated"]}'
                )
                itemize.add_item(
                    "Number of Documents: " + f'{summary["n_docs"]:,}'
                )
                itemize.add_item(
                    "Date Range: "
                    + f'{summary["date_str_min"]} to {summary["date_str_max"]}'
                )
                itemize.add_item(
                    "Dataset Size: "
                    + f'{File.humanize_size(summary["dataset_size"])}'
                )

    @staticmethod
    def fill_section_datasets(doc, summary_list):
        with doc.create(Section("Datasets")):
            for summary in summary_list:
                ArXivDoc.fill_subsection_dataset(doc, summary)

    @staticmethod
    def fill_section_data_collection_pipeline(doc):
        with doc.create(Section("Data Collection Pipeline")):
            Paragraph.fill_doc_from_list(
                doc,
                [
                    [
                        "Data Collection Pipeline",
                        "Our pipeline is automated, reproducible, and",
                        "resilient. It continuously discovers, ingests,",
                        "parses, validates, and versions documents from",
                        "official Sri Lankan sources.",
                        Cite("MLOpsSurvey2022"),
                    ],
                    [
                        "GitHub Actions orchestrates the workflow.",
                        "Cron jobs run several times per day, per",
                        "dataset. A matrix strategy isolates each source,",
                        "allowing independent retries without blocking",
                        "others. Secrets manage tokens; caches speed I/O.",
                        Cite("GitHubActions2023"),
                    ],
                    [
                        "Each run is idempotent and incremental.",
                        "Before crawling, we load a manifest of known",
                        "items. New or changed items are detected by",
                        "stable keys (URL + date) and content hashes.",
                        "Only deltas are committed to the repository.",
                        Cite("ReproducibleResearch2017"),
                    ],
                    [
                        "Crawling is implemented in Python with",
                        "Selenium in headless Chromium.",
                        "We wait for dynamic content via explicit",
                        "conditions (e.g., presence of selectors),",
                        "handle pagination, and capture canonical URLs.",
                        Cite("Selenium2023"),
                    ],
                    [
                        "Politeness is enforced. We respect robots.txt,",
                        "throttle requests, randomize delays, and apply",
                        "exponential backoff on transient failures.",
                        "Errors are logged and surfaced in the Actions",
                        "summary for rapid triage.",
                        Cite("WebCrawlingBestPractices2021"),
                    ],
                    [
                        "Raw artifacts are preserved alongside parsed",
                        "representations. For each document we store",
                        "the fetched HTML or PDF, plus normalized JSON",
                        "with metadata (title, date, source, language,",
                        "hashes) to enable downstream reproducibility.",
                        Cite("DataVersioning2020"),
                    ],
                    [
                        "PDF parsing uses PyMuPDF (fitz). For each PDF,",
                        "we extract text, metadata, and layout blocks,",
                        "retain page boundaries, and normalize Unicode.",
                        "When images contain embedded text, PyMuPDF’s",
                        "text extraction captures vector text regions.",
                        Cite("PyMuPDF2024"),
                    ],
                    [
                        "The parser records coordinates for blocks,",
                        "allowing approximate structure recovery",
                        "(sections, headings, tables) where present.",
                        "Heuristics join hyphenated lines and",
                        "preserve numbering and legal citations.",
                        Cite("DocumentLayoutAnalysis2021"),
                    ],
                    [
                        "Quality gates run in CI. Schemas are validated,",
                        "required fields are enforced, and checksums",
                        "guard against corruption. Unit tests cover",
                        "fetching, parsing, and serialization, and",
                        "fail the job on regressions.",
                        Cite("DataQuality2022"),
                    ],
                    [
                        "Historical coverage was built via a",
                        "back-population pipeline. We iterate over",
                        "archival indexes and date ranges, enqueue",
                        "jobs in batches, checkpoint progress, and",
                        "resume safely after interruptions.",
                        Cite("HistoricalWebData2019"),
                    ],
                    [
                        "Transparency is prioritized. Run metadata,",
                        "document counts, and last-updated timestamps",
                        "are published to README badges. Commit",
                        "messages summarize deltas, enabling clear,",
                        "auditable provenance across releases.",
                        Cite("OpenDataPractices2020"),
                    ],
                ],
            )

    @staticmethod
    def fill_end(doc):
        doc.append(NoEscape("\\bibliographystyle{plainnat}"))
        doc.append(NoEscape("\\bibliography{latex/references}"))

    def build_with_pylatex(self):
        doc = Document(documentclass="article")

        self.fill_preamble(doc)
        self.fill_abstract(doc, self.global_summary)

        self.fill_section_introduction(doc)
        self.fill_section_related_work(doc)

        self.fill_section_datasets(doc, self.summary_list)

        self.fill_section_data_collection_pipeline(doc)
        doc.create(Section("Licensing and Access"))
        doc.create(Section("Conclusion and Future Work"))

        self.fill_end(doc)

        doc.generate_tex(self.PATH_PREFIX)
        assert os.path.exists(self.TEX_PATH)
        log.info(f"Wrote {File(self.TEX_PATH)}")

        doc.generate_pdf(self.PATH_PREFIX, clean=False)
        os.system(f"bibtex {self.PATH_PREFIX}")
        doc.generate_pdf(self.PATH_PREFIX, clean=False)
        doc.generate_pdf(self.PATH_PREFIX, clean=True, clean_tex=False)
        assert os.path.exists(self.PDF_PATH)
        log.info(f"Generated {File(self.PDF_PATH)}")
        log.info(f"Generated {File(self.PDF_PATH)}")
