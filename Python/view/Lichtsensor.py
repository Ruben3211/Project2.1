from .Sensor import *

class Lichtsensor(Sensor):
    def __init__(self, tab):
        # Maak object
        super().__init__(tab, _soort='lichtintensiteit', _bovengrens=40, _frequentie=30, _titel='Licht', _eenheid=' procent')


