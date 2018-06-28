#message format {'id': 'rx', 'rf_data': b'\x02world', 'options': b'\x00', 'source_addr': b'\x00\x02', 'rssi': b'7'}
'''
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.devices import XBee64BitAddress

def data_received_callback(xbee_message):
    address = xbee_message.remote_device.get_64bit_addr()
    data = xbee_message.data
    f = open("HELLO","wb")
    print("Received data from %s: %s" % (address, data))
    #f.write(data)
    f.close()
    
device = XBeeDevice("/dev/ttyUSB0", 115200)
device.open()


device.add_data_received_callback(data_received_callback)
'''

import serial
import time
from   xbee import XBee
import Stream_handler


serial_port = serial.Serial('/dev/ttyUSB0', 57600)

stream = Stream_handler()
xbee = XBee(serial_port, callback=stream.rcv_file_data)


while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()

'''
import serial
import time
from xbee import XBee

serial_port = serial.Serial('/dev/ttyUSB0', 115200)

def print_data(data):
    print (data["rf_data"])

xbee = XBee(serial_port, callback=print_data)

while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()
'''
