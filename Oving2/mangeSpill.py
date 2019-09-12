""" Modul for klassen MangeSpill"""
import numpy as np
import matplotlib.pyplot as plt
from enkeltSpill import EnkeltSpill


class MangeSpill():
    """Klasse som benytter enkeltspill for å spille flere spill"""
    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.nyttspill = EnkeltSpill(spiller1, spiller2)
        self.antall_spill = antall_spill
        self.resultater = []

    def arranger_enkeltspill(self, i):
        """Metode for å gjennomføre et enkeltspill"""
        self.nyttspill.gjennomfoer_spill()
        print(self.nyttspill)
        self.resultater.append((self.spiller1.poeng, self.spiller2.poeng, i))
        #print(self.resultater)

    def arranger_turnering(self):
        """Metode for å arrangere turnering"""
        for i in range(1, self.antall_spill+1):
            self.arranger_enkeltspill(i)

    def plott_graf(self):
        """Plotter grafen ved bruk av numpy og pyplot"""
        x_axis = np.arange(1, self.antall_spill + 1, 1)
        y_1_axis = np.zeros(self.antall_spill)
        y_2_axis = np.zeros(self.antall_spill)

        index = 0
        for i in self.resultater:
            y_1_axis[index] = i[0] / i[2]
            y_2_axis[index] = i[1] / i[2]
            index += 1

        plt.plot(x_axis, y_1_axis, label='Spiller 1')
        plt.show()
