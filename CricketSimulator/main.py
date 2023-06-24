from Commentator import Commentator
from Field import Field
from Match import Match
from Player import Player
from Scoreboard import Scoreboard
from Team import Team
from Umpire import Umpire
from Weather import Weather


def simulate_match():
    # Create field and set weather conditions
    field = Field("Large", 0.8, "Dry", 0.2)
    weather = Weather("Sunny", 30, 10)
    field.set_weather_conditions(weather)

    # Create teams and players
    teamA = Team("Team A")
    teamB = Team("Team B")

    # Creating players for Team A
    player1 = Player("Player 1", 70, 80, 70, 80, 5)
    player2 = Player("Player 2", 50, 60, 60, 70, 3)
    player3 = Player("Player 3", 60, 70, 70, 80, 4)
    player4 = Player("Player 4", 40, 50, 60, 70, 2)
    player5 = Player("Player 5", 50, 60, 50, 60, 1)
    player6 = Player("Player 6", 55, 65, 55, 65, 1)
    player7 = Player("Player 7", 45, 55, 65, 75, 2)
    player8 = Player("Player 8", 65, 75, 75, 85, 5)
    player9 = Player("Player 9", 55, 65, 65, 75, 3)
    player10 = Player("Player 10", 60, 70, 70, 80, 4)
    player11 = Player("Player 11", 70, 80, 70, 80, 5)

    # Adding players to Team A
    teamA.add_player(player1)
    teamA.add_player(player2)
    teamA.add_player(player3)
    teamA.add_player(player4)
    teamA.add_player(player5)
    teamA.add_player(player6)
    teamA.add_player(player7)
    teamA.add_player(player8)
    teamA.add_player(player9)
    teamA.add_player(player10)
    teamA.add_player(player11)

    # Creating players for Team B
    player12 = Player("Player 12", 70, 80, 70, 80, 5)
    player13 = Player("Player 13", 50, 60, 60, 70, 3)
    player14 = Player("Player 14", 60, 70, 70, 80, 4)
    player15 = Player("Player 15", 40, 50, 60, 70, 2)
    player16 = Player("Player 16", 50, 60, 50, 60, 1)
    player17 = Player("Player 17", 55, 65, 55, 65, 1)
    player18 = Player("Player 18", 45, 55, 65, 75, 2)
    player19 = Player("Player 19", 65, 75, 75, 85, 5)
    player20 = Player("Player 20", 55, 65, 65, 75, 3)
    player21 = Player("Player 21", 60, 70, 70, 80, 4)
    player22 = Player("Player 22", 70, 80, 70, 80, 5)

    # Adding players to Team B
    teamB.add_player(player12)
    teamB.add_player(player13)
    teamB.add_player(player14)
    teamB.add_player(player15)
    teamB.add_player(player16)
    teamB.add_player(player17)
    teamB.add_player(player18)
    teamB.add_player(player19)
    teamB.add_player(player20)
    teamB.add_player(player21)
    teamB.add_player(player22)

    # Select captains
    teamA.select_captain(player1)
    teamB.select_captain(player16)

    # Create match and initialize match stats
    match = Match(teamA, teamB, field)
    match.update_score(0)
    # match.update_wicket()
    # match.update_overs()

    # Create scoreboard
    scoreboard = Scoreboard()

    # Create umpire
    umpire = Umpire()

    # Create commentator
    commentator = Commentator(match.get_match_stats())

    # Simulate the match
    for over in range(1, 6):
        umpire.signal_start_of_over()

        for ball in range(1, 7):
            # Provide commentary for each ball and over
            commentary = commentator.provide_commentary(ball, over)
            print(commentary)

            # Predict outcome and make decision
            outcome = umpire.predict_outcome()

            current_score = match.make_decision(outcome)

            # Update match stats
            print("\n", outcome, "\n", "Score :", current_score)

            match.update_score(current_score)
            if outcome == "out":
                match.update_wicket()
                scoreboard.update_wickets()

            match.update_overs()
            scoreboard.update_score(current_score)
            scoreboard.update_overs()

            # Update commentator's match stats
            commentator.update_match_stats(
                scoreboard.wickets, scoreboard.overs, scoreboard.score, ball
            )

            umpire.signal_end_of_ball()

        umpire.signal_end_of_over()

    # Display final match stats and scoreboard
    commentator.display_match_stats()
    scoreboard.display_score()


if __name__ == "__main__":
    simulate_match()
