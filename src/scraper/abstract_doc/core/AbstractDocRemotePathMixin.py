import os
from functools import cached_property

from utils import Log

log = Log("AbstractDocRemotePathMixin")


class AbstractDocRemotePathMixin:
    @classmethod
    def get_remote_repo_url(cls) -> str:
        assert os.environ["GITHUB_USERNAME"]
        return "/".join(
            [
                "https://github.com",
                os.environ["GITHUB_USERNAME"],
                cls.get_doc_class_label(),
            ]
        )

    @classmethod
    def get_remote_data_url_base(cls) -> str:
        assert os.environ["GITHUB_USERNAME"]
        return "/".join(
            [
                cls.get_remote_repo_url(),
                "tree",
                "data",
            ]
        )

    @cached_property
    def remote_data_url(self) -> str:
        return "/".join(
            [
                self.get_remote_data_url_base(),
                self.__class__.get_dir_docs_for_cls_relative(),
                self.dir_doc_relative_to_class,
            ]
        )
