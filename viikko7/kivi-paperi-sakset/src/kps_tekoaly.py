from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari=None):
        super().__init__(tuomari)
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
