"""
SOCCER.io Shots

Eventos de chute
"""
from matplotlib.patches import FancyArrowPatch
from soccerio.data import Event


class Shot(Event):
    """Representa um chute"""

    def __init__(self, a, b, foot, **kwargs):
        if not foot in ["R", "L"]:
            raise ValueError("'foot' must be 'R' (right) or 'L' (left)")
        self.foot = foot
        defaultarc = "arc3,rad=%s" % (0.15 if foot == "R" else -0.15)

        arrowstyle = kwargs["arrowstyle"] if "arrowstyle" in kwargs else "-"
        linestyle = kwargs["linestyle"] if "linestyle" in kwargs else "-"
        connectionstyle = kwargs["connectionstyle"] if "connectionstyle" in kwargs else defaultarc

        patch = FancyArrowPatch(a, b, connectionstyle=connectionstyle, arrowstyle=arrowstyle,
                                linestyle=linestyle, mutation_scale=10)
        if "event_type" in kwargs:
            event_type = kwargs["event_type"]
            del kwargs["event_type"]
        else:
            event_type =  "shot"
        super(Shot, self).__init__(event_type, a, b, patch=patch, **kwargs)


class Goal(Shot):
    """
    Representa um chute que resultou em gol
    A região do gol pode ser:
    - TL = Topo esquerdo
    - TC = Topo (centro)
    - TR = Topo direito
    - ML = Meio esquerdo
    - MC = Meio (centro)
    - MR = Meio direito
    - BL = Baixo esquerdo
    - BC = Baixo (centro)
    - BR = Baixo direito
    """

    def __init__(self, a, region, foot, **kwargs):
        v = ["T", "M", "B"]
        h = ["L", "C", "R"]
        regions = ["".join(z) for y in [list(zip([x] * len(h), h)) for x in v] for z in y]
        if not region in regions:
            raise ValueError("Not a valid region, must be one of: %s" % regions)
        x = 48.34 if region[1] == "L" else 50 if region[1] == "C" else 51.66
        y = 5
        super(Goal, self).__init__(a, (x,y), foot, event_type="goal",
                                   arrowstyle="-|>,head_length=0.6,head_width=0.4", linestyle="-.",
                                   **kwargs)


class NonGoal(Shot):
    """Representa um chute que não é um gol e que pode ou não ter sido bem sucedido"""

    def __init__(self, a, b, foot, success=True, **kwargs):
        line = "-" if success else "--"
        self.success = success
        if "event_type" in kwargs:
            event_type = kwargs["event_type"]
            del kwargs["event_type"]
        else:
            event_type =  "nongoal"
        super(NonGoal, self).__init__(a, b, foot, event_type=event_type, linestyle=line, **kwargs)


class Pass(NonGoal):
    """Representa um passe"""

    def __init__(self, a, b, foot, success=True, **kwargs):
        super(Pass, self).__init__(a, b, foot, success, event_type="pass", **kwargs)


class Corner(NonGoal):
    """Representa um escanteio"""

    def __init__(self, a, b, foot, success=True, **kwargs):
        arrow = "->,head_length=0.6,head_width=0.4"
        super(Corner, self).__init__(a, b, foot, success, event_type="corner", arrowstyle=arrow,
                                     **kwargs)

class FreeKick(NonGoal):
    """Representa uma cobrança de falta"""

    def __init__(self, a, b, foot, success=True, **kwargs):
        arrow = "%s,head_length=0.6,head_width=0.4" % ("-|>" if success else "->")
        super(FreeKick, self).__init__(a, b, foot, success, event_type="corner", arrowstyle=arrow,
                                       **kwargs)


class Penalty(NonGoal):
    """Representa uma cobrança de penalti"""

    def __init__(self, a, b, foot, success=True, **kwargs):
        arrow = "%s,head_length=0.6,head_width=0.4" % ("-|>" if success else "->")
        super(Penalty, self).__init__(a, b, foot, success, event_type="penalty", arrowstyle=arrow,
                                      **kwargs)
