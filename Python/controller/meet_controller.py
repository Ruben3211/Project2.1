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

    # def ontvang_sensor_waarde(self):
    #     for t in self.eenheden:
    #         if t.id == 1:
    #             t.stuur_sensor_waarde()
    #             return t.waarde
    #         if t.id == 3:
    #             t.stuur_sensor_waarde()
    #             return t.waarde



    # Aparte thread voor de loop
    def createThread(self):
        self.thread = Thread(target=self.loop)
        self.thread.setDaemon(True)
        self.thread.start()
        self.threadl = Thread(target=self.loopl)
        self.threadl.setDaemon(True)
        self.threadl.start()

    def loop(self):
        unit2 = self.eenheden[1]
        while unit2:
            for i in range(0, self.ontvang_temp_frequentie()):
                if self.ontvang_temp_switch() == True:
                    self.automatisch()
                else:
                    self.handmatig()
                print(i, self.ontvang_temp_frequentie() - 1, "temp")
                if i == self.ontvang_temp_frequentie() - 1:
                    unit2.stuur_sensor_waarde()
                    #self.sla_waarde_op(unit2.waarde)
                    self.dashboard.temperatuursensor.grafiek.variabele = unit2.waarde
                sleep(1)

    def loopl(self):
        unit1 = self.eenheden[0]
        while unit1:
            for i in range(0, self.ontvang_licht_frequentie()):
                if self.ontvang_licht_switch() == True:
                    self.automatisch()
                else:
                    self.handmatig()
                print(i, self.ontvang_licht_frequentie() - 1, "licht")
                if i == self.ontvang_licht_frequentie() - 1:
                    unit1.stuur_sensor_waarde()
                    #self.sla_waarde_op(unit1.waarde)
                    self.dashboard.lichtsensor.grafiek.variabele = unit1.waarde
                sleep(1)

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
        return self.dashboard.lichtsensor.oprollen

    #mode
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

    #mode
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

# m = meetController()
# m.sla_waarde_op()


