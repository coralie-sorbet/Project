from player import Player

class Team:


    def __init__(self, team_name):
        if not isinstance(team_name, str):
            raise TypeError("Team name must be a string.")
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Must add a Player object.")
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            raise ValueError("Player not found in the team.")

    def __str__(self):
        players_str = ', '.join([player.name for player in self.players])
        return f"Team {self.team_name} has players: {players_str}"