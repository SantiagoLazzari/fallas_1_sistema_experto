from random import choice
from experta import *


class PreferedLandscape(Fact):
    """
    Info about the prefered landscape.
    possible options:
    - mountain
    - beach
    - city
    """
    pass


class TuristAgent(KnowledgeEngine):
    @Rule(PreferedLandscape(landscape='mountain'))
    def mountain(self):
        print("Bariloche")

    @Rule(PreferedLandscape(landscape='beach'))
    def red_light(self):
        print("Mar del plata")

engine = TuristAgent()
engine.reset()
prefered_landscape = PreferedLandscape(landscape = 'beach')
engine.declare(prefered_landscape)
engine.run()
