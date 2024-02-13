from consatnts import *
from optimization import sumSentences
from single_expansion import SingleExpansion
class MultipleExpansion(SingleExpansion):
    def __init__(self, rawedequation: str) -> None:
        separator = SingleExpansionSeparator()
        formatedequation = rawedequation
        splitNumber = formatedequation.count(SingleExpansionSeparator.IDENTIFIER)
        for i in range(splitNumber):
            separator.starter = i;
            separator.terminator = i;
            equation = formatedequation[formatedequation.index(separator.starter)+separator.starterLen():formatedequation.index(separator.terminator)]
            super().__init__(equation,True)
            if formatedequation.index(separator.starter) != 0:
                index = formatedequation.index(separator.starter)
                signBehindParenthese =  formatedequation[index-1]
                if signBehindParenthese == "+": 
                    formatedequation = formatedequation[:index-1] + formatedequation[index:]
                if signBehindParenthese == "-":
                    formatedequation = formatedequation[:index-1] + formatedequation[index:]
                    for s in self.expanded:
                        if s[0] == "-" : 
                            self.expanded[self.expanded.index(s)] =  s.replace("-","+")
                        if s[0] == "+" : 
                            self.expanded[self.expanded.index(s)] = s.replace("+","-")

            formatedequation = formatedequation.replace(formatedequation[formatedequation.index(separator.starter):formatedequation.index(separator.terminator)+separator.terminatorLen()], "".join(self.expanded) )

        formatedequation = formatedequation.replace(" ","")
        final = formatedequation.replace("+"," +").replace("-"," -")
        final = list(filter(lambda x : [""].__contains__(x) == False ,final.split(" ")))
        self.final = sumSentences(final)


