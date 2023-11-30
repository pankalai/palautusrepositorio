class TennisGame:
    points = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        self.score[player_name] += 1

    def get_score(self):
        diff = self.score[self.player1_name] - self.score[self.player2_name]

        if not self.is_endgame():
            if diff == 0:
                return self.points[self.score[self.player1_name]] + "-All"

            return (
                self.points[self.score[self.player1_name]]
                + "-"
                + self.points[self.score[self.player2_name]]
            )
        else:
            if diff == 0:
                return "Deuce"

            leader = self.player1_name if diff > 0 else self.player2_name
            if abs(diff) == 1:
                return "Advantage " + leader
            return "Win for " + leader

    def is_endgame(self):
        return (
            self.score[self.player1_name] >= 4
            or self.score[self.player2_name] >= 4
            or (self.score[self.player1_name] + self.score[self.player2_name] > 5)
        )
