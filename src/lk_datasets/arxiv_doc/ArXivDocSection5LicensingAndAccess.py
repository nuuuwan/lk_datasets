from pylatex import Section

from latex import Cite, Footnote, Paragraph

PARAGRAPH_ITEMS = [
    [
        "All datasets and code are openly available to",
        "the public. The repositories are hosted on",
        "GitHub under the MIT License, which permits",
        "reuse, modification, and redistribution with",
        "attribution to the original author",
        Footnote("https://opensource.org/licenses/MIT"),
        ".",
    ],
    [
        "This permissive model encourages transparency",
        "and collaboration. Researchers, developers, and",
        "institutions can integrate the datasets into",
        "their pipelines without restrictive terms or",
        "commercial barriers",
        Cite("OpenDataPractices2020"),
        ".",
    ],
    [
        "Each dataset repository includes structured",
        "metadata, versioned releases, and README files",
        "with descriptive statistics and provenance.",
        "All assets are mirrored on Hugging Face to",
        "ensure redundancy and faster global access",
        Cite("HuggingFaceDatasets2021"),
        ".",
    ],
    [
        "Public accessibility is a design principle.",
        "Automated GitHub Actions update metadata badges",
        "and commit summaries whenever new data are",
        "ingested. Users can clone, fork, or download",
        "any subset directly without authentication",
        Footnote("https://docs.github.com/actions"),
        ".",
    ],
    [
        "Licensing notices are embedded in every dataset",
        "directory, clarifying reuse rights and",
        "responsibilities. The datasets intentionally",
        "avoid any personally identifiable information",
        "or restricted content to uphold ethical",
        "data-sharing standards",
        Cite("EthicalOpenData2019"),
        ".",
    ],
    [
        "The open license facilitates reproducible",
        "science and supports downstream applications",
        "in natural language processing, digital",
        "governance, and policy research. By ensuring",
        "public access, the project aligns with FAIR",
        "principles—Findable, Accessible, Interoperable,",
        "and Reusable",
        Cite("FAIRPrinciples2016"),
        ".",
    ],
]


class ArXivDocSection5LicensingAndAccess:
    @staticmethod
    def fill_section_licensing_and_access(doc):
        with doc.create(Section("Licensing and Access")):
            Paragraph.fill_doc_from_list(
                doc,
                PARAGRAPH_ITEMS,
            )
