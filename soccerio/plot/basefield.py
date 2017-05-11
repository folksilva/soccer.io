"""
SOCCER.io BaseField

Estrutura base para um campo de futebol no PyPlot
"""

import matplotlib.pyplot as plt


class BaseField(object):
    """Base de campo de futebol

        title = Titulo do gráfico
        fieldcolor = Cor do fundo do campo
        linescolor = Cor das linhas do campo
        **kwargs = parâmetros adicionais que serão repassados para pyplot.figure()
    """

    def __init__(self, title=None, fieldcolor="#FAFAFA", linescolor="#9B9B9B", **kwargs):
        self.fig = plt.figure(**kwargs)
        if title:
            self.ax = plt.subplot(111, title=title, aspect="equal")
        else:
            self.ax = plt.subplot(111, aspect="equal")
        self.ax.set_xlim(100)
        self.ax.set_ylim(130)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.fc = fieldcolor
        self.ec = linescolor
        self.ax.axis("off")
        self.fig.subplots_adjust(hspace=0, wspace=0)

        self.teams = []
        self.players = []
        self.events = []
        

    def add_team(self, team, display=False, **kwargs):
        """
        Adiciona uma equipe ao campo

        Se team não for uma instância de soccerio.data.Team, cria uma nova instância
        usando team como name e **kwargs para os outros parâmetros.

        Se display for True, a equipe será incluída imediatamente na figura.
        """
        pass


    def add_player(self, player, display=False, **kwargs):
        """
        Adiciona um jogador ao campo

        Se player não for uma instância de soccerio.data.Player, cria uma nova instância
        usando player como name e **kwargs para os outros parâmetros.

        Se display for True, o jogador será incluído imediatamente na figura.
        """
        pass


    def add_event(self, event, display=False, **kwargs):
        """
        Adiciona um evento ao campo

        Se event não for uma instância de soccerio.data.Event, cria uma nova instância
        usando event como event_type e **kwargs para os outros parâmetros.

        Se display for True, o evento será incluído imediatamente na figura.
        """
        pass


    def display_players(self, team=None, legend=True, **kwargs):
        """
        Inclui na figura os jogadores do campo

        Se team for igual a None, todos os jogadores serão exibidos, as cores serão
        baseadas nas cores dos jogadores. Se team for uma string ou uma instância de
        soccerio.data.Team, apenas os jogadores dessa equipe serão exibidos, as 
        cores serão baseadas nas cores dos jogadores. Se team for uma lista de 
        strings ou uma lista de soccerio.data.Team, apenas os jogadores das equipes
        selecionadas serão exibidos, as cores serão baseadas nas cores dos jogadores.

        Se legend for True uma legenda será adicionada, usando **kwargs como parâmetros
        adicionais.
        """
        pass
        

    def display_events(self, player=None, event_type=None, color_by="player", legend=True, **kwargs):
        """
        Inclui na figura os eventos do campo

        Se player for igual a None, os eventos de todos os jogadores serão exibidos. 
        Se player for uma string ou uma instância de soccerio.data.Player, apenas 
        os eventos desse jogador serão exibidos. Se player for uma lista de strings 
        ou de soccerio.data.Player, apenas os eventos desses jogadores serão exibidos.

        Se event_type for igual a None, os eventos de todos os tipos serão exibidos.
        Se event_type for uma string, apenas os eventos desse tipo serão exibidos. Se
        event_type for uma lista de strings, apenas os eventos dos tipos selecionados
        serão exibidos.

        color_by permite escolher como os eventos terão as cores definidas:
         - player = As cores mudam de acordo com o jogador que realizou o evento
         - team = As cores mudam de acordo com a equipe que realizou o evento
         - event = As cores mudam de acordo com o tipo de evento

        Se legend for True, uma legenda será adicionada, usando **kwargs como
        parâmetros adicionais.
        """
        pass

