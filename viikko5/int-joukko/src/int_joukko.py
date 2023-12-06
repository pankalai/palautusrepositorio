class IntJoukko:
    OLETUSKOKO = 5
    OLETUSKASVATUS = 5

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, joukon_koko=None, kasvatuskoko=None):
        self.joukon_koko = (
            joukon_koko if self.parametri_validi(joukon_koko) else self.OLETUSKOKO
        )

        self.kasvatuskoko = (
            kasvatuskoko if self.parametri_validi(kasvatuskoko) else self.OLETUSKASVATUS
        )

        self.ljono = self._luo_lista(self.joukon_koko)
        self.alkioiden_lkm = 0

    def parametri_validi(self, parametri):
        if not parametri or not isinstance(parametri, int) or parametri < 0:
            return False
        return True

    def kuuluu(self, n):
        if n in self.ljono:
            return True

        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return

        if self.alkioiden_lkm == len(self.ljono):
            self.ljono = self.ljono + self._luo_lista(self.kasvatuskoko)

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

    def poista(self, n):
        if not self.kuuluu(n):
            return

        index = self.ljono.index(n)
        self.ljono = self.ljono[:index] + self.ljono[index + 1 :] + [0]
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[: self.alkioiden_lkm]

    def yhdiste(a, b):
        return Yhdiste(a, b)

    def leikkaus(a, b):
        return Leikkaus(a, b)

    def erotus(a, b):
        return Erotus(a, b)

    def __str__(self):
        return (
            "{"
            + ", ".join([str(luku) for luku in self.ljono[: (self.alkioiden_lkm)]])
            + "}"
        )


class JoukkoOperaatiot(IntJoukko):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super(JoukkoOperaatiot, self).__init__()
        self.IntJoukko1 = a
        self.IntJoukko2 = b
        self.lista1 = self.IntJoukko1.to_int_list()
        self.lista2 = self.IntJoukko2.to_int_list()
        self.muodosta()

    def muodosta(self):
        return


class Yhdiste(JoukkoOperaatiot):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super().__init__(a, b)

    def muodosta(self):
        lista = sorted(self.lista1 + self.lista2)
        self.lisaa(lista[0])
        for i in range(1, len(lista)):
            if lista[i] != lista[i - 1]:
                self.lisaa(lista[i])


class Leikkaus(JoukkoOperaatiot):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super().__init__(a, b)

    def muodosta(self):
        lista = sorted(self.lista1 + self.lista2)
        for i in range(len(lista) - 1):
            if lista[i] == lista[i + 1]:
                self.lisaa(lista[i])


class Erotus(JoukkoOperaatiot):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super().__init__(a, b)

    def muodosta(self):
        j = 0
        for i in range(len(self.lista1)):
            while j < len(self.lista2) - 1 and self.lista2[j] < self.lista1[i]:
                j += 1
            if self.lista1[i] != self.lista2[j]:
                self.lisaa(self.lista1[i])
