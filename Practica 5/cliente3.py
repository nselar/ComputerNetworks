# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:14:29 2022

@author: nicks
"""

#(1) Importamos la libreria ModbusCliente 
from pyModbusTCP.client import ModbusClient 
#(2)Creamos el cliente ModbusTCP 
client = ModbusClient(host="10.196.9.84", port=23456) 
#(3)Conectamos el cliente ModbusTCP creado con el servidor ModbusTCP 
client.open() 

numero=28

while True:
    # Lectura del indice 
    client.write_multiple_registers(10,client.read_holding_registers(0))
    #Lectura del sensor de temperatura
    client.write_multiple_registers(11,client.read_holding_registers(1))
    #Lectura sensor presion sistolica
    client.write_multiple_registers(12,client.read_holding_registers(3))
    #Lectura sensor diastolica
    client.write_multiple_registers(13,client.read_holding_registers(5))
    # Escritura del numero X
    client.write_single_register(14,numero)