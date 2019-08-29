from spiller import Spiller


class Sekvensiell(Spiller):

    def __init__(self):
        super().__init__()
        self.i = 0

    def velg_aksjon(self):
        aksjon = Spiller.aksjoner[self.index]
        self.i += 1
        if self.i == 3:
            self.i = 0
        return aksjon