from controller.eenheid_controller import *
from time import sleep
from view.Dashboardview import Dashboardview
from threading import Thread

class meetController:
    def __init__(self, master):
        self.dashboard = Dashboardview(master)
        self.e = eenheidController()
        self.eenheden = self.e.haal_eenheden()
        self.createThread()

    def sla_waarde_op(self, waarde):
        self.waarde = waarde
        q = "INSERT INTO j_values (value, datetime, unit_id) VALUES (%s, CURRENT_TIMESTAMP, %s)"
        for t in self.eenheden:
            p = (self.waarde, t.id)
            self.e.db.insert(q, p)

    def ontvang_sensor_waarde(self):
        for t in self.eenheden:
            t.ontvang_sensor_waarde()
            #self.sla_waarde_op(t.waarde)
            return t.waarde

    # Running methods in Threads
    def createThread(self):
        self.thread = Thread(target=self.loop)
        self.thread.setDaemon(True)
        self.thread.start()
        print(self.thread)
        print('createThread():', self.thread.isAlive())

    def loop(self):
        while True:
            self.ontvang_sensor_waarde()
            self.dashboard.temperatuursensor.grafiek.variabele = self.ontvang_sensor_waarde()
            if self.ontvang_temp_switch() == True:
                self.automatisch()
            else:
                self.handmatig()
            sleep(self.ontvang_temp_frequentie())

    def ontvang_temp_bovengrens(self):
        return self.dashboard.temperatuursensor.bovengrens

    def ontvang_temp_frequentie(self):
        return self.dashboard.temperatuursensor.frequentie

    def ontvang_temp_switch(self):
        return self.dashboard.temperatuursensor.switch

    def ontvang_temp_oprollen(self):
        return self.dashboard.temperatuursensor.oprollen

    def ontvang_licht_bovengrens(self):
        return self.dashboard.lichtsensor.bovengrens

    def ontvang_licht_frequentie(self):
        return self.dashboard.lichtsensor.frequentie

    def ontvang_licht_switch(self):
        return self.dashboard.lichtsensor.switch

    def ontvang_licht_oprollen(self):
            for t in self.eenheden:
                if self.dashboard.lichtsensor.oprollen == True:
                    t.open_scherm()
                else:
                    t.sluit_scherm()
    #mode
    def automatisch(self):
        for t in self.eenheden:
            if self.ontvang_sensor_waarde() > self.ontvang_temp_bovengrens():
                t.open_scherm()
            elif self.ontvang_sensor_waarde() <= self.ontvang_temp_bovengrens():
                t.sluit_scherm()

    #mode
    def handmatig(self):
        for t in self.eenheden:
            if self.ontvang_temp_oprollen() == True:
                t.open_scherm()
            else:
                t.sluit_scherm()


# m = meetController()
# m.sla_waarde_op()


