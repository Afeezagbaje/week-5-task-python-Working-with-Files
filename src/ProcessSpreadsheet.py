import pandas as pd
from interface import IReadingFiles


class ProcessSpreadSheet(IReadingFiles):
    """This class read files with .csv and .tsv format only and create a spreadsheet
      ......
      checking_valid_format() check if the format of the file is valid
      read_content() read the content of the file
      iterator() turns our content into an iterator
      iterating_content() print the content one at a time
      first_two_rows() returns the first two rows of the file
      last_two_rows() returns the last two rows of the file
    """
    def __init__(self, file):
        self.file = file
        self.df = None
        self.get_extension = self.file.split('.')
        self.get_extension = self.get_extension[-1]

    def checking_valid_format(self):
        if self.get_extension not in ('csv', 'tsv'):
            print('Invalid Format. Only .csv, .tsv format is allowed')
        return True

    def read_content(self):
        try:
            if self.checking_valid_format():
                if self.file.endswith('csv'):
                    self.df = pd.read_csv(self.file)
                elif self.file.endswith('tsv'):
                    self.df = pd.read_csv(self.file, sep='\t')
                return self.df
        except FileNotFoundError:
            print('This file does not exist')

    def iterator(self):
        try:
            return (list(row) for row in self.read_content().values)
        except AttributeError:
            pass

    def iterating_content(self):
        try:
            return next(self.iterator())
        except TypeError:
            pass

    def first_two_rows(self):
        try:
            return self.read_content().iloc[:2]
        except AttributeError:
            pass

    def last_two_rows(self):
        try:
            return self.read_content().iloc[-2:]
        except AttributeError:
            pass
