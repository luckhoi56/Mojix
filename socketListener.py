import socket
import xml.etree.ElementTree as ET
import time
import sys
import pandas as pd
from lxml import etree
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.50.42', 3177))
t_end = time.time() + 3 # 10 seconds
epc_lst =[]
rssi_lst= []
port_lst =[]
mux_lst =[]
ts_lst =[]
while time.time() < t_end:
    data = s.recv(1500)

    data = data.split('\n',4)[-1]
    if (data =="\n\n"):
        continue;
    else:
        try:
            tree = ET.ElementTree (ET.fromstring(data))
        except ET.ParseError as err:
            print("Sorry, wrong formet")
            print (data)
            continue
    root = tree.getroot()
    #print (root)


    #append to a list


    epc_lst.append(root[5][2][3][0][5][1].text)
    rssi_lst.append(root[5][2][3][0][5][2][1].text.split(':')[1])
    port_lst.append(root[5][2][3][0][5][2][3].text.split(':')[1])
    mux_lst.append(root[5][2][3][0][5][2][4].text.split(':')[1])
    ts_lst.append(root[5][2][3][0][5][2][0].text.split(':')[1])
#doc = etree.parse('data')

list_of_lists = [epc_lst, rssi_lst, port_lst, mux_lst, ts_lst]

#for a in zip (*list_of_lists):
 #   print(a)

data = dict (list_of_lists)
df = pd.DataFrame(data)
print(df)