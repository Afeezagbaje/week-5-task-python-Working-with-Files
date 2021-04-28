import unittest
from src.ProcessSpreadsheet import ProcessSpreadSheet


class TestProcessSpreadSheet(unittest.TestCase):
    def setUp(self):
        self.csv_format = ProcessSpreadSheet('../sample_files/lorum.csv')
        self.tsv_format = ProcessSpreadSheet('../sample_files/lorum.tsv')
        self.txt_format = ProcessSpreadSheet('../sample_files/lorum.txt')
        self.invalid_format = ProcessSpreadSheet('../sample_files/lorum.xml')

    def test_checking_valid_format(self):
        self.assertTrue(self.csv_format.checking_valid_format())
        self.assertTrue(self.tsv_format.checking_valid_format())
        self.assertIsNot(self.txt_format.checking_valid_format(), True)
        self.assertFalse(self.invalid_format.checking_valid_format())

    def test_read_content(self):
        self.assertIsNotNone(self.csv_format.read_content())
        self.assertIsNotNone(self.tsv_format.read_content())
        self.assertIsNone(self.txt_format.read_content())
        self.assertIsNone(self.invalid_format.read_content())

    def test_iterator(self):
        self.assertIsNotNone(self.csv_format.iterator())
        self.assertIsNotNone(self.tsv_format.iterator())
        self.assertIsNone(self.txt_format.iterator())
        self.assertIsNone(self.invalid_format.iterator())

    def test_iterating_content(self):
        self.assertIsNotNone(self.csv_format.iterating_content())
        self.assertIsNotNone(self.tsv_format.iterating_content())
        self.assertIsNone(self.txt_format.iterating_content())
        self.assertIsNone(self.invalid_format.iterating_content())

    def test_first_two_rows(self):
        self.assertIsNotNone(self.csv_format.first_two_rows())
        self.assertIsNotNone(self.tsv_format.first_two_rows())
        self.assertIsNone(self.txt_format.first_two_rows())
        self.assertIsNone(self.invalid_format.first_two_rows())

    def test_last_two_rows(self):
        self.assertIsNotNone(self.csv_format.last_two_rows())
        self.assertIsNotNone(self.tsv_format.last_two_rows())
        self.assertIsNone(self.txt_format.last_two_rows())
        self.assertIsNone(self.invalid_format.last_two_rows())


if __name__ == '__main__':
    unittest.main()
