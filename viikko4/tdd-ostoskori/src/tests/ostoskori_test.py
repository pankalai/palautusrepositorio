import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)

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
        leipa = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_niiden_summa(self):
        leipa = Tuote("Leipä", 5)
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(), 8)

    # 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
