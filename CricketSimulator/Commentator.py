from Scoreboard import Scoreboard


class Commentator:
    def __init__(self, match_stats):
        """
        Initialize the commentator with match statistics.
        """
        self.match_stats = match_stats
        self.scoreboard = Scoreboard()
        self.wickets = self.scoreboard.wickets
        self.over = self.scoreboard.overs
        self.score = self.scoreboard.score
        self.balls = self.scoreboard.balls

    def provide_commentary(self, ball_number, over_number):
        """
        Provide commentary for each ball and over.
        """
        self.scoreboard.update_score(self.score)
        self.scoreboard.update_wickets()
        self.scoreboard.update_overs()

        commentary = f"Ball {ball_number} of Over {over_number} - "
        commentary += f"Score: {self.scoreboard.display_score()}"

        return commentary

    def update_match_stats(self, wickets, over, score, balls):
        """
        Update the match statistics for the commentator.
        """
        self.wickets = wickets
        self.over = over
        self.score = score
        self.balls = balls

    def display_match_stats(self):
        """
        Display the current match statistics.
        """
        print(f"Match Statistics:")
        print(f"Score: {self.score}/{self.wickets}")
        print(f"Overs: {self.over}.{self.balls}")
