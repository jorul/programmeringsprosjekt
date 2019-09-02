"""Aksjon defineres"""


class Aksjon:
    """En aksjon har en handling,
    og handlingene til ulike aksjoner 
    kan vurderes for å finne ut hvem som vinner"""
    def __init__(self, handling):
        self.handling = handling

    def __eq__(self, spiller2):
        return self.handling == spiller2.handling

    def __gt__(self, spiller2):
        if self.taper_mot() == spiller2.handling:
            return False
        return True

    def __str__(self):
        return self.handling

    def taper_mot(self):
        """returnerer den handlingen som den 
        handlingen metoden brukes på vil tape mot"""
        if self.handling == "stein":
            return "papir"
        if self.handling == "saks":
            return "stein"
        return "saks"
