from abc import ABC, abstractmethod


class IReadingFiles(ABC):
    @abstractmethod
    def checking_valid_format(self):
        pass

    @abstractmethod
    def iterator(self):
        pass

    @abstractmethod
    def read_content(self):
        pass

    @abstractmethod
    def first_two_rows(self):
        pass

    @abstractmethod
    def last_two_rows(self):
        pass
