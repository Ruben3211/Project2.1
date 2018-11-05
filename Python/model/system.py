import serial
import struct


class eenheid:
    def __init__(self, naam ,type, poort):
        """
        initialiseren van all klas variabelen

        :param id: Uniek id voor een eenheid
        :param naam: naam van de eenheid
        :param type: type van de eenheid
        :param poort: de usb poort waarmee de eenheid verbing
        """

        self.naam = naam
        self.type = type
        self.poort = poort
        self.ser = self.connect()

    def connect(self):
        ser = serial.Serial(port=self.poort,
                            baudrate=9600,
                            bytesize=8,
                            stopbits=2,
                            xonxoff=False)

        print('verbonden met', self.naam)
        return ser

    def open_screen(self):
        self.ser.write(struct.pack('>B', 1))

    def close_screen(self):
        self.ser.write(struct.pack('>B', 2))

    def ontvang(self):
        
        nummer = self.ser.readline(2)
        return nummer

unit = eenheid('test','2','com5')
print(unit)
while True:
    unit.ontvang()
    nummer = int(input("voer hier het commando in"))
    def bit_to_int(self, ont):
        self.bit = ont
        nummer = int(self.bit)
        return nummer


eenheid = eenheid('test','2','com3')
print(eenheid)
while True:

    eenheid.ontvang()
    nummer = 3
    if nummer == 1:
        eenheid.open_screen()

    elif nummer == 2:
        eenheid.close_screen()

    elif nummer == 3:
        print(eenheid.bit_to_int(eenheid.ontvang()))
