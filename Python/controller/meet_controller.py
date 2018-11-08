from controller.eenheid_controller import *
from time import sleep
from view.Dashboardview import Dashboardview

class meetController:
    def __init__(self, master):
        self.dashboard = Dashboardview(master)
        self.e = eenheidController()
        self.eenheden = self.e.haal_eenheden()
        self.loop()

    def sla_waarde_op(self, waarde):
        self.waarde = waarde
        q = "INSERT INTO j_values (value, datetime, unit_id) VALUES (%s, CURRENT_TIMESTAMP, %s)"
        for t in self.eenheden:
            p = (self.waarde, t.id)
            self.e.db.insert(q, p)

    def ontvang_sensor_waarde(self):
        for t in self.eenheden:
            t.ontvang_sensor_waarde()
            self.sla_waarde_op(t.waarde)

    def loop(self):
        while True:
            self.ontvang_sensor_waarde()
            self.ontvang_grenswaarde()
            sleep(5)

    def ontvang_grenswaarde(self):
        print(Dashboardview.temperatuursensor.bovengrens)

    def stuur_mode(self):
        return self.mode

    def stuur_meet_freq(self):
        return self.meet_freq

    def stuur_grenswaarde(self):
        return self.grenswaarde


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


# m = meetController()
# m.sla_waarde_op()


