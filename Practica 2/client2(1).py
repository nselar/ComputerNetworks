# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:35:30 2022

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
    normal=2
    alta=3
    baja=1
    #Temperatura
    if(client.read_holding_registers(16)[0] == 36):
        client.write_single_register(15,normal)
    elif(client.read_holding_registers(16)[0] < 36):
        client.write_single_register(15,baja)
    elif(client.read_holding_registers(16)[0] > 36):
        client.write_single_register(15,alta)
    #Presion sistolica
    client.write_multiple_registers(19,client.read_holding_registers(3));
    if(client.read_holding_registers(19)[0] == 120):
        client.write_single_register(12,normal)
    elif(client.read_holding_registers(19)[0] < 120):
        client.write_single_register(12,baja)
    elif(client.read_holding_registers(19)[0] > 120):
        client.write_single_register(12,alta)
    #Presion diastólica
    client.write_multiple_registers(13,client.read_holding_registers(5));
    if(client.read_holding_registers(13)[0] == 80):
        client.write_single_register(14,normal)
    elif(client.read_holding_registers(13)[0] < 80):
        client.write_single_register(14,baja)
    elif(client.read_holding_registers(13)[0] > 80):
        client.write_single_register(14,alta)