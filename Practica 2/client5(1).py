# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:51:25 2022

@author: nicks
"""

#(1) Importamos la libreria ModbusCliente 
from pyModbusTCP.client import ModbusClient 
#(2)Creamos el cliente ModbusTCP 
client = ModbusClient(host="192.168.1.140", port=23456) 
#(3)Conectamos el cliente ModbusTCP creado con el servidor ModbusTCP 
client.open() 


while True:
    # Lectura de indices y escritura en la primera direccion del banco
    client.write_multiple_registers(10,client.read_holding_registers(0));
    # Lectura de temperatura y escritura en la segunda direccion del banco
    client.write_multiple_registers(16,client.read_holding_registers(1));
    normal=1
    alterado=2
    #Temperatura
    if(client.read_holding_registers(16)[0] == 36 or client.read_holding_registers(16)[0] == 37):
        client.write_single_register(12,normal)
    else:
        client.write_single_register(12,alterado)
    #Presion sistolica
    client.write_multiple_registers(15,client.read_holding_registers(3));
    if(client.read_holding_registers(15)[0] >= 110 and client.read_holding_registers(15)[0] <= 130):
        client.write_single_register(12,normal)
    else:
        client.write_single_register(12,alterado)
    #Presion diastólica
    client.write_multiple_registers(19,client.read_holding_registers(5));
    if(client.read_holding_registers(19)[0] >= 70 and client.read_holding_registers(19)[0] <= 90):
        client.write_single_register(12,normal)
    else:
        client.write_single_register(12,alterado)