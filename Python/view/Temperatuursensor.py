"""
In de klasse Temperatuursensor wordt een nieuwe Temperatuursensor aangemaakt en wordt de Sensor meegegeven.
Hierin worden alle Temperatuursensoren voorzien van de beginwaarden wanneer deze wordt aangemaakt.

Created: 08-11-2018
Author: Jeloambo
Version: 1.0
"""

from .Sensor import *


class Temperatuursensor(Sensor):
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
        super().__init__(tab, _soort='temperatuur', _bovengrens=20, _frequentie=5, _titel='Temperatuur', _eenheid=' graden celsius')
