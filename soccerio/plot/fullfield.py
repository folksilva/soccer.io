"""
SOCCER.io FullField

Desenha um campo de futebol por completo no PyPlot
"""

from datetime import datetime
from matplotlib.patches import Rectangle, Circle, Arc, FancyArrowPatch, ArrowStyle
from matplotlib.lines import Line2D
from soccerio.plot import BaseField


class FullField(BaseField):
    """Desenha um campo de futebol completo e retorna a figura e o axis"""

    def __init__(self, title=None, home=None, away=None, **kwargs):
        super(BaseField, self).__init__()
        BaseField.__init__(self, title, **kwargs)
        self.home = home
        self.away = away
        now = datetime.now()

        simple_arrow_style = ArrowStyle("Simple", head_length=4, head_width=4)
        
        field = Rectangle((5, 5), 90, 120, facecolor=self.fc, edgecolor=self.ec)
        tr_corner = Arc((5,5), 2, 2, 0, 0, 90, color=self.ec)
        br_corner = Arc((5, 125), 2, 2, 270, 0, 90, color=self.ec)
        bl_corner = Arc((95, 125), 2, 2, 180, 0, 90, color=self.ec)
        tl_corner = Arc((95, 5), 2, 2, 90, 0, 90, color=self.ec)

        h_goal = Rectangle((46.34, 2.56), 7.32, 2.44, facecolor=self.fc, edgecolor=self.ec)
        h_penalty_area = Rectangle((29.84, 5), 40.32, 16.5, facecolor=self.fc, edgecolor=self.ec)
        h_box = Rectangle((40.84, 5), 18.32, 5.5, facecolor=self.fc, edgecolor=self.ec)
        h_penalty_mark = Circle((50, 16), 0.5, facecolor=self.ec, edgecolor=self.ec)
        h_penalty_arc = Arc((50, 16), 18.3, 18.3, 0, 37, 143, color=self.ec)
        h_arrow = FancyArrowPatch((95.8, 5), (95.8, 20), arrowstyle=simple_arrow_style, color="black")

        midway_circle = Circle((50, 65), 9.15, facecolor=self.fc, edgecolor=self.ec)
        midway_line = Line2D((5, 95), (65, 65), color=self.ec)
        midway_point = Circle((50, 65), 0.5, facecolor=self.ec, edgecolor=self.ec)

        a_goal = Rectangle((46.34, 125), 7.32, 2.44, facecolor=self.fc, edgecolor=self.ec)
        a_penalty_area = Rectangle((29.84, 108.5), 40.32, 16.5, facecolor=self.fc, edgecolor=self.ec)
        a_box = Rectangle((40.84, 119.5), 18.32, 5.5, facecolor=self.fc, edgecolor=self.ec)
        a_penalty_mark = Circle((50, 114), 0.5, facecolor=self.ec, edgecolor=self.ec)
        a_penalty_arc = Arc((50, 114), 18.3, 18.3, 180, 37, 143, color=self.ec)
        a_arrow = FancyArrowPatch((95.8, 125), (95.8, 110), arrowstyle=simple_arrow_style, color="black")

        now = datetime.now()

        self.ax.add_patch(field)
        self.ax.add_patch(tr_corner)
        self.ax.add_patch(br_corner)
        self.ax.add_patch(bl_corner)
        self.ax.add_patch(tl_corner)
        self.ax.add_patch(h_goal)
        self.ax.add_patch(h_penalty_area)
        self.ax.add_patch(h_box)
        self.ax.add_patch(h_penalty_mark)
        self.ax.add_patch(h_penalty_arc)
        self.ax.add_patch(midway_circle)
        self.ax.add_line(midway_line)
        self.ax.add_patch(midway_point)
        self.ax.add_patch(a_goal)
        self.ax.add_patch(a_penalty_area)
        self.ax.add_patch(a_box)
        self.ax.add_patch(a_penalty_mark)
        self.ax.add_patch(a_penalty_arc)
        self.ax.text(5, 125.5, u'SOCCER.io %s' % now.year, ha="right", va="top", size=8)

        if home:
            self.ax.text(96, 5, home, ha="right", va="top", size=10, rotation="vertical")
            self.ax.add_patch(h_arrow)

        if away:
            self.ax.text(96, 125, away, ha="right", va="bottom", size=10, rotation="vertical")
            self.ax.add_patch(a_arrow)



