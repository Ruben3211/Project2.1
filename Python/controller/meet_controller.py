from controller.eenheid_controller import *

class meetController:
    def __init__(self):

        self.e = eenheidController()
        self.eenheden = self.e.haal_eenheden()

    def sla_waarde_op(self):
        q = "INSERT INTO j_values (value, CURRENT_DATETIME, unit_id) VALUES (%s, %s)"
        for t in self.eenheden:
            # print(t.id)
            p = (t.waarde, t.id)
            self.e.db.insert(q, p)

m = meetController()
m.sla_waarde_op()
