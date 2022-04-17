from abc import ABC
from abc import abstractclassmethod


class Step(ABC):

    def __init__(self):
        pass

    @abstractclassmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):  #繼承python內建的Exception
    pass