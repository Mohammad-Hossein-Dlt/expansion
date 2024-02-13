class SingleExpansionSeparator:
    IDENTIFIER = "/"
    STARTER = "<@>"
    TERMINATOR = "</@>"

    def __init__(self) -> None:
        self._starter : str = SingleExpansionSeparator.STARTER
        self._terminator : str = SingleExpansionSeparator.TERMINATOR
        self.index = -1

    def starterLen(self) -> int: return len(self._starter)

    @property
    def starter(self) -> str: return self._starter

    @starter.setter
    def starter(self,index) -> str: self._starter = SingleExpansionSeparator.STARTER.replace("@",str(index))
    


    def terminatorLen(self) -> int: return len(self._terminator)


    @property
    def terminator(self) -> str: return  self._terminator

    @terminator.setter
    def terminator(self,index) -> str: self._terminator = SingleExpansionSeparator.TERMINATOR.replace("@",str(index))


