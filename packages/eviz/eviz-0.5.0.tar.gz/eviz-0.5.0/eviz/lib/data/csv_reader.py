import pandas as pd

from .base_reader import BaseReader


class CsvReader(BaseReader):
    def __init__(self, filename, model):
        super().__init__(filename=filename, model=model)
        self.data = self.open_file(self.fn)
        self.model = 'tabular'

    def open_file(self, file):
        return pd.read_csv(file)
