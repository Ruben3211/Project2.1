import mysql
from mysql import connector

class DB:
    def __init__(self):
        """
        Maakt een connectie met de database zodra de klasse DB wordt aangemaakt
        """
        self.sql = mysql.connector.connect(host="localhost", user="root", passwd="")

    def select(self, query):
        """
        Functie waarmee SELECT statement kan worden uitgevoerd.
        :param query: De query die uitgevoerd moet worden.
        :return: Het resultaat van de query.
        """
        cursor = self.sql.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def done(self, n):
        """
        Functie die kijkt of query goed is uitgevoerd.
        :param n: Aantal rijen dat de database teruggeeft na het uitvoeren van een query
        :return: True als er iets is uitgevoerd, False als er niks is uitgevoerd
        """
        if n == 0:
            return False
        elif n < 0:
            return True

    def insert(self, query, parameters):
        """
        Functie waarmee data in de database kan worden gezet.
        :param query: De query voor het toevoegen van data.
        :param parameters: De waarden die in de database moeten komen.
        :return: Het aantal rijen dat in de database is geplaatst.
        """
        cursor = self.sql.cursor()
        cursor.execute(query, parameters)
        self.sql.commit()
        return self.done(cursor.rowcount)

    def delete(self, query):
        """
        Functie waarmee data uit de database kan worden verwijderd.
        :param query: Query om data te verwijderen.
        :return: Het aantal rijen dat verwijderd is.
        """
        cursor = self.sql.cursor()
        cursor.execute(query)
        self.sql.commit()
        return self.done(cursor.rowcount)

    def update(self, query):
        """
        Functie waarmee data kan worden geupdate die al in de database staan.
        :param query: Update query.
        :return: Aantal rijen dat geupdate is.
        """
        cursor = self.sql.cursor()
        cursor.execute(query)
        self.sql.commit()
        return self.done(cursor.rowcount)

    def script(self, query):
        cursor = self.sql.cursor()
        cursor.execute(query)
        self.sql.commit()
        return self.done(cursor.rowcount)

    def createDB(self):
        fd = open('jeloambo.sql', 'r', encoding="utf-8")
        sqlFile = fd.read()
        fd.close()
        commands = sqlFile.replace("\n", "").split(";")
        # print(sqlFile)
        for command in commands:
            self.script(command)

    def checkDB(self):
        query = "SHOW DATABASES"
        db_list = self.select(query)
        l = []
        for i in db_list:
            l.append(i[0])
        if "jeloambo" in l:
            print("Database bestaat al")
        elif "jeloambo" not in l:
            self.createDB()
        else:
            print("Er is iets mis gegaan")



db = DB()
db.checkDB()
