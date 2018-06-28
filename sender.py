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
