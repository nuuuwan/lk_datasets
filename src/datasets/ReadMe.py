from utils import File, Log

from datasets.Dataset import Dataset

log = Log("ReadMe")


class ReadMe:
    PATH = "README.md"

    @classmethod
    def get_lines_for_summary(cls, summary) -> list[str]:
        if not summary:
            return ["⚠️ No data yet", ""]
        time_updated = summary["time_updated"]
        n_docs = summary["n_docs"]
        date_str_min = summary["date_str_min"]
        date_str_max = summary["date_str_max"]
        total_size_humanized = summary["total_size_humanized"]
        url_source = summary["url_source"]
        url_data = summary["url_data"]
        url_repo = summary["url_repo"]

        total_size_humanized_for_badge = total_size_humanized.replace(
            " ", "_"
        )

        return [
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated}-green)",
            "![DatasetSize](https://img.shields.io/badge"
            + f"/dataset_size-{total_size_humanized_for_badge}-yellow)",
            "",
            f"[{url_repo}]({url_repo})",
            "",
            f"📜 [**{n_docs:,}** documents]({url_data})"
            + f" (**{total_size_humanized}**),"
            + f" from **{date_str_min}** to **{date_str_max}**,"
            + f" scraped from **[{url_source}]({url_source})**",
            "",
        ]

    @classmethod
    def get_lines_for_dataset(cls, i_dataset, dataset) -> list[str]:
        summary = dataset.summary
        return [
            f"## {i_dataset:02d}) {dataset.name}",
            "",
        ] + cls.get_lines_for_summary(summary)

    @classmethod
    def get_lines_for_datasets(cls) -> list[str]:
        lines = []
        for i_dataset, dataset in enumerate(Dataset.list_all(), start=1):
            lines.extend(cls.get_lines_for_dataset(i_dataset, dataset))
        return lines

    @classmethod
    def get_lines_for_footer(cls) -> list[str]:
        return [
            "---",
            "",
            "![Maintainer](https://img.shields.io/badge"
            + "/maintainer-nuuuwan-red)",
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)",
            "",
        ]

    @classmethod
    def get_lines(cls) -> list[str]:
        return (
            [
                "# 🇱🇰 #SriLanka Dataset `Dataset`",
                "",
            ]
            + cls.get_lines_for_datasets()
            + cls.get_lines_for_footer()
        )

    @classmethod
    def build(cls):
        File(cls.PATH).write_lines(cls.get_lines())
        log.info(f"Wrote {cls.PATH}")
