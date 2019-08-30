import abc
from aksjon import Aksjon


class Spiller:
    __metaclass__ = abc.ABCMeta

    stein = Aksjon("stein")
    saks = Aksjon("saks")
    papir = Aksjon("papir")
    aksjoner = [stein, saks, papir]

    def __init__(self):
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
    
    
    def vinner_over(self, aksjon):
        if aksjon == self.stein:
            return self.papir
        if aksjon == self.saks:
            return self.stein
        return self.saks

    @staticmethod
    def mest_vanlig(liste):
        teller = 0
        mest_vanlig = liste[0]     
        for i in liste: 
            høyest = liste.count(i) 
            if(høyest> teller): 
                teller = høyest
                mest_vanlig = i
        return mest_vanlig

