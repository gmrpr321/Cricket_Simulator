# Cricket Simulation Module

## Introduction
The Cricket Simulation Module is a Python module that allows you to simulate cricket matches. It provides classes and functions to simulate the match, keep track of scores, provide commentary, and manage teams and players. This module can be used to create cricket simulations, analyze player and team performance, and generate match statistics.

## Files and Structure
The module consists of the following files:

- `Commentator.py`: Defines the `Commentator` class, which provides commentary for each ball and over of the match.
- `Field.py`: Defines the `Field` class, which represents the cricket field and stores information about its size, fan ratio, pitch conditions, and home advantage.
- `Match.py`: Defines the `Match` class, which simulates and keeps track of the current match statistics.
- `Player.py`: Defines the `Player` class, which represents a cricket player and stores their stats and performance.
- `Scoreboard.py`: Defines the `Scoreboard` class, which maintains the score, wickets, overs, and balls of the match.
- `Team.py`: Defines the `Team` class, which represents a cricket team and stores information about its players, captain, and current batting and bowling lineup.
- `Umpire.py`: Defines the `Umpire` class, which predicts the outcome of each ball and makes decisions on LBWs, catches, no-balls, wide-balls, etc.
- `Weather.py`: Defines the `Weather` class, which represents the weather conditions during the match.
- `main.py`: Contains the `simulate_match` function, which initializes the match, teams, players, and other components, and simulates the match by iterating over overs and balls.

## Class Descriptions

### Commentator Class
Description: This class provides commentary for each ball and over of the match based on the current match statistics.
Methods:
- `__init__(self, match_stats)`: Initializes the commentator with the match statistics.
- `provide_commentary(self, ball_number, over_number)`: Provides commentary for each ball and over.
- `update_match_stats(self, wickets, over, score, balls)`: Updates the match statistics for the commentator.
- `display_match_stats(self)`: Displays the current match statistics.

### Field Class
Description: This class represents the cricket field and stores information about its size, fan ratio, pitch conditions, home advantage, and weather conditions.
Methods:
- `__init__(self, size, fan_ratio, pitch_conditions, home_advantage)`: Initializes the field with the given parameters.
- `set_weather_conditions(self, weather_conditions)`: Sets the weather conditions for the field.
Getter methods:
- `get_field_size(self)`: Returns the size of the field.
- `get_fan_ratio(self)`: Returns the fan ratio for the field.
- `get_pitch_conditions(self)`: Returns the pitch conditions for the field.
- `get_home_advantage(self)`: Returns the home advantage for the field.
- `get_weather_conditions(self)`: Returns the weather conditions for the field.

### Match Class
Description: This class simulates and keeps track of the current match statistics.
Methods (continued):

#### Scoreboard-related methods:
- `update_wicket(self)`: Updates the wickets in the match and the scoreboard.
- `update_over(self)`: Updates the overs and balls in the match and the scoreboard.
- `update_match_stats(self)`: Updates the match statistics for the commentator and scoreboard.

#### Match simulation methods:
- `simulate_ball(self)`: Simulates a ball in the match by invoking the umpire's decision-making process, updating the match statistics, and providing commentary.
- `simulate_over(self)`: Simulates an over in the match by invoking the simulate_ball method for each ball in the over.
- `simulate_match(self)`: Simulates the entire match by iterating over overs and balls and updating the match statistics.

### Player Class
Description: This class represents a cricket player and stores their stats and performance.
Methods:
- `__init__(self, name)`: Initializes the player with the given name.
Getter and setter methods for player attributes such as name, batting average, bowling average, etc.

### Scoreboard Class
Description: This class maintains the score, wickets, overs, and balls of the match.
Methods:
- `__init__(self)`: Initializes the scoreboard with default values.
Getter and setter methods for scoreboard attributes such as score, wickets, overs, balls, etc.

### Team Class
Description: This class represents a cricket team and stores information about its players, captain, and current batting and bowling lineup.
Methods:
- `__init__(self, name, players, captain)`: Initializes the team with the given name, players, and captain.
- `get_next_batsman(self)`: Returns the next batsman in the batting lineup.
- `get_next_bowler(self)`: Returns the next bowler in the bowling lineup.
- `update_batting_order(self)`: Updates the batting order based on the current batsman.
- `update_bowling_order(self)`: Updates the bowling order based on the current bowler.
Getter methods for team attributes such as name, players, captain, batting lineup, bowling lineup, etc.

### Umpire Class
Description: This class predicts the outcome of each ball and makes decisions on LBWs, catches, no-balls, wide-balls, etc.
Methods:
- `__init__(self)`: Initializes the umpire.
- `make_decision(self)`: Makes a decision on the outcome of a ball (e.g., runs scored, wicket, no-ball, wide-ball).
Decision-related methods:
- `decide_runs(self)`: Decides the runs scored on a ball.
- `decide_wicket(self)`: Decides whether a wicket has been taken on a ball.
- `decide_no_ball(self)`: Decides whether a no-ball has been bowled.
- `decide_wide_ball(self)`: Decides whether a wide-ball has been bowled.

### Weather Class
Description: This class represents the weather conditions during the match.
Methods:
- `__init__(self, temperature, humidity)`: Initializes the weather with the given temperature and humidity.
Getter and setter methods for weather attributes such as temperature, humidity, etc.
