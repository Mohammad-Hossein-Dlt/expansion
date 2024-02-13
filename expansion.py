from optimization import FormatEquation
from single_expansion import SingleExpansion
from multiple_expansion import MultipleExpansion
from consatnts import *
class Expansion:
    def __init__(self, equation) -> None:
        self.__equation__: str = FormatEquation(equation).equation
        self.result = list()
        self.splitNumber = self.__equation__.count(SingleExpansionSeparator.IDENTIFIER)
        print(self.__equation__)
        if self.splitNumber == 1 : self.result = SingleExpansion(equation).expanded
        else: self.result = MultipleExpansion(self.__equation__).final
