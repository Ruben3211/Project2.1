"""
In de klasse Lichtsensor wordt een nieuwe Lichtsensor aangemaakt en wordt de Sensor meegegeven.
Hierin worden alle Lichtsensoren voorzien van de beginwaarden wanneer deze wordt aangemaakt.

Created: 08-11-2018
Author: Jeloambo
Version: 1.0
"""

from .Sensor import *


class Lichtsensor(Sensor):
    def __init__(self, tab):
        """
        :initialiseren van all klas variabelen.
        :param tab: is het tablad welke wordt meegegeven.
        :param _soort: hetgene wat de sensor meet.
        :param _bovengrens: de aangegeven bovengrens waarbij de rolluik open of dicht moet gaan.
        :param _frequentie: de meet frequentie.
        :param _titel: de titel van het venster.
        :param _eenheid: de waarde waarin gemeten wordt.
        """
        super().__init__(tab, _soort='lichtintensiteit', _bovengrens=40, _frequentie=5, _titel='Licht', _eenheid=' procent')
