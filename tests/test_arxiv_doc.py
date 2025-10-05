import os
import unittest
from unittest.mock import patch

from utils import JSONFile

from lk_datasets import ArXivDoc, LKDatasetsGlobalReadMe

TEST_SUMMARY_LIST = JSONFile(
    os.path.join("tests", "_input", "TEST_SUMMARY_LIST.json"),
).read()


class TestCase(unittest.TestCase):
    def test_build(self):
        with patch.object(
            LKDatasetsGlobalReadMe,
            "get_summary_list",
            return_value=TEST_SUMMARY_LIST,
        ):
            ArXivDoc().build()
