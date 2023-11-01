import unittest
from statistics_service import StatisticsService,sort_by_points,SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_get_player_points(self):
        self.assertAlmostEqual(sort_by_points(Player("Selänne", "PIT", 45, 40)), 85)

    def test_search_returns_player(self):
        self.assertAlmostEqual(self.stats.search("Semenko").name, "Semenko")

    def test_search_returns_none_unknown_player(self):
        self.assertAlmostEqual(self.stats.search("Selänne"), None)

    def test_team_return_players(self):
        self.assertAlmostEqual([a.name for a in self.stats.team("EDM")].sort(), ["Semenko","Kurri","Gretzky"].sort())

    def test_top_players(self):
        self.assertAlmostEqual([a.name for a in self.stats.top(1,SortBy.POINTS)], ["Gretzky","Lemieux"])

    