from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    edad = models.IntegerField(label='¿Cuál es tu edad?', min=18, max=100)
    
    carrera = models.StringField(
        label='¿Qué carrera estudia?'
    )
    
    ciclo_estudios = models.StringField(
        choices=[['VII', 'VII'], ['VIII', 'VIII'], ['IX', 'IX'], ['X', 'X']],
        label='¿En qué ciclo de estudio se encuentra?',
        widget=widgets.RadioSelect,
    )
    
    especialidad = models.StringField(
        label='¿Qué especialidad estudia?'
    )


# FUNCTIONS
# PAGES
class Encuesta(Page):
    form_model = 'player'
    form_fields = ['edad']


class Estudios(Page):
    form_model = 'player'
    form_fields = ['carrera', 'ciclo_estudios', 'especialidad']


page_sequence = [Encuesta, Estudios]
