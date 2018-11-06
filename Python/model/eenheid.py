import serial
import struct


class eenheid:
    def __init__(self, id, naam, type, poort): #grenswaarde, meet_freq, deel_freq, datum_toe):
        """
        initialiseren van all klas variabelen
        :param id: Uniek id voor een eenheid
        :param naam: naam van de eenheid
        :param type: type van de eenheid
        :param poort: de usb poort waarmee de eenheid verbing
        """
        self.id = id
        self.naam = naam
        self.type = type
        self.poort = poort
        self.ser = self.connect()
        # self.grenswaarde = grenswaarde
        # self.meet_freq = meet_freq
        # self.deel_freq = deel_freq
        # self.datum = datum_toe

    #def update(self):


    def connect(self):
        ser = serial.Serial(port=self.poort,
                            baudrate=9600,
                            bytesize=8,
                            stopbits=2,
                            xonxoff=False)

        print('verbonden met', self.naam)
        return ser

    def open_screen(self):
        # self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 1))

    def close_screen(self):
        # self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 2))

    def verander_mode(self):
        self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 3))

    def stuur_sensor_type(self):
        self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 4))
        self.ser.write(struct.pack('>B', self.meet_freq))

    def stuur_meet_freq(self):
        self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 5))
        self.ser.write(struct.pack('>B', self.meet_freq))

    def stuur_grens_waarde(self):
        # stuur een nieuwe waarde voor wanneer het roluik omhoog en naar beneden moet gaan
        self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 6))
        self.ser.write(struct.pack('>B', self.grenswaarde))

    def stuur_deel_freq(self):
        self.ser.write(struct.pack('>B', 255))
        self.ser.write(struct.pack('>B', 7))
        self.ser.write(struct.pack('>B', self.deel_freq))


    def ontvang(self):
        nummer = self.ser.readline(2)
        return nummer

    def bit_to_int(self, ont):
        self.bit = ont
        nummer = int(self.bit)
        return nummer

eenheid = eenheid(1, 'test', '2', 'com3')
print(eenheid)
while True:

    nummer = input("commando")
    #eenheid.ontvang()
    if nummer == 1:
        eenheid.open_screen()

    elif nummer == 2:
        eenheid.close_screen()

    elif nummer == 3:
        print(eenheid.bit_to_int(eenheid.ontvang()))