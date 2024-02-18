from typing_extensions import override
from abc import ABC, abstractmethod


class Capture:
    """
    Abstract Class of Capture stream
    """

    @abstractmethod
    def get_frame(self):
        raise NotImplementedError

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_frame()



