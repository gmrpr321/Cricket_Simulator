from Umpire import Umpire
from Commentator import Commentator
from Scoreboard import Scoreboard


class Match:
    """
    A class to simulate and keep track of current match stats
    """

    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.current_inning = 1
        self.umpire = Umpire()
        self.scoreboard = Scoreboard()
        self.commentator = Commentator(
            {
                self.scoreboard.score,
                self.scoreboard.wickets,
                self.scoreboard.overs,
                self.scoreboard.balls,
            }
        )

    def update_score(self, runs):
        """
        Update the score in the match and the scoreboard.
        """
        self.scoreboard.update_score(runs)

    def update_wicket(self):
        """
        Update the wickets in the match and the scoreboard.
        """
        self.scoreboard.update_wickets()

    def update_overs(self):
        """
        Update the overs in the match and the scoreboard.
        """
        self.scoreboard.update_overs()

    def get_match_stats(self):
        """
        Get the current match statistics.
        """
        return {
            "score": self.scoreboard.score,
            "wickets": self.scoreboard.wickets,
            "overs": self.scoreboard.overs,
            "balls": self.scoreboard.balls,
        }

    def display_scoreboard(self):
        """
        Display the current score on the scoreboard.
        """
        self.scoreboard.display_score()

    def provide_commentary(self, ball_number, over_number):
        """
        Provide commentary for each ball and over.
        """
        return self.commentator.provide_commentary(ball_number, over_number)

    def predict_outcome(self):
        """
        Predict the outcome of a ball based on player stats.
        """
        return self.umpire.predict_outcome()

    def make_decision(self, outcome):
        """
        Make decisions on LBWs, catches, no-balls, wide-balls, etc.
        """
        return self.umpire.get_score(outcome)

    def display_match_stats(self):
        """
        Display the current match statistics.
        """
        self.commentator.display_match_stats()
