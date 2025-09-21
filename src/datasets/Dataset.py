from functools import cache, cached_property

import requests
from utils import Log

log = Log("Dataset")


class Dataset:

    def __init__(self, repo_name: str, doc_class_label: str):
        self.repo_name = repo_name
        self.doc_class_label = doc_class_label

    def __str__(self):
        return f"Dataset({self.repo_name}/{self.doc_class_label})"

    @cached_property
    def url_summary(self):
        return "/".join(
            [
                "https://raw.githubusercontent.com",
                "nuuuwan",
                self.repo_name,
                "refs",
                "heads",
                "data",
                "data",
                self.doc_class_label,
                "summary.json",
            ]
        )

    @cached_property
    def summary(self) -> dict:
        try:
            response = requests.get(self.url_summary, timeout=10)
            response.raise_for_status()
            summary = response.json()
            log.info(f"Fetched summary for {self}")
            return summary
        except Exception as e:
            log.error(f"Failed to fetch summary for {self}: {e}")
            return None

    @classmethod
    def get_repo_to_doc_classes(cls) -> dict[str, list[str]]:
        return {
            "lk_hansard": ["lk_hansard"],
            "lk_appeal_court_judgements": ["lk_appeal_court_judgements"],
            "lk_supreme_court_judgements": ["lk_supreme_court_judgements"],
            "lk_police_press_releases": ["lk_police_press_releases"],
            "lk_legal_docs": [
                "lk_acts",
                "lk_bills",
                "lk_extraordinary_gazettes",
            ],
            "lk_cabinet_decisions": ["lk_cabinet_decisions"],
            "lk_treasury": ["lk_treasury_press_releases"],
        }

    @classmethod
    @cache
    def list_all(cls) -> list["Dataset"]:
        datasets = []
        for (
            repo_name,
            doc_class_labels,
        ) in cls.get_repo_to_doc_classes().items():
            for doc_class_label in doc_class_labels:
                dataset = cls(repo_name, doc_class_label)
                datasets.append(dataset)
        datasets.sort(
            key=lambda d: (d.summary.get("date_str_max")),
            reverse=True,
        )
        return datasets

    @classmethod
    @cache
    def get_global_summary(cls) -> dict:
        summary_list = [
            dataset.summary for dataset in cls.list_all() if dataset.summary
        ]
        return dict(
            n_datasets=len(summary_list),
            n_docs=sum([s.get("n_docs", 0) for s in summary_list]),
            all_dataset_size=sum(
                [s.get("dataset_size", 0) for s in summary_list]
            ),
        )
