from streamlit import selectbox
from pandas import DataFrame
from lib.subjects import Subjects


class SelectBox:

    def __init__(self, title, subject: Subjects):
        self.title = title
        self.name = subject.name
        self._data_frame = DataFrame({subject.name: subject.value})

    def select_options(self):
        return selectbox(self.title, self._data_frame[self.name])
