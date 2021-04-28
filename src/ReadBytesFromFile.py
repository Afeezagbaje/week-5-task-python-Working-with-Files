from .interface import IReadingFiles


class ReadBytesFromFile(IReadingFiles):
    """This class read files with .txt, .csv and .tsv format only
      ......
      checking_valid_format() check if the format of the file is valid
      get_content() read the content
      iterator() turns our content into an iterator
      read_content() read the content of the file
      first_two_rows() returns the first two rows of the file
      last_two_rows() returns the last two rows of the file
    """
    def __init__(self, file):
        self.file = file
        self.get_extension = self.file.split('.')
        self.get_extension = self.get_extension[-1]

    def checking_valid_format(self):
        if self.get_extension not in ('txt', 'csv', 'tsv'):
            print('Invalid Format. Only .txt, .csv, .tsv format is allowed')
            return False
        return True

    def get_content(self):
        if self.checking_valid_format():
            try:
                with open(self.file) as file_content:
                    contents = file_content.readlines()
                return contents
            except FileNotFoundError:
                return 'This file does not exist'

    def iterator(self):
        try:
            return iter(self.get_content())
        except TypeError:
            pass

    def read_content(self):
        try:
            for line in self.iterator():
                print(line)
        except TypeError:
            pass

    def first_two_rows(self):
        try:
            for line in self.get_content()[1:3]:
                print(line)
        except TypeError:
            pass

    def last_two_rows(self):
        try:
            for line in self.get_content()[-2:]:
                print(line)
        except TypeError:
            pass


read = ReadBytesFromFile('../sample_files/lorum.csv')

print(read.iterator())