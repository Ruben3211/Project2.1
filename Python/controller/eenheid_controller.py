from model.database import Database
from model.eenheid import eenheid

class eenheidController:
    def __init__(self):
        self.db = Database()

    def haal_eenheden(self):
        # 0: id, 1: name, 2: type, 3: sensitivity, 4: measure_freq, 5: share_freq, 6: datetime_added, 7: manual, 8: port
        resultaat = self.db.select("SELECT id, name, type, port, measure_freq, sensitivity FROM j_units")
        eenheden = []
        for a in resultaat:
            eenheden.append(eenheid(a[0], a[1], a[2], a[3], a[4], a[5]))
            for t in eenheden:
                t.setup()
        return eenheden

    def nieuwe_eenheid(self, name, type, sensitivity, measure_freq, share_freq, manual, port):
        q = "INSERT INTO j_units(name, type, sensitivity, measure_freq, share_freq, datetime_added, manual, port) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, %s, %s)"
        p = (name, type, int(sensitivity), int(measure_freq), int(share_freq), int(manual), port)
        self.db.insert(q, p)

    def verwijder_eenheid(self, id):
        q = "DELETE FROM j_units WHERE id = '%s'"
        self.db.delete(q, (id,))


# new = eenheidController()
# for i in new.haal_eenheden():
#     for j in i:
#         print(j," ", end='')
#     print("\n")

# new.verwijder_eenheid(16)
# new.nieuwe_eenheid(3,2,4,1,4,5,"HOI")

