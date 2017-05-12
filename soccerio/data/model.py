"""
SOCCER.io Model

Modelo base da estrutura de dados
"""

class Model(object):
    """Modelo base para estruturas de dados"""

    def __init__(self, **kwargs):
        self.patch = kwargs["patch"] if "patch" in kwargs else None
