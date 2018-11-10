"""
In de klasse eenheid kunnen meerdere bestuuringseenheden worden aangemaakt.
Deze eenheden halen de waarden van de arduino op en maken hiermee het product functioneel.

Created: 07-11-2018
Author: Jeloambo
"""

import serial
import struct
import time


class eenheid:
    def __init__(self, id, naam, sensor_type, poort, meet_freq, grenswaarde):
        """
        :initialiseren van all klas variabelen
        :param id: Uniek id voor een eenheid
        :param naam: naam van de eenheid
        :param sensor_type: type van de eenheid
        :param poort: de usb poort waarmee de eenheid verbind
        :param ser: de connectie naar de arduino
        :param grenswaarde: is de grenswaarde waarop de het scherm moet sluiten en openen
        :param meet_freq: meet frequentie voor het meten van de sensor waarden
        :param sensor_waarde: de waarde van de sensor
        """
        self.id = id
        self.naam = naam
        self.sensor_type = sensor_type
        self.poort = poort
        self.ser = self.connect()
        self.grenswaarde = grenswaarde
        self.meet_freq = meet_freq
        self.sensor_waarde = 0
        self.waarde = 0

    # maakt de connectie aan voor de besturingseenheid
    def connect(self):
        self.ser = serial.Serial(port=self.poort, baudrate=9600, bytesize=8, stopbits=2, xonxoff=True)

        print('verbonden met', self.naam)
        return self.ser

    # Open het scherm
    def open_scherm(self):
            self.ser.write(struct.pack('>B', 255))
            self.ser.write(struct.pack('>B', 1))

    # Sluit het scherm
    def sluit_scherm(self):
            self.ser.write(struct.pack('>B', 255))
            self.ser.write(struct.pack('>B', 2))

    # Haalt de sensor waarde op van de arduino via atmel
    def stuur_sensor_waarde(self):
        self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 4))
        self.waarde = self.ser.readline(2)
        self.waarde = self.bit_to_int(self.waarde)

    """
    Zet de waarde van bits om naar integers.
    :param ont: de bits die omgezet moeten worden.
    return: de integer waarde van de bits die worden meegegeven.
    """
    def bit_to_int(self, ont):
        self.bit = ont
        nummer = int(self.bit)
        return nummer

    # functie voor het opzetten van de connectie
    def setup(self):
        x = 0
        print(".")
        time.sleep(1)
        print("..")
        while x == 0:
            self.open_scherm()
            time.sleep(1)
            print("...")
            self.sluit_scherm()
            time.sleep(1)
            x += 1

        print("{} is gereed voor gebruik" .format(self.naam))
