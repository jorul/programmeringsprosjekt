"""Modul for klassen MestVanlig"""
import random
from spiller import Spiller


class MestVanlig(Spiller):
    """Spiller som returnerer den aksjonen som vinner over den
    aksjonen motstanderen har spilt flest ganger tidligere"""
    def __init__(self):
        super().__init__()

    def velg_aksjon(self):
        if self.motstander_historie == []:
            return random.choice(self.aksjoner)

        return self.vinner_over(self.mest_vanlig(self.motstander_historie))
