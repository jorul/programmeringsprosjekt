"""Modul for klassen enkeltspill"""

class EnkeltSpill:
    """Klasse for å opprette et enkeltspill med metoder for å gjennomføre spillet"""
    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.resultat = ""
        self.spiller1_aksjon = None
        self.spiller2_aksjon = None

    def gjennomfoer_spill(self):
        """Spill som er opprettet gjennomføres"""
        self.spiller1_aksjon = self.spiller1.velg_aksjon()
        self.spiller2_aksjon = self.spiller2.velg_aksjon()
        spiller1_poeng = 0
        spiller2_poeng = 0
        if self.spiller1_aksjon == self.spiller2_aksjon:
            spiller1_poeng = 0.5
            spiller2_poeng = 0.5
            self.resultat = 'uavgjort'
        elif self.spiller1_aksjon > self.spiller2_aksjon:
            spiller1_poeng = 1
            self.resultat = f'{self.spiller1.oppgi_navn()} vant'
        else:
            spiller2_poeng = 1
            self.resultat = f'{self.spiller2.oppgi_navn()} vant'
        self.spiller1.motta_resultat(self.spiller1_aksjon, self.spiller2_aksjon, spiller1_poeng)
        self.spiller2.motta_resultat(self.spiller2_aksjon, self.spiller1_aksjon, spiller2_poeng)

    def __str__(self):
        tekst = (f'{self.spiller1.oppgi_navn()} valgte {self.spiller1_aksjon}, '
                 f'{self.spiller2.oppgi_navn()} valgte {self.spiller2_aksjon}'
                 f' --> {self.resultat}')
        return tekst
