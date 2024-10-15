import numpy as np
from itertools import combinations

class League:
    def __init__(self):
        self.teams = []
        self.scores = {}

    def add_team(self, team):
        if not isinstance(team, Team):
            raise TypeError("Must add a Team object.")
        self.teams.append(team)
        self.scores[team.team_name] = 0

    def simulate_game(self, team1, team2):
        # Calculate the average skill level for each team
        team1_avg_skill = np.mean([player.skill_level for player in team1.players])
        team2_avg_skill = np.mean([player.skill_level for player in team2.players])

        # Add some randomness to the result
        team1_random = team1_avg_skill + np.random.normal(0, 5)
        team2_random = team2_avg_skill + np.random.normal(0, 5)

        # Determine the winner or if it's a tie
        if team1_random > team2_random:
            self.scores[team1.team_name] += 3
            print(f"{team1.team_name} wins against {team2.team_name}!")
        elif team2_random > team1_random:
            self.scores[team2.team_name] += 3
            print(f"{team2.team_name} wins against {team1.team_name}!")
        else:
            self.scores[team1.team_name] += 1
            self.scores[team2.team_name] += 1
            print(f"It's a tie between {team1.team_name} and {team2.team_name}!")

    def play_season(self):
        # Play games for all combinations of teams
        for team1, team2 in combinations(self.teams, 2):
            self.simulate_game(team1, team2)

    def get_results(self):
        print("League Results:")
        for team_name, score in self.scores.items():
            print(f"{team_name}: {score} points")