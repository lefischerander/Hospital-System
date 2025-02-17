import unittest
from unittest.mock import patch, MagicMock
from test_analyse import Analyse
import pandas as pd
import os
from pathlib import Path


class TestAnalyse(unittest.TestCase):
    @patch("analyse.sa.create_engine")
    @patch("analyse.pd.read_sql_query")
    @patch("analyse.messagebox.askquestion")
    def test_read_diagnoses_icd(
        self, mock_askquestion, mock_read_sql_query, mock_create_engine
    ):
        # Mock the database connection and query result
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_read_sql_query.return_value = pd.DataFrame(
            {
                "hadm_id": [1, 2],
                "seq_num": [1, 2],
                "icd_code": ["A00", "B00"],
                "long_title": ["Cholera", "Herpesviral [herpes simplex] infections"],
                "icd_version": [9, 10],
            }
        )
        mock_askquestion.return_value = "yes"

        analyse = Analyse()
        result = analyse.read_diagnoses_icd(123)

        # Check if the result is as expected
        expected_result = (
            " hadm_id  seq_num icd_code                                      long_title  icd_version\n"
            "       1        1      A00                                        Cholera            9\n"
            "       2        2      B00  Herpesviral [herpes simplex] infections           10"
        )
        self.assertEqual(result, expected_result)

        # Check if the file was created
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, "diagnoses_123.txt")
        with open(file_path, "r") as file:
            file_content = file.read()
            self.assertEqual(file_content, expected_result)


if __name__ == "__main__":
    unittest.main()
