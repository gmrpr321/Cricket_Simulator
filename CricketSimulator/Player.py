class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        """
        Initialize a player with the given stats.
        """
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience
        self.runs_scored = 0
        self.balls_faced = 0
        self.wickets_taken = 0
        self.catches_taken = 0

    def __str__(self):
        """
        Return the string representation of a player.
        """
        return self.name

    def bat(self, runs):
        """
        Update the player's batting statistics based on the runs scored.
        """
        self.runs_scored += runs
        self.balls_faced += 1

    def bowl(self, runs_conceded, wickets):
        """
        Update the player's bowling statistics based on the runs conceded and wickets taken.
        """
        self.runs_conceded += runs_conceded
        self.wickets_taken += wickets

    def field(self, catches):
        """
        Update the player's fielding statistics based on the number of catches taken.
        """
        self.catches_taken += catches

    def get_batting_average(self):
        """
        Calculate and return the batting average of the player.
        """
        if self.balls_faced > 0:
            batting_average = self.runs_scored / self.balls_faced
            return batting_average
        else:
            return 0.0

    def get_bowling_average(self):
        """
        Calculate and return the bowling average of the player.
        """
        if self.wickets_taken > 0:
            bowling_average = self.runs_conceded / self.wickets_taken
            return bowling_average
        else:
            return 0.0

    def get_catch_percentage(self):
        """
        Calculate and return the catch percentage of the player.
        """
        if self.catches_taken > 0:
            catch_percentage = (self.catches_taken / self.fielding) * 100
            return catch_percentage
        else:
            return 0.0
