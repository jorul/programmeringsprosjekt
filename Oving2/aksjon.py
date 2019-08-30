class Aksjon:
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
        if self.handling == "stein":
            return "papir"
        elif self.handling == "saks":
            return "stein"
        elif self.handling == "papir":
            return "saks"


