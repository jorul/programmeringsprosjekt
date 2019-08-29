from enkeltSpill import EnkeltSpill
from tilfeldig import Tilfeldig
from testSpiller import TestSpiller1
from sekvensiell import Sekvensiell


class MangeSpill():
    def __init__(self, spiller1, spiller2, antall_spill):
        self.nyttspill = EnkeltSpill(spiller1, spiller2)
        self.antall_spill = antall_spill
    
    def arranger_enkeltspill(self):
        self.nyttspill.gjennomfoer_spill()
        print(self.nyttspill)
    
    def arranger_turnering(self):
        for i in range(0,self.antall_spill):
            self.arranger_enkeltspill()

s1 = Tilfeldig()
s2 = Sekvensiell()

testing = MangeSpill(s1,s2,6)
testing.arranger_turnering()
