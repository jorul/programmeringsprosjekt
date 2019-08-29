class Aksjon:
    def __init__(self, handling):
        self.handling = handling

    def __eq__(self, spiller2):
        return self.handling == spiller2.handling

    def __gt__(self, spiller2):
        if self.vinner_over() == spiller2.handling:
            return True
        return False

    def __str__(self):
        return self.handling

    def vinner_over(self):
        if self.handling == "stein":
            return "saks"
        elif self.handling == "saks":
            return "papir"
        elif self.handling == "papir":
            return "stein"
