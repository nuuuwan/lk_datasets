from pylatex import Section

from latex import Cite, Footnote, Paragraph

PARAGRAPH_ITEMS = [
    [
        "The study of open datasets has been central to the",
        "development of natural language processing (NLP)",
        "and computational social science. Large corpora such",
        "as Common Crawl",
        Footnote("https://commoncrawl.org/"),
        ", Wikipedia",
        "Dumps",
        Footnote("https://dumps.wikimedia.org/"),
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
        Footnote("https://indiankanoon.org/"),
        ", the OpenSubtitles",
        "multilingual dataset",
        Footnote("https://opus.nlpl.eu/OpenSubtitles.php"),
        ", and the African News Corpus",
        Footnote("https://data.africanlp.org"),
        ". Such datasxets have",
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
        Footnote("https://github.com/sltalk"),
        Footnote("https://github.com/SriLankaNLP"),
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
]


class ArXivDocSectionRelatedWork:

    @staticmethod
    def fill_section_related_work(doc):

        with doc.create(Section("Related Work")):
            Paragraph.fill_doc_from_list(
                doc,
                PARAGRAPH_ITEMS,
            )
