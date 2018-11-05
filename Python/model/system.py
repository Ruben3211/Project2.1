import serial
import struct

class system:
    def __init__(self, naam ,type, port):
        self.naam = naam
        self.type = type
        self.port = port
        self.ser = self.connect()

    def connect(self):
        ser = serial.Serial(port=self.port, baudrate=9600, bytesize=8, stopbits=2, xonxoff=False)
        print('verbonden met', self.naam)
        return ser

    def open_screen(self):
        self.ser.write(struct.pack('>B', 1))

    def close_screen(self):
        self.ser.write(struct.pack('>B', 2))

    def ontvang(self):
        nummer = self.ser.readline(2)
        return nummer

unit = system('test','2','com5')
print(unit)
while True:
    unit.ontvang()
    nummer = int(input("voer hier het commando in"))
    if nummer == 1:
        unit.open_screen()

    elif nummer == 2:
        unit.close_screen()

    elif nummer == 3:
        print(unit.ontvang())
