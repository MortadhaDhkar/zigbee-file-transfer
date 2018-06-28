# Xbee communication
from serial import Serial
from xbee import XBee 
from  base import *
from parameters import *

serial      = Serial(PORT,BAUDRATE)
xbee      = XBee(serial)

file_name = "test.jpg"
file_data = []
file_to_send = open(file_name, "rb")
chunk = file_to_send.read(NBR_BYTES_PER_PACKET)
while chunk:
    file_data.append(chunk)
    chunk = file_to_send.read(NBR_BYTES_PER_PACKET)
    
nbr_packets = len(file_data)
print("+ Sending Header")
payload = struct.pack(">B",0)+struct.pack(">I",nbr_packets)
xbee.tx(dest_addr=DESTINATION_ADDRESS,data=payload)
print("+ Sending File ..")
xbee_send_file(xbee,file_data)
print("+ Done")
xbee.halt()
serial.close()


'''
from serial import Serial
from xbee import XBee 

serial      = Serial('/dev/ttyUSB0',115200)
xbee      = XBee(serial,packet_handler)
payload = bytearray()
payload.append(1)
for v in b"Helllo":
    payload.append(v)


payload2 = bytearray()
payload2.append(2)
for v in b"world":
    payload2.append(v)
    
xbee.tx(dest_addr="\x00\x02",data=payload)    
xbee.tx(dest_addr="\x00\x02",data=payload2)


xbee.halt()
serial.close()
'''



'''

from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.devices import XBee64BitAddress
sync_ops_timeout = 5
device = XBeeDevice("/dev/ttyUSB0", 115200)
device.open()
payload = bytearray()
payload.append(5)

print(payload)
remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040E4DD23"))
device.send_data(remote_device,payload)
device.close()
'''














