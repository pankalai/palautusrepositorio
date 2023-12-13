from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tuomari import Tuomari


class Peli:
    def __init__(self, peli):
        self._peli = peli

    @staticmethod
    def luo_peli(tyyppi):
        if tyyppi == "a":
            return Peli(KPSPelaajaVsPelaaja())
        if tyyppi == "b":
            return Peli(KPSTekoaly())
        if tyyppi == "c":
            return Peli(KPSParempiTekoaly())

        return None

    def pelaa(self):
        return self._peli.pelaa()
