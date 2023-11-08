from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, playerReader: PlayerReader):
        self.stats = playerReader

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            filter(
                lambda player: player.nationality == nationality, self.stats.players
            ),
            reverse=True,
            key=lambda player: player.points,
        )
