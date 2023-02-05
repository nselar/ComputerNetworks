 #!/usr/bin/env python3
# -*- coding: utf-8 -*- 
""" 
Created on Wed Feb 17 14:26:39 2021 
@author: Alvaro Olmedo 
""" 
from pyModbusTCP.server import ModbusServer, DataBank 
from time import sleep 
from random import uniform 
# create an instance of Modbusserver 
server = ModbusServer("192.168.1.140", 23456, no_block=True) 
try:
    print("Start server...") 
    server.start() 
    print("Server is on line") 
    state = [0] 
    state = DataBank.get_words(15,5) 
    print("values of registers on 15 has changed to " + str(state)) 
    while True: 
     DataBank.set_words(0,[int(uniform(0,100))]) 
     if state != DataBank.get_words(1): 
         state = DataBank.get_words(1) 
         print("value register 1 has changed to " + str(state))
         sleep(0.5) 
except: 
 print("Shutdown server...") 
 server.stop() 
 print("Server is offline")

