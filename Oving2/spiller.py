import abc
from aksjon import Aksjon


class Spiller:

    stein = Aksjon("stein")
    saks = Aksjon("saks")
    papir = Aksjon("papir")

    def __intit__(self):
        self.poeng = 0
        self.historie = []
        self.motstander_historie = []

    @abc.abstractmethod
    def velg_aksjon(self):
        return

    def motta_resultat(self, selv_valgt, motstander_valgt, poeng):
        self.poeng += poeng
        self.historie.append(selv_valgt)
        self.motstander_historie.append(motstander_valgt)

    def oppgi_navn(self):
        return self.__class__.__name__

