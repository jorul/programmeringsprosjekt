from spiller import Spiller
import random

class Historiker(Spiller):
    def __init__(self, husk = 1):
        super().__init__()
        self.husk = husk
    
    def velg_aksjon(self):
        if self.motstander_historie == []:
            return random.choice(self.aksjoner)
        
        liste_med_neste = self.finn_neste()
        if liste_med_neste == []:
            return random.choice(self.aksjoner)
        vanligst = self.mest_vanlig(liste_med_neste)
        return self.vinner_over(vanligst)
    
    def finn_neste(self):
        sekvens = self.motstander_historie[0 - (self.husk):]
        indexer_for_neste = [(i+len(sekvens)) for i in range(len(self.motstander_historie)-len(sekvens)) if self.motstander_historie[i:i+len(sekvens)] == sekvens]
        liste_med_neste =[]
        for n in indexer_for_neste:
            liste_med_neste.append(self.motstander_historie[n])
        return liste_med_neste





