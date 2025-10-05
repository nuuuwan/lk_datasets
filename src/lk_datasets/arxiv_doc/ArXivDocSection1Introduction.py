from pylatex import Section

from latex import Paragraph

PARAGRAPH_ITEMS = [
    [
        "Sri Lanka’s digital record of law, policy, and media",
        "is fragmented across numerous government and",
        "private sources. Much of this information exists",
        "as PDFs or web pages, often lacking machine-",
        "readable structure or public archival consistency.",
        "This fragmentation limits access for citizens,",
        "journalists, and researchers interested in the",
        "island’s governance, history, and socio-economic",
        "trends.",
    ],
    [
        "The Sri Lanka Document Datasets initiative aims",
        "to bridge this gap by collecting, cleaning, and",
        "organizing key public documents into standardized,",
        "machine-readable formats. It unifies diverse",
        "materials—from Hansards and court judgements",
        "to news articles and tourism reports—under a",
        "common data framework. All datasets are openly",
        "licensed and continuously updated to ensure",
        "reproducibility and public transparency.",
    ],
    [
        "This effort is particularly significant for data-",
        "driven research in low-resource contexts. By",
        "providing structured data in Sinhala, Tamil, and",
        "English, the project supports the development of",
        "natural language processing models, cross-lingual",
        "studies, and digital humanities research. The",
        "datasets also enable policy analysis, legal",
        "precedent tracking, and media monitoring in a",
        "transparent, open science environment.",
    ],
    [
        "In this paper, we describe the scope and structure",
        "of these datasets, outline the scraping and curation",
        "processes, and highlight their potential applications",
        "in AI, governance, and public knowledge. Our goal",
        "is to create a living data archive that strengthens",
        "civic engagement and academic research through",
        "open, verifiable information.",
    ],
]


class ArXivDocSection1Introduction:
    @staticmethod
    def fill_section_introduction(doc):
        with doc.create(Section("Introduction")):
            Paragraph.fill_doc_from_list(
                doc,
                PARAGRAPH_ITEMS,
            )
