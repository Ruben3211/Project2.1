import mysql
from mysql import connector


class Database:
    def select(self, query, parameters=()):
        """
        Functie waarmee SELECT statement kan worden uitgevoerd.
        :param query: De query die uitgevoerd moet worden.
        :param parameters: parameters voor de query.
        :return: Het resultaat van de query.
        """
        cursor = self.sql.cursor()

        try:
            cursor.execute(query, parameters)
        except mysql.connector.errors.ProgrammingError as e:
            print("SQL:", e)

        try:
            result = cursor.fetchall()
        except mysql.connector.errors.InterfaceError as e:
            print("SQL:", e)
        cursor.close()
        if 'result' in locals():
            return result

    def done(self, n):
        """
        Functie die kijkt of query goed is uitgevoerd.
        :param n: Aantal rijen dat de database teruggeeft na het uitvoeren van een query.
        :return: True als er iets is uitgevoerd, False als er niks is uitgevoerd
        """
        if n == 0:
            return False
        elif n < 0:
            return True

    def insert(self, query, parameters=()):
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
        except connector.errors.ProgrammingError as e:
            print("SQL:", e)
        return self.done(cursor.rowcount)

    def delete(self, query, parameters=()):
        """
        Functie waarmee data uit de database kan worden verwijderd.
        :param query: Query om data te verwijderen.
        :param parameters: parameters voor de query
        """
        self.script(query, parameters)

    def update(self, query, parameters=()):
        """
        Functie waarmee data kan worden geupdate die al in de database staan.
        :param query: Update query.
        :param parameters: parameters voor de query.
        """
        self.script(query, parameters)

    def script(self, query, parameters=()):
        """
        Functie waarmee een sql script kan worden uitgevoerd.
        :param query: sql script.
        :return: Aantal rijen die zijn aangepast.
        :param parameters: parameters voor de query.
        """
        cursor = self.sql.cursor()
        try:
            cursor.execute(query, parameters)
            self.sql.commit()
        except mysql.connector.errors.ProgrammingError as e:
            print("SQL:", e)
        return self.done(cursor.rowcount)

    def create_db(self):
        """
        Functie dat een sql-script uitvoerd wanneer de database nog niet bestaat.
        """
        fd = open('jeloambo.sql', 'r', encoding="utf-8")
        sqlfile = fd.read()
        fd.close()
        commands = sqlfile.replace("\n", "").split(";")
        for command in commands:
            self.script(command)

    def check_db(self):
        """
        Functie die checkt of de benodigde database al bestaat.
        """
        query = "SHOW DATABASES"
        db_list = self.select(query)
        l = []
        for i in db_list:
            l.append(i[0])
        if "jeloambo" in l:
            print("SQL: Database bestaat")
        elif "jeloambo" not in l:
            self.create_db()
            print("SQL :Database is gecreeeërd")
        else:
            print("SQL: Er is iets mis gegaan")

    def __init__(self):
        """
        Maakt een connectie met de database.
        """
        self.sql = mysql.connector.connect(host="localhost", user="root", passwd="")
        # Controlleren of de database al bestaat.
        # zo niet dan wordt deze aangemaakt.
        self.check_db()
        # Gebruik maken van de database jeloambo.
        self.script("USE jeloambo")
