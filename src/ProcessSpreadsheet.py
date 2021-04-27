import pandas as pd
from interface import IReadingFiles


class ProcessSpreadSheet(IReadingFiles):
    def __init__(self, file):
        self.file = file
        self.df = None

    def checking_valid_format(self):
        if self.file[-3:] not in ('csv', 'tsv'):
            raise Exception('Invalid Format. Only .csv, .tsv format is allowed')
        return True

    def read_content(self):
        if self.checking_valid_format():
            if self.file.endswith('csv'):
                self.df = pd.read_csv(self.file)
            elif self.file.endswith('tsv'):
                self.df = pd.read_csv(self.file, sep='\t')
            return self.df

    def iterator_content(self):
        return (list(row) for row in self.read_content().values)

    def first_two_rows(self):
        return self.read_content().iloc[:2]

    def last_two_rows(self):
        return self.read_content().iloc[-2:]


read_spread = ProcessSpreadSheet('lorum.csv')
# print(read_spread.read_content())

print('First two lines: ')
print(read_spread.first_two_rows())

print('Last two lines: ')
print(read_spread.last_two_rows())

print(list(read_spread.iterator_content()))