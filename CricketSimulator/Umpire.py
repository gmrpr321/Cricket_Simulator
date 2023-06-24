import random


class Umpire:
    def __init__(self):
        """
        Initialize the umpire with scores, wickets, and overs.
        """
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.decision_log = []

    def signal_start_of_over(self):
        """
        Signal the start of an over.
        """
        print("Umpire: Start of over")

    def signal_end_of_ball(self):
        """
        Signal the end of a ball.
        """
        print("Umpire: End of ball")

    def signal_end_of_over(self):
        """
        Signal the end of an over.
        """
        print("Umpire: End of over")

    def predict_outcome(self):
        """
        Predict the outcome of a ball based on player stats.
        """
        outcomes = ["Dot ball", "Boundary", "Out", "Single", "Wide", "No ball", "six"]
        outcome = random.choice(outcomes)
        return outcome

    def get_score(self, outcome):
        """
        Make decisions on LBWs, catches, no-balls, wide-balls, etc and returns score
        """
        if outcome == "Dot ball":
            self.overs += 0.1
        elif outcome == "Boundary":
            self.score = 4
        elif outcome == "six":
            self.score = 6
        elif outcome == "Out":
            self.wickets = 1
        elif outcome == "Single":
            self.score = 1
        elif outcome == "Wide":
            self.score = 1
        elif outcome == "No ball":
            self.score = 1

        self.decision_log.append(outcome)
        return self.score

    def get_wickets(self):
        """
        Get the current number of wickets.
        """
        return self.wickets

    def get_overs(self):
        """
        Get the current number of overs.
        """
        return self.overs

    def get_decision_log(self):
        """
        Get the log of decisions made by the umpire.
        """
        return self.decision_log

    def reset_umpire(self):
        """
        Reset the umpire's state to start a new match or innings.
        """
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.decision_log = []
