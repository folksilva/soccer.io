"""
SOCCER.io Team

Representa uma equipe
"""

from soccerio.data import Model

class Team(Model):
    """Uma equipe de futebol"""

    def __init__(self, name, color=None, **kwargs):
        super(Team, self).__init__(**kwargs)
        self.name = name
        self.color = color
