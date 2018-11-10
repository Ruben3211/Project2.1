from .Sensor import *


class Temperatuursensor(Sensor):
    def __init__(self, tab):
        # Maak object
        self.animation = animation
        super().__init__(tab, _soort='temperatuur', _bovengrens=20, _frequentie=5, _titel='Temperatuur', _eenheid=' graden celsius')
