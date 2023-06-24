class Scoreboard:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.balls = 0

    def update_score(self, runs):
        """
        Update the score on the scoreboard.
        """
        self.score += runs

    def update_wickets(self):
        """
        Update the number of wickets on the scoreboard.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the number of overs on the scoreboard.
        """
        self.balls += 1
        if self.balls == 6:
            self.overs += 1
            self.balls = 0

    def display_score(self):
        """
        Display the current score, wickets, and overs on the scoreboard.
        """
        return f"{self.score}/{self.wickets} ({self.overs}.{self.balls} overs)"
