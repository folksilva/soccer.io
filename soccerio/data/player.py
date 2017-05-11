"""
SOCCER.io Player

Representa um jogador de futebol
"""
from soccerio.data import Team

class Player(object):
    """Um jogador de futebol"""
    
    def __init__(self, name, number=None, team=None, color=None, **kwargs):
        self.name = name
        self.number = number
        if isinstance(team, Team):
            self.team = team
        elif isinstance(team, str):
            self.team = Team(team, **kwargs)
        else:
            self.team = None
        self.color = color
