import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipä", 5)

    # 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    # 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_niiden_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.hinta(), 8)

    # 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_kaksi_kertaa_tuotteen_hinta(
        self,
    ):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), self.maito.hinta() * 2)

    # 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(
        self,
    ):
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    # 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(
        self,
    ):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    # 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(
        self,
    ):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].lukumaara(), 2)

    # 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_ostos_jolla_sama_nimi_ja_lkm(
        self,
    ):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    # 13
    def test_jos_korissa_kaksi_samaa_tuotetta_poiston_jalkeen_ostosta_yksi_kpl(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    # 14
    def test_jos_korissa_oleva_tuote_poistetaan_kori_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

    # 15
    def test_metodi_tyhjenna_kori_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.tyhjenna()

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)
