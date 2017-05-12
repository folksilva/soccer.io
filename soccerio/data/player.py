"""
SOCCER.io Player

Representa um jogador de futebol
"""

from soccerio.data import Model
from soccerio.data import Team

class Player(Model):
    """Um jogador de futebol"""

    def __init__(self, name, number=None, team=None, color=None, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.name = name
        self.number = number
        if isinstance(team, Team):
            self.team = team
        elif isinstance(team, str):
            self.team = Team(team, **kwargs)
        else:
            self.team = None
        self.color = color
