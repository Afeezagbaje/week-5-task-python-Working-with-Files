from interface import IReadingFiles


class ReadBytesFromFile(IReadingFiles):
    def __init__(self, file):
        self.file = file

    def checking_valid_format(self):
        if self.file[-3:] not in ('txt', 'csv', 'tsv'):
            raise Exception('Invalid Format. Only .txt, .csv, .tsv format is allowed')
        return True

    def get_content(self):
        if self.checking_valid_format():
            with open(self.file) as file_content:
                contents = file_content.readlines()
            return contents

    def iterator_content(self):
        return iter(self.get_content())

    def read_content(self):
        for line in self.iterator_content():
            print(line)

    def first_two_rows(self):
        for line in self.get_content()[1:3]:
            print(line)

    def last_two_rows(self):
        for line in self.get_content()[-2:]:
            print(line)


read_file = ReadBytesFromFile('lorum.csv')
print(read_file.read_content())

print('First two lines: ')
print(read_file.first_two_rows())
