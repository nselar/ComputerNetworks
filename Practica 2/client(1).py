# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:49:42 2022

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
    # Lectura de valores y escritora en la segunda direccion del banco
    client.write_multiple_registers(16,client.read_holding_registers(1));
    # Lectura de valores y escritura en la tercera direccion del banco
    client.write_multiple_registers(15,client.read_holding_registers(3));
    # Lectura de valores y escritura en la cuarta direccion del banco
    client.write_multiple_registers(19,client.read_holding_registers(5));
    