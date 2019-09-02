"""Modul for klassen Sekvensiell"""
from spiller import Spiller


class Sekvensiell(Spiller):
    """Spiller som spiller aksjonene i fast rekkefølge sekvensielt"""
    def __init__(self):
        super().__init__()
        self.i = 0

    def velg_aksjon(self):
        aksjon = Spiller.aksjoner[self.i]
        self.i += 1
        if self.i == 3:
            self.i = 0
        return aksjon
