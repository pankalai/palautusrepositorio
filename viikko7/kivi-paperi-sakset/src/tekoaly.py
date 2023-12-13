class Tekoaly:
    def __init__(self):
        self._siirto = 0
        self.siirrot = ["k", "p", "s"]

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        return self.siirrot[self._siirto]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
