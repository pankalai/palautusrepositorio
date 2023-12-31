from tuote import Tuote
from ostos import Ostos
from functools import reduce


class Ostoskori:
    def __init__(self):
        self._ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return reduce(
            lambda summa, ostos: summa + ostos.lukumaara(), self._ostoskori, 0
        )
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        return reduce(lambda summa, ostos: summa + ostos.hinta(), self._ostoskori, 0)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = self.hae_ostos_ostoskorista(lisattava)
        if ostos:
            ostos.muuta_lukumaaraa(1)
            return

        self._ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        ostos = self.hae_ostos_ostoskorista(poistettava)
        if ostos:
            ostos.muuta_lukumaaraa(-1)
            if ostos.lukumaara() == 0:
                self._ostoskori.remove(ostos)

    def tyhjenna(self):
        self._ostoskori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

    def hae_ostos_ostoskorista(self, haettava: Tuote):
        for ostos in self._ostoskori:
            if ostos.tuotteen_nimi() == haettava.nimi():
                return ostos
        return None

        ## Vaihtoehtoinen tapa
        # return next(
        #     (
        #         ostos
        #         for ostos in self._ostoskori
        #         if ostos.tuotteen_nimi() == haettava.nimi()
        #     ),
        #     None,
        # )
