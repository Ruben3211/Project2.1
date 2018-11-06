import mysql
from mysql import connector

class DB:
    def select(self, query):
        """
        Functie waarmee SELECT statement kan worden uitgevoerd.
        :param query: De query die uitgevoerd moet worden.
        :return: Het resultaat van de query.
        """
        cursor = self.sql.cursor()

        try:
            cursor.execute(query)
        except (mysql.connector.errors.ProgrammingError) as e:
            print(e)

        try:
            result = cursor.fetchall()
        except (mysql.connector.errors.InterfaceError) as e:
            print(e)
        cursor.close()
        if 'result' in locals():
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
        try:
            cursor.execute(query, parameters)
            self.sql.commit()
        except (mysql.connector.errors.ProgrammingError) as e:
            print(e)
        return self.done(cursor.rowcount)

    def delete(self, query):
        """
        Functie waarmee data uit de database kan worden verwijderd.
        :param query: Query om data te verwijderen.
        """
        self.script(query)

    def update(self, query):
        """
        Functie waarmee data kan worden geupdate die al in de database staan.
        :param query: Update query.
        """
        self.script(query)

    def script(self, query):
        """
        Functie waarmee een sql script kan worden uitgevoerd.
        :param query: sql script
        :return: Aantal rijen die zijn aangepast
        """
        cursor = self.sql.cursor()
        try:
            cursor.execute(query)
            self.sql.commit()
        except (mysql.connector.errors.ProgrammingError) as e:
            print(e)
        return self.done(cursor.rowcount)

    def createDB(self):
        """
        Functie dat een sql-script uitvoerd wanneer de database nog niet bestaat.
        :return:
        """
        fd = open('jeloambo.sql', 'r', encoding="utf-8")
        sqlFile = fd.read()
        fd.close()
        commands = sqlFile.replace("\n", "").split(";")
        for command in commands:
            self.script(command)

    def checkDB(self):
        """
        Functie die checkt of de benodigde database al bestaat.
        :return:
        """
        query = "SHOW DATABASES"
        db_list = self.select(query)
        l = []
        for i in db_list:
            l.append(i[0])
        if "jeloambo" in l:
            print("Database bestaat al")
        elif "jeloambo" not in l:
            self.createDB()
            print("Database is gecreeeërd")
        else:
            print("Er is iets mis gegaan")

    def __init__(self):
        """
        Maakt een connectie met de database
        """
        self.sql = mysql.connector.connect(host="localhost", user="root", passwd="")
        # Controlleren of de database al bestaat
        # zo niet dan wordt deze aangemaakt.
        self.checkDB()
        # Gebruik maken van de database jeloambo
        self.script("USE jeloambo")

db = DB()
print(db.select("SELECT name, FROM j_units"))
print(db.insert("SELECT"))
