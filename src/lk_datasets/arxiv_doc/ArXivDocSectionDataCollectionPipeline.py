from pylatex import Section

from latex import Cite, Footnote, Paragraph

PARAGRAPH_ITEMS = [
    [
        "Our pipeline is automated, reproducible, and",
        "resilient. It continuously discovers, ingests,",
        "parses, validates, and versions documents from",
        "official Sri Lankan sources",
        Cite("MLOpsSurvey2022"),
        ".",
    ],
    [
        "GitHub Actions orchestrates the workflow.",
        "Cron jobs run several times per day, per",
        "dataset. A matrix strategy isolates each source,",
        "allowing independent retries without blocking",
        "others. Secrets manage tokens; caches speed I/O",
        Footnote("https://docs.github.com/actions"),
        ".",
    ],
    [
        "Each run is idempotent and incremental.",
        "Before crawling, we load a manifest of known",
        "items. New or changed items are detected by",
        "stable keys (URL + date) and content hashes.",
        "Only deltas are committed to the repository",
        Cite("ReproducibleResearch2017"),
        ".",
    ],
    [
        "Crawling is implemented in Python with",
        "Selenium in headless Chromium.",
        "We wait for dynamic content via explicit",
        "conditions (e.g., presence of selectors),",
        "handle pagination, and capture canonical URLs",
        Footnote("https://www.selenium.dev/documentation/"),
        ".",
    ],
    [
        "Politeness is enforced. We respect robots.txt,",
        "throttle requests, randomize delays, and apply",
        "exponential backoff on transient failures.",
        "Errors are logged and surfaced in the Actions",
        "summary for rapid triage",
        Cite("WebCrawlingBestPractices2021"),
        ".",
    ],
    [
        "Raw artifacts are preserved alongside parsed",
        "representations. For each document we store",
        "the fetched HTML or PDF, plus normalized JSON",
        "with metadata (title, date, source, language,",
        "hashes) to enable downstream reproducibility",
        Cite("DataVersioning2020"),
        ".",
    ],
    [
        "PDF parsing uses PyMuPDF (fitz). For each PDF,",
        "we extract text, metadata, and layout blocks,",
        "retain page boundaries, and normalize Unicode.",
        "When images contain embedded text, PyMuPDF’s",
        "text extraction captures vector text regions",
        Footnote("https://pymupdf.readthedocs.io"),
        ".",
    ],
    [
        "The parser records coordinates for blocks,",
        "allowing approximate structure recovery",
        "(sections, headings, tables) where present.",
        "Heuristics join hyphenated lines and",
        "preserve numbering and legal citations",
        Cite("DocumentLayoutAnalysis2021"),
        ".",
    ],
    [
        "Quality gates run in CI. Schemas are validated,",
        "required fields are enforced, and checksums",
        "guard against corruption. Unit tests cover",
        "fetching, parsing, and serialization, and",
        "fail the job on regressions",
        Cite("DataQuality2022"),
        ".",
    ],
    [
        "Historical coverage was built via a",
        "back-population pipeline. We iterate over",
        "archival indexes and date ranges, enqueue",
        "jobs in batches, checkpoint progress, and",
        "resume safely after interruptions",
        Cite("HistoricalWebData2019"),
        ".",
    ],
    [
        "Transparency is prioritized. Run metadata,",
        "document counts, and last-updated timestamps",
        "are published to README badges. Commit",
        "messages summarize deltas, enabling clear,",
        "auditable provenance across releases",
        Cite("OpenDataPractices2020"),
        ".",
    ],
]


class ArXivDocSectionDataCollectionPipeline:

    @staticmethod
    def fill_section_data_collection_pipeline(doc):
        with doc.create(Section("Data Collection Pipeline")):
            Paragraph.fill_doc_from_list(
                doc,
                PARAGRAPH_ITEMS,
            )
