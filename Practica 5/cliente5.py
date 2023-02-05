# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:42:48 2022

@author: nicks
"""

#(1) Importamos la libreria ModbusCliente 
from pyModbusTCP.client import ModbusClient 
#(2)Creamos el cliente ModbusTCP 
client = ModbusClient(host="10.196.9.84", port=23456) 
#(3)Conectamos el cliente ModbusTCP creado con el servidor ModbusTCP 
client.open() 

index = client.read_holding_registers(0)[0]
temp = client.read_holding_registers(1)[0]
press = client.read_holding_registers(3)[0]
presd = client.read_holding_registers(5)[0]

alterado=2
normal=1

client.write_single_register(10,index)
client.write_single_register(11,temp)
if (temp==37 or temp==36):
   client.write_single_register(14,normal+28)
else:
    client.write_single_register(14,alterado+28)

client.write_single_register(12,press)
if (press>=110 and press<=130):
    client.write_single_register(14,normal+28)
else:
    client.write_single_register(14,alterado+28)

client.write_single_register(13,presd)
if (presd>=70 and presd<=90):
    client.write_single_register(14,normal+28)
else:
    client.write_single_register(14,alterado+28)