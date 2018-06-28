from uuid import uuid4
import struct
class Stream_handler:
    def __init__(self):
        self.nbr_packets =0
        self.file_name = str(uuid4())
        self.file_data = []
    def rcv_file_data(self,xbee_message):
        if xbee_message["rf_data"][0]==0:
            self.nbr_packets  = struct.unpack(">B",xbee_message["rf_data"][1])[0]        
        else:
            self.file_data.append(xbee_message["rf_data"][1:])
            index =struct.unpack(">B", xbee_message["rf_data"][0])[0]
            if index == self.nbr_packets:
                f = open(self.file_name, "ab")
                for e in self.file_data:
                    f.write(e)
                f.close()
                self.file_name = str(uuid4())
                
