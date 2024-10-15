class Player:
    def __init__(self, name, skill_level):
        if not isinstance(name, str):
            raise TypeError("Player name must be a string.")
        if not isinstance(skill_level, (int, float)):
            raise TypeError("Player skill level must be a number.")
        self.name = name
        self.skill_level = skill_level

    def __str__(self):
        return f"The player {self.name} has a skill level of {self.skill_level}."