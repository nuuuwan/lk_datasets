from utils import File, Log

from datasets.Dataset import Dataset
from scraper import AbstractDoc

log = Log("ReadMe")


class ReadMe:
    PATH = "README.md"

    @classmethod
    def get_lines_for_dataset(cls, i_dataset, dataset) -> list[str]:
        summary = dataset.summary
        if not summary or "doc_class_emoji" not in summary:
            return []
        header_lines = AbstractDoc.get_lines_for_header(summary)
        first_header_line = header_lines[0]
        first_header_line = first_header_line.replace(
            "# 🇱🇰 #SriLanka", f"## {i_dataset:02d} "
        ).replace("`Dataset`", "")
        header_lines[0] = first_header_line
        return header_lines + AbstractDoc.get_lines_for_blurb(summary)

    @classmethod
    def get_lines_for_datasets(cls) -> list[str]:
        lines = []
        for i_dataset, dataset in enumerate(Dataset.list_all(), start=1):
            lines.extend(cls.get_lines_for_dataset(i_dataset, dataset))
        return lines

    @classmethod
    def get_lines(cls) -> list[str]:
        return (
            [
                "# 🇱🇰 #SriLanka `Datasets`",
                "",
            ]
            + cls.get_lines_for_datasets()
            + ["---", ""]
            + AbstractDoc.get_lines_for_footer()
        )

    @classmethod
    def build(cls):
        File(cls.PATH).write_lines(cls.get_lines())
        log.info(f"Wrote {cls.PATH}")
