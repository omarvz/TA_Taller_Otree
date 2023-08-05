from otree.api import *




doc = """
Este juego de negociación involucra a 3 jugadores. Cada uno exige una 
porción de cierta cantidad disponible. Si la suma de las demandas no 
es mayor que la cantidad disponible, ambos jugadores obtienen las 
porciones exigidas. De lo contrario, ambos no obtienen nada.
"""


class C(BaseConstants):
    NAME_IN_URL = 'bargaining'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 2  #Debe ser 10
    AMOUNT_SHARED = cu(150)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_requests = models.CurrencyField()


class Player(BasePlayer):
    request = models.CurrencyField(
        doc="""
        Monto solicitado por este jugador.
        """,
        min=0,
        max=C.AMOUNT_SHARED,
        label="Por favor, ingresa un monto del 0 al 100.",
    )


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    group.total_requests = sum([p.request for p in players])
    if group.total_requests <= C.AMOUNT_SHARED:
        for p in players:
            p.payoff = p.request
    else:
        for p in players:
            p.payoff = cu(0)


def other_player(player: Player):
    return player.get_others_in_group()[0]

def other_player2(player: Player):
    return player.get_others_in_group()[1]


# PAGES
class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Request(Page):
    form_model = 'player'
    form_fields = ['request']


class ResultsWaitPage(WaitPage):
    body_text = "Esperando que los otros jugadores realicen su demanda."
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(other_player_request=other_player(player).request,
                    other_player_request2=other_player2(player).request)


page_sequence = [Introduction, Request, ResultsWaitPage, Results]
