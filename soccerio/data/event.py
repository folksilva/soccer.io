"""
SOCCER.io Event

Um evento de jogo
"""

from soccerio.data import Player


class Event(object):
    """
    Um evento de jogo

    event_type: Tipo do evento
    a: Posição do evento ou do início do evento, tupla (x, y)
    b: Posição de término do evento
    event_result: Resultado do evento
    player: Jogador que realizou o evento, se não for uma instância do soccerio.data.Player,
    cria uma nova instância usando esse valor como name e **kwargs como parâmetros adicionais
    """

    def __init__(self, event_type, a, b=None, event_result=None, player=None, **kwargs):
        self.event_type = event_type
        if not isinstance(a, tuple) or not isinstance(a, list):
            raise ValueError("parameter 'a' have to be a tuple or list with x and y coordinates")
        self.a = a
        if b and not isintance(b, tuple) or not isinstance(b, list):
            raise ValueError("parameter 'b' have to be None, a tuple or a list with x and y coordinates")
        self.b = b
        event_result = event_result
        if isinstance(player, Player):
            self.player = player
        elif isinstance(player, str):
            self.player = Player(player, **kwargs)
        else:
            self.player = None
        self.start_arrow_style = kwargs["start_arrow_style"] if "start_arrow_style" in kwargs else None
        self.end_arrow_style = kwargs["end_arrow_style"] if "end_arrow_style" in kwargs else None
        self.connection_style = kwargs["connection_style"] if "connection_style" in kwargs else None
        self.patch = kwargs["patch"] if "patch" in kwargs else None

