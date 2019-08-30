from spiller import Spiller
import random
from collections import Counter
from aksjon import Aksjon

class MestVanlig(Spiller):
    def __init__(self):
        super().__init__()
    
    def velg_aksjon(self):
        if self.motstander_historie == []:
            return random.choice(self.aksjoner)

        return self.vinner_over(self.mest_vanlig(self.motstander_historie))
 

