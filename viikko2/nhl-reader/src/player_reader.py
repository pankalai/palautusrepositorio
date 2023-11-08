from player import Player
import requests


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.get_players()

    def get_players(self):
        self.players = []
        for player_dict in requests.get(self.url).json():
            self.players.append(Player(player_dict))
