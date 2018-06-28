from time import sleep
import serial
from xbee import XBee
from uuid import uuid4
import struct


BAUDRATE             = 57600
PORT                 = '/dev/ttyUSB0'

serial_port = serial.Serial(PORT, BAUDRATE)


class Stream_handler:
    def __init__(self):
        self.nbr_packets =0
        self.file_name = str(uuid4())
        self.file_data = []
    def rcv_file_data(self,xbee_message):
        if xbee_message["rf_data"][0]=='\x00':
            self.nbr_packets  = struct.unpack(">I",xbee_message["rf_data"][1:5])[0]
        else:
            self.file_data.append(xbee_message["rf_data"][5:])
            index =struct.unpack(">I", xbee_message["rf_data"][1:5])[0]
            if index == self.nbr_packets:
                print ("writing to file")
                f = open(self.file_name, "wb")
                for e in self.file_data:
                    f.write(e)
                f.close()
                self.file_name = str(uuid4())

stream = Stream_handler()
xbee = XBee(serial_port, callback=stream.rcv_file_data)

while True:
    try:
        sleep(1)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()
