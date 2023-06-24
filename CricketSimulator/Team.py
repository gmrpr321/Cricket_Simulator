class Team:
    def __init__(self, name):
        """
        Initialize a team with the given name and an empty player list.
        """
        self.name = name
        self.players = []
        self.captain = None
        self.current_batsmen = []
        self.current_bowler = None
        self.bowler_log = []  # contains a tuple of player object and no of overs bowled
        self.batsmen_log = (
            []
        )  # contains a tuple of player object and wicket status (f-wicket, t-not wicket)

    def add_player(self, player):
        """
        Add a player to the team.
        """
        self.players.append(player)

    def remove_player(self, player):
        """
        Remove a player from the team.
        """
        if player in self.players:
            self.players.remove(player)

    def select_captain(self, captain):
        """
        Select a captain for the team.
        """
        if captain in self.players:
            self.captain = captain

    def get_player_stats(self, player):
        """
        Retrieve the stats of a specific player in the team.
        """
        if player in self.players:
            return player.stats
        return None

    def get_team_stats(self):
        """
        Calculate and return the overall team statistics.
        """
        total_runs = 0
        total_wickets = 0
        total_batting_points = 0
        total_bowling_points = 0

        for player in self.players:
            total_runs += player.stats["runs"]
            total_wickets += player.stats["wickets"]
            total_batting_points += player.batting
            total_bowling_points += player.bowling

        average_batting_score = total_runs / len(self.players)
        average_bowling_points = total_bowling_points / len(self.players)

        team_stats = {
            "total_runs": total_runs,
            "total_wickets": total_wickets,
            "average_batting_score": average_batting_score,
            "average_bowling_points": average_bowling_points,
        }

        return team_stats

    def make_substitution(self, out_player, in_player):
        """
        Perform a player substitution, replacing an outgoing player with an incoming player during a match.
        """
        if out_player in self.players and in_player not in self.players:
            index = self.players.index(out_player)
            self.players[index] = in_player

    def choose_batsmen(self):
        """
        Choose the next batsmen, the batsman with higher batting point has higher priority.
        """
        temp_players_list = list(self.players)
        calc_list = []
        # Extract the batting points for each player
        for i in range(len(temp_players_list)):
            calc_list.append((temp_players_list[i].batting, i))
        calc_list = sorted(calc_list)
        current_batsman = temp_players_list[calc_list[0][1]]
        for player in self.batsmen_log:
            if player[1] and (not current_batsman == player[0]):
                current_batsman = player[0]
                break

        self.current_batsmen.append(current_batsman)

    def auto_choose_bowler(self):
        """
        Choose a bowler for the next over.
        """
        temp_players_list = list(self.players)
        calc_list = []
        # Extract the bowling points for each player
        for i in range(len(temp_players_list)):
            calc_list.append((temp_players_list[i].bowling, i))
        calc_list = sorted(calc_list)
        current_bowler = temp_players_list[calc_list[0][1]]
        for player in self.bowler_log:
            if player[1] < 30 and (not current_bowler == player[0]):
                current_bowler = player[0]
                break

        self.current_bowler = current_bowler

    def choose_bowler(self, player):
        self.current_bowler = player

    def reset_team(self):
        """
        Reset the team's current batsmen, bowler, and logs to their initial state.
        """
        self.current_batsmen = []
        self.current_bowler = None
        self.bowler_log = []
        self.batsmen_log = []

    def display_team(self):
        """
        Display the team's name, players, captain, current batsmen, and current bowler.
        """
        print(f"Team: {self.name}")
        print("Players:")
        for player in self.players:
            print(player.name)
        print("Captain:", self.captain.name if self.captain else "None")
        print("Current Batsmen:")
        for batsman in self.current_batsmen:
            print(batsman.name)
        print("Current Bowler:")
        print(self.current_bowler.name if self.current_bowler else "None")

    def get_player_count(self):
        """
        Return the number of players currently in the team.
        """
        return len(self.players)

    def is_team_complete(self):
        """
        Check if the team has a full roster of players or if any positions are vacant.
        """
        return len(self.players) == 11
