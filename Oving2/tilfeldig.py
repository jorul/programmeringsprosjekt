from aksjon import Aksjon
from spiller import Spiller
import random

class Tilfeldig(Spiller):
    def __init__(self):
        super().__init__()
    def velg_aksjon(self):
        return random.choice(self.aksjoner)


