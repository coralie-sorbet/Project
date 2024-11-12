import csv
import random
from player import Player
from team import Team
from league import League

# Function to read players from CSV and create Player objects
def load_players_from_csv(file_path):
    players = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                name = row['Name']
                skill_level = float(row['Skill level'])
                player = Player(name, skill_level)
                players.append(player)
    return players

# Function to initialize teams and assign players randomly
def initialize_teams(player_list):

    # Create 4 empty teams
    teams = [Team("Real Madrid"), Team("FC Barcelone"), Team("PSG"), Team("TFC")]
    
    # Shuffle the players and assign 3 players to each team
    random.shuffle(player_list)
    for i, player in enumerate(player_list):
        teams[i % len(teams)].add_player(player)

    return teams

# Function to run the simulation
def run_simulation():
    # Load players from CSV
    players = load_players_from_csv('players.csv')

    # Initialize teams and assign players
    teams = initialize_teams(players)

    # Create the league and add teams
    league = League()
    for team in teams:
        league.add_team(team)

    # Simulate the season
    league.play_season()

    # Get the results
    league.get_results()

    # Determine and print the champion
    champion_team = max(league.scores, key=league.scores.get)
    print(f"The league champion is {champion_team} with {league.scores[champion_team]} points!")

if __name__ == "__main__":
    run_simulation()