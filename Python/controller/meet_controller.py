from controller.eenheid_controller import *
from time import sleep
class meetController:
    def __init__(self):

        self.e = eenheidController()
        self.eenheden = self.e.haal_eenheden()
        self.sla_waarde_op()

    def sla_waarde_op(self):
        while True:
            for t in self.eenheden:
                t.ontvang_sensor_waarde()
                print(t.waarde)
                if t.waarde > 40:
                    t.open_scherm()
                if t.waarde < 40:
                    t.sluit_scherm()
                sleep(5)
            q = "INSERT INTO j_values (value, datetime, unit_id) VALUES (%s, CURRENT_TIMESTAMP, %s)"
            for t in self.eenheden:
                p = (t.waarde, t.id)
                self.e.db.insert(q, p)


# m = meetController()
# m.sla_waarde_op()

