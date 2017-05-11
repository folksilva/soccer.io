"""
SOCCER.io Team

Representa uma equipe
"""

class Team(object):
    """Uma equipe de futebol"""

    def __init__(self, name, color=None):
        self.name = name
        self.color = color
