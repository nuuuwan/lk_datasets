from functools import cached_property

import requests
from utils import Log

log = Log("Dataset")


class Dataset:

    def __init__(self, name: str):
        self.name = name

    @cached_property
    def url_summary(self):
        return "/".join(
            [
                "https://raw.githubusercontent.com",
                "nuuuwan",
                self.name,
                "refs/heads/main/summary.json",
            ]
        )

    @cached_property
    def summary(self) -> dict:
        try:
            response = requests.get(self.url_summary)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            log.error(f"Failed to fetch summary for dataset {self.name}: {e}")

    @classmethod
    def list_all_names(cls) -> list[str]:
        return sorted(
            [
                "lk_hansard",
                "lk_appeal_court_judgements",
                "lk_supreme_court_judgements",
                "lk_police_press_releases",
            ]
        )

    @classmethod
    def list_all(cls) -> list["Dataset"]:
        return [cls(name) for name in cls.list_all_names()]
