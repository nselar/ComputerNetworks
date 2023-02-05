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
    lectura=0

    while True:
        lectura=lectura+1
        DataBank.set_words(0,[lectura])
        DataBank.set_words(1,[int(uniform(35,43))])
        DataBank.set_words(3,[int(uniform(100,140))])
        DataBank.set_words(5,[int(uniform(60,100))])

        if state != DataBank.get_words(0,20):
            state = DataBank.get_words(0,20)
            print("records that change " + str(state))
            sleep(2.5)
except:
    print("Shutdown server...")
    server.stop()
    print("Server is offline")

