"""
In de klasse Dashboardcontroller wordt een meetController aangemaakt.
Hierin wordt master(tk) meegegeven.

Created: 10-11-2018
Author: Jeloambo
Version: 1.0
"""

from controller.meet_controller import meetController


class Dashboardcontroller:
    def __init__(self, master):
        """
        :initialiseren van all klas variabelen
        :param meter: maakt een nieuwe meetController aan, waar de master wordt meegegeven
        """
        self.meter = meetController(master)
