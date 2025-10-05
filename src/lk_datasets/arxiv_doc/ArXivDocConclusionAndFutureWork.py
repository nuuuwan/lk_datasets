from pylatex import Section

from latex import Cite, Paragraph


class ArXivDocConclusionAndFutureWork:
    @staticmethod
    def fill_section_conclusion_and_future_work(doc):
        with doc.create(Section("Conclusion and Future Work")):

            Paragraph.fill_doc_from_list(
                doc,
                [
                    [
                        "This project establishes an open, reproducible,",
                        "and scalable foundation for Sri Lankan document",
                        "datasets, spanning legal, governmental, and",
                        "media sources. The pipeline integrates crawling,",
                        "parsing, and versioning into a unified",
                        "ecosystem for data-driven research.",
                        Cite("OpenDataPractices2020"),
                    ],
                    [
                        "The datasets already serve as a valuable",
                        "resource for natural language processing,",
                        "computational law, and policy analysis. They",
                        "enable quantitative and qualitative insights",
                        "into governance, lawmaking, and civic",
                        "communication over time.",
                        Cite("FAIRPrinciples2016"),
                    ],
                    [
                        "Future development focuses on three priorities:",
                    ],
                    [
                        "First, expanding coverage by adding new",
                        "datasets from additional government agencies,",
                        "media sources, and historical archives.",
                        Cite("DataExpansion2023"),
                    ],
                    [
                        "Second, improving the linguistic accuracy of",
                        "Sinhala and Tamil parsing, particularly for",
                        "complex sentence structures and transliterated",
                        "terms. Enhancements in tokenization, font",
                        "handling, and multilingual embeddings are",
                        "planned.",
                        Cite("MultilingualNLP2022"),
                    ],
                    [
                        "Third, integrating OCR parsing for PDFs with",
                        "unstructured or scanned content. We are",
                        "experimenting with deep-learning-based OCR",
                        "pipelines that combine layout recognition and",
                        "language modeling to recover high-quality text",
                        "from low-quality sources.",
                        Cite("OCROpenResearch2021"),
                    ],
                    [
                        "Together, these directions will further improve",
                        "coverage, data quality, and usability, ensuring",
                        "that the Sri Lanka Datasets initiative remains a",
                        "sustainable open infrastructure for the region’s",
                        "digital and academic ecosystem.",
                        Cite("OpenDataSustainability2020"),
                    ],
                ],
            )
