from aksjon import Aksjon
from spiller import Spiller


class TestSpiller(Spiller):
    def __init__(self):
        super().__init__()

    def velg_aksjon(self):
        return Aksjon("stein")
