# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:33:32 2022

@author: nicks
"""

#(1) Importamos la libreria ModbusCliente 
from pyModbusTCP.client import ModbusClient 
#(2)Creamos el cliente ModbusTCP 
client = ModbusClient(host="10.196.9.84", port=23456) 
#(3)Conectamos el cliente ModbusTCP creado con el servidor ModbusTCP 
client.open() 

temp = client.read_holding_registers(1)[0]
press = client.read_holding_registers(3)[0]
presd = client.read_holding_registers(5)[0]

if (temp==37):
   client.write_single_register(12,2+28)
elif(temp>37):
   client.write_single_register(12,3+28)
else:
    client.write_single_register(12,1+28)

client.write_single_register(13,press)
if (press==120):
    client.write_single_register(14,2+28)
elif(press>120):
    client.write_single_register(14,3+28)
else:
    client.write_single_register(14,1+28)

client.write_single_register(15,presd)
if (presd==80):
    client.write_single_register(16,2+28)
elif(presd>80):
    client.write_single_register(16,3+28)
else:
    client.write_single_register(16,1+28)