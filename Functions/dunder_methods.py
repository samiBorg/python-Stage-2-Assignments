'''
Write a program illustrating example of each dunder menthods mentioned here in subtpoics:

- __str__, __repr__, __dir__ etc
-  __name__ == "__main__"
'''


class FootballTeam:
    def __init__(self, team_name, captain, score):
        self.team_name = team_name
        self.captain = captain
        self.score = score

    def __str__(self):
        return "Team: {}, captain: {}, score: {}".format(self.team_name, self.captain, self.score)

    def __repr__(self):
        return "FootballTeam({}, {}, {})".format(self.team_name, self.captain, self.score)

    def __add__(self, other):
        return self.score + other.score

    def __len__(self):
        return len(self.team_name)

    def __dir__(self):
        return [self.team_name, self.captain]


if __name__ == "__main__":

    brazil = FootballTeam("Brazil", "Ronaldo", 20)
    argentina = FootballTeam("Argentina", "Messi", 15)
    france = FootballTeam("France", "Mbappe", 22)

    print(brazil.__repr__())
    print(brazil.__str__())
    print("Score of teams brazil and argentina together: ", brazil + argentina)
    print("Length of the team name:", str(brazil), "= ", len(brazil))
    print(dir(france))
