from controller.eenheid_controller import *
from time import sleep
from view.Dashboardview import Dashboardview

class meetController:
    def __init__(self):

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





# m = meetController()
# m.sla_waarde_op()


