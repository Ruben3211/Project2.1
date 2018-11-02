import serial
# class system:
#     def __init__(self,name ,type):
#         self.name
#         self.type
#         self.port
#     def connect(self):
#         ser = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='PARITY_NONE', stopbits='STOPBITS_TWO', xonxoff=False)
#
#         print('verbonden met' )
#         return ser
#
#     def open_screen(self):
#
#     def close_screen(self):


ser = serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity='n', stopbits=2 ,xonxoff=0)
print(ser)
while True:
    nummer = int(input("voer hier het commando in"))
    ser.write(nummer)

