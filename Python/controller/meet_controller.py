"""
In de klasse meet_controller worden nieuwe Dashboardviews en eenheidControllers aangemaakt.
De master wordt hier doorgegeven aan Dashboardview. Alle waarden van het Dashboard worden hier opgevraagd
en maken met deze waarden het programma interactief.

Created: 10-11-2018
Author: Jeloambo
Version: 1.2.6
"""

from controller.eenheid_controller import *
from time import sleep
from view.Dashboardview import Dashboardview
from threading import Thread

class meetController:
    def __init__(self, master):
        """
        :initialiseren van all klas variabelen.
        :param dashboard: hier wordt een nieuw Dashboardview aangemaakt en de master wordt meegegeven.
        :param e: maakt een nieuwe eenheidController aan.
        :param eemheden: haalt een list op van alle eenheden en de waarden daarvan.
        :param createThread: met deze functie worden de threads aangemaakt
        """
        self.dashboard = Dashboardview(master)
        self.e = eenheidController()
        self.eenheden = self.e.haal_eenheden()
        self.createThread()

    # stopt de waarden van de sensoren in de database
    def sla_waarde_op(self):
        for t in self.eenheden:
            q = "INSERT INTO j_values (value, datetime, unit_id) VALUES (%s, CURRENT_TIMESTAMP, %s)"
            p = (t.waarde, t.id)
            self.e.db.insert(q, p)

    # Maakt een thread aan per eenheid
    def createThread(self):
        self.threadtemp = Thread(target=self.loop_temperatuursensor)
        self.threadtemp.setDaemon(True)
        self.threadtemp.start()
        self.threadlicht = Thread(target=self.loop_lichtsensor)
        self.threadlicht.setDaemon(True)
        self.threadlicht.start()

    # Een loop voor het programma voor de temperatuursensor
    def loop_temperatuursensor(self):
        x = True
        unit2 = self.eenheden[1]
        y = 0
        while x:
            for i in range(0, 61):
                print(y, "t")
                if self.ontvang_temp_switch() == True:
                    self.automatisch()
                else:
                    self.handmatig()
                if y == self.ontvang_temp_frequentie() - 1:
                    unit2.stuur_sensor_waarde()
                    self.dashboard.temperatuursensor.grafiek.variabele = unit2.waarde
                    y = 0
                    sleep(1)
                    continue
                y += 1
                sleep(1)
            self.sla_waarde_op()

    # Een loop voor het programma vam de lichtsensor
    def loop_lichtsensor(self):
        x = True
        unit1 = self.eenheden[0]
        while x:
            for i in range(0, self.ontvang_licht_frequentie()):
                print(i, "l")
                if self.ontvang_licht_switch() == True:
                    self.automatisch()
                else:
                    self.handmatig()
                if i == self.ontvang_licht_frequentie() - 1:
                    unit1.stuur_sensor_waarde()
                    self.dashboard.lichtsensor.grafiek.variabele = unit1.waarde
                    sleep(1)
                    continue
                x = True
                sleep(1)


    """
    Haalt de bovengrens waarde op van het dashboard van de temperatuursensor
    :return: de bovengrens van de temperatuursensor
    """
    def ontvang_temp_bovengrens(self):
        return self.dashboard.temperatuursensor.bovengrens

    """
    Haalt de frequentie op van het dashboard van de temperatuursensor
    :return: de frequentie van de temperatuursensor
    """
    def ontvang_temp_frequentie(self):
        return self.dashboard.temperatuursensor.frequentie

    """
    Haalt de handmatig/automatische knop waarde op van het dashboard van de temperatuursensor
    :return: de switch waarde van de temperatuursensor
    """
    def ontvang_temp_switch(self):
        return self.dashboard.temperatuursensor.switch

    """
    Haalt de oprol/uitrol knop waarde op van het dashboard van de temperatuursensor
    :return: de oprol/uitrol waarde van de temperatuursensor
    """
    def ontvang_temp_oprollen(self):
        return self.dashboard.temperatuursensor.oprollen

    """
    Haalt de bovengrens waarde op van het dashboard van de lichtsensor
    :return: de bovengrens van de lichtsensor
    """
    def ontvang_licht_bovengrens(self):
        return self.dashboard.lichtsensor.bovengrens

    """
    Haalt de frequemtie waarde op van het dashboard van de lichtsensor
    :return: de frequentie van de lichtsensor
    """
    def ontvang_licht_frequentie(self):
        return self.dashboard.lichtsensor.frequentie

    """
    Haalt de handmatig/automatische knop waarde op van het dashboard van de lichtsensor
    :return: de switch waarde van de lichtsensor
    """
    def ontvang_licht_switch(self):
        return self.dashboard.lichtsensor.switch

    """
    Haalt de oprol/uitrol knop waarde op van het dashboard van de lichtsensor
    :return: de oprol/uitrol waarde van de lichtsensor
    """
    def ontvang_licht_oprollen(self):
        return self.dashboard.lichtsensor.oprollen

    # Wanneer het programma op automatisch staat, wordt hier gekeken naar de temperatuur en de bovengrens.
    # om de rolluik automatisch open en dicht te laten gaan.
    def automatisch(self):
        unit1 = self.eenheden[0]
        unit2 = self.eenheden[1]
        if self.ontvang_licht_switch() == True:
            if unit1.waarde > self.ontvang_licht_bovengrens():
                unit1.open_scherm()
                self.dashboard.lichtsensor.uitrollenFunc()
            elif unit1.waarde <= self.ontvang_licht_bovengrens():
                unit1.sluit_scherm()
                self.dashboard.lichtsensor.oprollenFunc()

        if self.ontvang_temp_switch() == True:
            if unit2.waarde > self.ontvang_temp_bovengrens():
                unit2.open_scherm()
                self.dashboard.temperatuursensor.uitrollenFunc()
            elif unit2.waarde <= self.ontvang_temp_bovengrens():
                unit2.sluit_scherm()
                self.dashboard.temperatuursensor.oprollenFunc()

    # Wanneer het porgramma op handmatig staat, wordt hier gekeken wanneer er een knop wordt ingedrukt
    # om de rolluik handmatig open en dicht te laten gaan.
    def handmatig(self):
        unit1 = self.eenheden[0]
        unit2 = self.eenheden[1]
        if self.ontvang_licht_switch() == False:
            if self.ontvang_licht_oprollen() == True:
                unit1.open_scherm()
            else:
                unit1.sluit_scherm()

        if self.ontvang_temp_switch() == False:
            if self.ontvang_temp_oprollen() == True:
                unit2.open_scherm()
            else:
                unit2.sluit_scherm()
