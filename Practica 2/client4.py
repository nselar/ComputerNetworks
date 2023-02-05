#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:53:58 2022

@author: nicolassela
"""

from pyModbusTCP.client import ModbusClient 

client = ModbusClient(host="192.168.1.140", port=23456) 

client.open()
while True:
    address1 = 10; #Indice
    client.write_multiple_registers(address1, client.read_input_registers(0))
    address2 = 16   # Temperatura
    client.write_multiple_registers(address2, client.read_input_registers(1))
    normal=1
    alta=2
    baja=0
    
    #Comparacion temperatura
    if(client.read_holding_registers(1)[0] == 37):
        client.write_multiple_registers(15, normal)
    elif(client.read_holding_registers(1)[0] < 37):
        client.write_multiple_registers(15, baja)
    elif(client.read_holding_registers(1)[0] > 37):
        client.write_multiple_registers(15, alta)
        
    #Presion sistolica
    address4 = 19   
    client.write_multiple_registers(address4, client.read_input_registers(3))
        
    if(client.read_holding_registers(3)[0] == 120):
        client.write_multiple_registers(12, normal)
    elif(client.read_holding_registers(3)[0] < 120):
        client.write_multiple_registers(12, baja)
    elif(client.read_holding_registers(3)[0] > 120):
        client.write_multiple_registers(12, alta)
        
    address4 = 13   #Presion diastolica
    client.write_multiple_registers(address4, client.read_input_registers(5))
        
    if(client.read_holding_registers(5)[0] == 80):
        client.write_multiple_registers(14, normal)
    elif(client.read_holding_registers(5)[0] < 80):
        client.write_multiple_registers(14, baja)
    elif(client.read_holding_registers(5)[0] > 80):
        client.write_multiple_registers(14, alta)
    