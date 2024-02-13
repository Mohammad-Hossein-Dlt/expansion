from optimization import *
class SingleExpansion :
    def __init__(self,equation: str, separator: bool = False) -> None:
        self.__showWithSeparator = separator
        equation =  equation.replace("|","")
        self.__equation = equation.replace(" ","") # --> (aX+bY+cZ+...)^n
        for i in [ ["+" , " +"] , ["-"," -"]  ] : self.__equation = self.__equation.replace(i[0],i[1])
        variables = list(filter(lambda x : ["","(",")"].__contains__(x) == False ,self.__equation[self.__equation.index("(")+1:self.__equation.index(")")].split(" "))) # --> ["aX", "bY", "cZ",...]   
        self.__variables =  variables
        for i in self.__variables:
            optimized = i
            while optimized.__contains__("^"):
                index = optimized.index("^")
                var = optimized[index-1]
                power = ""
                optimized = optimized[:index]+"<p>"+optimized[index+1:]
                for c in range(index+3, len( optimized )) :
                    if optimized[c].isalpha() : 
                        optimized = optimized[:c]+"</p>"+optimized[c:]
                        break
                    if c+1 == len(optimized): optimized = optimized+"</p>"
                power = optimized[optimized.index("<p>")+3:optimized.index("</p>")]
                brfore = optimized[:optimized.index(var)]
                midel = (var*int(power))
                after  = optimized[ optimized.index("</p>")+4:]
                optimized = brfore + midel + after
            self.__variables[self.__variables.index(i)] = optimized
        self.__power = int(self.__equation[self.__equation.index(")^")+2:]) # --> n
        for i in self.__variables:
            if i.isalpha(): self.__variables[self.__variables.index(i)] = "+1" + i
            elif "-" in i:
                if i[1:].isalpha() : self.__variables[self.__variables.index(i)] = "-1" + i[1:]
            elif "+" in i:
                if i[1:].isalpha() : self.__variables[self.__variables.index(i)] = "+1" + i[1:]
        self.expanded: dict = self.sentences()

    def sentences(self):
        finalSentences: list = []
        def generate(sentences: list):
            factors: list = []
            variables: list = []
            for s in sentences:
                factor = ""
                for char in s:
                    if char.isnumeric() or char == "-" or char == "+" : factor += char
                    if char.isalpha(): break
                factors.append(factor)
                variables.append(s[len(factor):])
            
            factors = list(map(lambda x : int(x), factors))
            variables = sorted(''.join(variables))
            
            multipliedFactors = 1
            for i in factors: multipliedFactors *= i
           
            combinedVariable = ""
            for i in variables:
                if i not in combinedVariable:
                    numberOfVar = variables.count(i)
                    if numberOfVar > 1 : combinedVariable += i + "^" + str(numberOfVar)
                    if  numberOfVar == 1 : combinedVariable += i

            finalS = ""
            if multipliedFactors > 0 :
                if multipliedFactors == 1 : finalS = "+" + "|"+  combinedVariable
                else : finalS = "+" + str(multipliedFactors) +  "|"+ combinedVariable
            else:
                if multipliedFactors == -1 : finalS = "-" + "|"+  combinedVariable
                else : finalS = str(multipliedFactors) +  "|"+ combinedVariable
        
            finalSentences.append(finalS)
        forModel = "for _ in iterable:"
        number = [self.__variables for i in range(self.__power)]
        generatedFor = ""
        for i in range(self.__power):
            generatedFor += (i*"	")+  forModel.replace("_", f"n{i}").replace("iterable",f"{number[i]}")+"\n"
            if i == len(number)-1 :
                xn = "["
                for s in [f"n{i}" for i in range(self.__power)]: xn += s+","
                xn += "]"
                generatedFor += ((i+1)*"	")+  f"generate({xn})"
        exec(generatedFor)
        return sumSentences(finalSentences,self.__showWithSeparator)
