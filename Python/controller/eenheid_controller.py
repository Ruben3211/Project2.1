"""
In de klasse eenheidController wordt een nieuwe Database aangemaakt. Hier worden alle eenheden die
opgeslagen staan in de database opgehaald en in een list gezet.

Created: 07-11-2018
Author: Jeloambo
Version: 1.0
"""

from model.database import Database
from model.eenheid import eenheid

class eenheidController:
    def __init__(self):
        """
        :initialiseren van all klas variabelen
        :param db: Hier wordt een nieuwe Database aangemaakt
        """
        self.db = Database()

    """
    Hier worden alle eenheden, met de bijbehorende variabelen, uit de database gehaalt.
    Deze waarden worden daarna in een list gezet.
    
    :return: de eenheden die uit de database zijn gehaalt in een list.
    """
    def haal_eenheden(self):
        # 0: id, 1: name, 2: type, 3: sensitivity, 4: measure_freq, 5: share_freq, 6: datetime_added, 7: manual, 8: port
        resultaat = self.db.select("SELECT id, name, type, port, measure_freq, sensitivity FROM j_units")
        eenheden = []
        for a in resultaat:
            eenheden.append(eenheid(a[0], a[1], a[2], a[3], a[4], a[5]))
        for t in eenheden:
            t.setup()
        return eenheden

    """
    Maakt een nieuwe eenheid aan met meegegeven variabelen.
    
    :param name: de naam van de eenheid.
    :param type: het type van de eenheid.
    :param sensitivity: de bovengrens van de eenheid.
    :param measure_freq: de meet frequentie van de eenheid.
    :param manual: de mode van de eenheid.
    :param port: de poort waarop de eenheid is aangesloten. 
    """
    def nieuwe_eenheid(self, name, type, sensitivity, measure_freq, manual, port):
        q = "INSERT INTO j_units(name, type, sensitivity, measure_freq, share_freq, datetime_added, manual, port) VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, %s, %s)"
        p = (name, type, int(sensitivity), int(measure_freq), int(manual), port)
        self.db.insert(q, p)

    """
    Verwijderd een eenheid met het meegegeven id.

    :param id: het id van de eenheid.
    """
    def verwijder_eenheid(self, id):
        q = "DELETE FROM j_units WHERE id = '%s'"
        self.db.delete(q, (id,))
