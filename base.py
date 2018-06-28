from parameters import *
import struct
def xbee_send_file(xbee ,file_data):
    seq_n = 1
    for elem in file_data:
        payload= struct.pack(">B",55) \
                 + struct.pack(">I",seq_n) \
                 + elem
        xbee.tx(dest_addr=DESTINATION_ADDRESS,data=payload)
        seq_n+=1
        del payload