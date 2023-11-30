class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = (
            kapasiteetti if self.parametri_validi(kapasiteetti) else self.KAPASITEETTI
        )

        self.kasvatuskoko = (
            kasvatuskoko if self.parametri_validi(kasvatuskoko) else self.OLETUSKASVATUS
        )

        self.ljono = self._luo_lista(self.kapasiteetti)
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


class Yhdiste(IntJoukko):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super(Yhdiste, self).__init__()
        self.IntJoukko1 = a
        self.IntJoukko2 = b
        self.muodosta_yhdiste()

    def muodosta_yhdiste(self):
        a_lista = self.IntJoukko1.to_int_list()
        b_lista = self.IntJoukko2.to_int_list()

        lista = sorted(a_lista + b_lista)
        self.lisaa(lista[0])
        for i in range(1, len(lista)):
            if lista[i] != lista[i - 1]:
                self.lisaa(lista[i])


class Leikkaus(IntJoukko):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super(Leikkaus, self).__init__()
        self.IntJoukko1 = a
        self.IntJoukko2 = b
        self.muodosta_leikkaus()

    def muodosta_leikkaus(self):
        a_lista = self.IntJoukko1.to_int_list()
        b_lista = self.IntJoukko2.to_int_list()

        lista = sorted(a_lista + b_lista)
        for i in range(len(lista) - 1):
            if lista[i] == lista[i + 1]:
                self.lisaa(lista[i])


class Erotus(IntJoukko):
    def __init__(self, a: IntJoukko, b: IntJoukko):
        super(Erotus, self).__init__()
        self.IntJoukko1 = a
        self.IntJoukko2 = b
        self.muodosta_erotus()

    def muodosta_erotus(self):
        a_lista = sorted(self.IntJoukko1.to_int_list())
        b_lista = sorted(self.IntJoukko2.to_int_list())

        j = 0
        for i in range(len(a_lista)):
            while j < len(b_lista) - 1 and b_lista[j] < a_lista[i]:
                j += 1
            if a_lista[i] != b_lista[j]:
                self.lisaa(a_lista[i])
