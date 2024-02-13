from consatnts import *
class FormatEquation :
    def __init__(self, equation: str) -> None:
        separator = SingleExpansionSeparator()
        self.equation = equation.replace(" ","").replace(")",")$")
        while self.equation.__contains__("$"):
            index = self.equation.index("$")
            after = self.equation[index+1:]
            index2 = index
            for char in after:
                if char.isnumeric() or char == "^" : index2 += 1
                else : break
            power = self.equation[index+1:index2+1]
            if power == "" : power = "^1"
            self.equation = self.equation[:index] + power + "|"+self.equation[index2+1:]
        for i in range(self.equation.count("(")):
            separator.starter, separator.terminator = i,i;
            starter = self.equation.rindex("(")
            self.equation =  self.equation[:starter]+ separator.starter + '~'+ self.equation[starter+1:]
            for char in range(starter,len(self.equation)):
                if self.equation[char] == "|":
                    self.equation =  self.equation[:char]+ separator.terminator + self.equation[char+1:]
                    break
        self.equation = "".join(self.equation).replace("~","(")





def sumSentences(sentences : list, separator : bool = False):
    seperatedSentences : dict[str, list] = {}
    sum_ = []
    for s in sentences:
       factor, sentence = s.split("|")
       if factor == "+" : factor = "+1"
       if factor == "-" : factor = "-1"
       keys = list(map(lambda x: x[0], seperatedSentences.items()))
       if keys.__contains__(sentence): seperatedSentences[sentence].append(int(factor))
       else: seperatedSentences[sentence] = [int(factor)]

    for s,f in seperatedSentences.items():
        total_fator = str(sum(f))
        optimized_total_fator = total_fator
        final_sentence = s;
        if int(total_fator) > 0: 
            if total_fator == "1": optimized_total_fator = "+"
            else : optimized_total_fator = "+" + total_fator 
        if int(total_fator) < 0  : 
            if total_fator == "-1": optimized_total_fator = "-"
            esle: optimized_total_fator = "-" + total_fator
        sum_.append(optimized_total_fator+("|" if separator else "")+final_sentence)
    return sum_;
