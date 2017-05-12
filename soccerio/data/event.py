"""
SOCCER.io Event

Um evento de jogo
"""

from soccerio.data import Model
from soccerio.data import Player


class Event(Model):
    """
    Um evento de jogo

    event_type: Tipo do evento
    a: Posição do evento ou do início do evento, tupla (x, y)
    b: Posição de término do evento
    player: Jogador que realizou o evento, se não for uma instância do soccerio.data.Player,
    cria uma nova instância usando esse valor como name e **kwargs como parâmetros adicionais
    """

    def __init__(self, event_type, a, b=None, player=None, **kwargs):
        super(Event, self).__init__(**kwargs)
        self.event_type = event_type
        if not isinstance(a, (tuple, list)):
            raise ValueError("parameter 'a' must be a tuple or list with x and y coordinates")
        self.a = a
        if b and not isinstance(b, (tuple, list)):
            raise ValueError("parameter 'b' must be a tuple or a list with x and y coordinates")
        self.b = b
        if isinstance(player, Player):
            self.player = player
        elif isinstance(player, str):
            self.player = Player(player, **kwargs)
        else:
            self.player = None
