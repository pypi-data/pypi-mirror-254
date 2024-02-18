from mindt_Selino.dtMinimisation import *
from mindt_Selino.optimizedQuineMcCluskey import OptimizedQuineMcCluskey

class DtMinOptimized(DtMinimisation):
    def __init__(self, path):
        readInput = ReadInput()

        input = readInput.readIntervalInput(path)

        newImplicants = set()

        for element in input:
            newImplicants.update(element.unfold(readInput.stages), readInput.stages)

        staggeredImplicants = list(newImplicants)

        output = OptimizedQuineMcCluskey.execute(staggeredImplicants)

        self.input = input
        self.staggeredImplicants = staggeredImplicants
        self.output = list(output)