
# Project League Simulation
This project is a Python-based League Game Simulator that organizes players into teams and simulates a season of games. The results of each game are determined based on the skill levels of the players. At the end of the season, the league champion is announced.

## Project Structure

player.py: Defines the Player class with attributes for player name and skill level.
team.py: Defines the Team class, which holds a list of Player objects and manages adding and removing players.
league.py: Defines the League class, which manages teams, game simulations, and tracks scores across the season.
main.py: The entry point for running the simulation. It loads players from a CSV file, initializes teams, and simulates a season of games.
players.csv: A CSV file that contains player names and skill levels.
 
 ## Setup Instructions

 ### Step 1: Clone the Repository

 git clone https://github.com/coralie-sorbet/Project.git
 cd Project

 ### Step 2: Prepare the players.csv File
You can modify the player names and skill levels or add more players, but there should be at least 12 players for the simulation to work.

 ### Step 3: Run the Simulation
     
     1. run player.py
     2. run team.py
     3. run league.py
     4. run main.py

## Example Output
After running the simulation, you will see the results printed in the terminal, including the total points for each team and the league champion.

TFC has 10 points.
FC Barcelone has 8 points.
Real Madrid has 12 points.
PSG has 7 points.

The league champion is Real Madrid with 12 points!

## Error Handling
The program includes basic error handling for common issues:

If a player's skill level is invalid (e.g., not a number), the program will raise a ValueError for that specific player.
Missing headers such as Name or Skill level in the CSV file will raise a KeyError.
