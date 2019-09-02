"""Dette er en spiller som velger stein, saks eller papir helt tilfeldig."""

import random
from spiller import Spiller


class Tilfeldig(Spiller):
    """Spilleren velger tilfeldig"""
    def __init__(self):
        super().__init__()

    def velg_aksjon(self):
        return random.choice(self.aksjoner)
