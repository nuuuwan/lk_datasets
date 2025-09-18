import json
import os

from utils import File, Log

from scraper.abstract_doc.readme.AbstractDocChartDocsByYearMixin import (
    AbstractDocChartDocsByYearMixin,
)
from utils_future import FileOrDirFuture, Format

log = Log("AbstractDocReadMeMixin")


class AbstractDocReadMeMixin(AbstractDocChartDocsByYearMixin):
    N_LATEST = 20

    # lines
    # ----------------------------------------------------------------

    @classmethod
    def get_lines_for_header(cls, summary) -> list[str]:
        title = Format.title(summary["doc_class_label"])
        return [
            f"# {title} `Dataset`",
            "",
        ]

    @classmethod
    def get_line_for_blurb_item_files(cls, summary) -> list[str]:
        n_docs = summary["n_docs"]
        n_docs_with_pdfs = summary["n_docs_with_pdfs"]
        n_docs_with_text = summary["n_docs_with_text"]

        blob_list = []
        for doc_type, n in [
            ("JSON", n_docs),
            ("PDF", n_docs_with_pdfs),
            ("TXT", n_docs_with_text),
            ("🤗 Hugging Face", n_docs_with_text),
        ]:
            if n == 0:
                continue
            p = n / n_docs
            if n == n_docs:
                emoji = "✅"
                label = ""
            else:
                emoji = "☑️"
                label = f"({p:.0%})"

            blob_list.append(f"{emoji} **{doc_type}** {label}".strip())
        return "💾 In " + Format.and_list(blob_list)

    @classmethod
    def get_line_for_blurb_item_lang(cls, summary) -> list[str]:
        lang = summary["latest_doc_d"]["lang"]
        blurb_langs = []
        for lang_i, lang_label in [
            ["si", "සිංහල"],
            ["ta", "தமிழ்"],
            ["en", "English"],
        ]:
            if lang_i in lang:
                blurb_langs.append(f"**{lang_label}**")

        return "🗣️ In " + Format.and_list(blurb_langs)

    @classmethod
    def get_lines_for_blurb(cls, summary) -> list[str]:
        time_updated = summary["time_updated"]
        n_docs = summary["n_docs"]
        date_str_min = summary["date_str_min"]
        date_str_max = summary["date_str_max"]
        dataset_size = summary["dataset_size"]
        url_source = summary["url_source"]
        url_data = summary["url_data"]
        url_repo = summary["url_repo"]

        dataset_size_humanized = FileOrDirFuture.humanize_size(dataset_size)
        time_updated_for_badge = Format.badge(time_updated)

        return [
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated_for_badge}-green)",
            "",
            f"[{url_repo}]({url_repo})",
            "",
            f"📜 [**{n_docs:,}** documents]({url_data})"
            + f" (**{dataset_size_humanized}**),"
            + f" from **{date_str_min}** to **{date_str_max}**,"
            + f" scraped from **[{url_source}]({url_source})**",
            "",
            cls.get_line_for_blurb_item_files(summary),
            "",
            cls.get_line_for_blurb_item_lang(summary),
            "",
        ]

    @classmethod
    def get_lines_for_metadata_example(cls, summary) -> list[str]:
        latest_doc_d = summary["latest_doc_d"]
        return [
            "## 📝 Example Metadata",
            "",
            "```json",
            json.dumps(latest_doc_d, indent=4),
            "```",
            "",
        ]

    @classmethod
    def get_lines_chart_docs_by_year(cls) -> list[str]:
        cls.get_chart_build()
        return [
            "## Documents By Year",
            "",
            f"![Documents by year]({cls.get_chart_image_path()})",
            "",
        ]

    @classmethod
    def get_lines_for_hugging_face(cls):
        url_hf = (
            "https://img.shields.io/badge"
            + "/-HuggingFace-FDEE21"
            + "?style=for-the-badge&logo=HuggingFace"
        )
        lines = [
            "## 🤗 Hugging Face Datasets",
            "",
            f"![HuggingFace]({url_hf})",
            "",
        ]

        for emoji, label_suffix in [["📄", "docs"], ["📦", "chunks"]]:
            dataset_id = cls.get_dataset_id(label_suffix)
            url = cls.get_dataset_url(label_suffix)
            lines.append(f"- {emoji} [{dataset_id}]({url})")
        lines.append("")
        return lines

    @classmethod
    def get_lines_for_latest_docs(cls):
        lines = [f"## 🆕 {cls.N_LATEST} Latest documents", ""]
        for doc in cls.list_all()[: cls.N_LATEST]:
            line = "- " + " | ".join(
                [
                    doc.date_str,
                    f"`{doc.num}`",
                    doc.description,
                    f"[data]({doc.remote_data_url})",
                ]
            )
            lines.append(line)
        lines.append("")
        return lines

    @classmethod
    def get_lines_for_footer(cls) -> list[str]:
        return [
            "---",
            "",
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
            "",
        ]

    @classmethod
    def lines(cls) -> list[str]:
        summary = cls.get_summary()
        return (
            cls.get_lines_for_header(summary)
            + cls.get_lines_for_blurb(summary)
            + cls.get_lines_for_metadata_example(summary)
            + cls.get_lines_chart_docs_by_year()
            + cls.get_lines_for_hugging_face()
            + cls.get_lines_for_latest_docs()
            + cls.get_lines_for_footer()
        )

    @classmethod
    def get_readme_path(cls) -> str:
        return os.path.join(cls.get_main_branch_dir_root(), "README.md")

    @classmethod
    def build_readme(cls):
        assert cls.list_all()
        os.makedirs(cls.get_main_branch_dir_root(), exist_ok=True)
        readme_path = cls.get_readme_path()
        File(readme_path).write("\n".join(cls.lines()))
        log.info(f"Wrote {readme_path}")
