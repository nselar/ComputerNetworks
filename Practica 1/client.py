#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
""" 
Created on Wed Feb 17 14:26:39 2021 
@author: Alvaro Olmedo 
""" 
#Las pruebas de conexión desde el cliente ModbusTCP al servidor ModbusTCP 
#Se realizaron mediante los siguientes pasos: 
 
#(1) Importamos la libreria ModbusCliente 
from pyModbusTCP.client import ModbusClient 
#(2)Creamos el cliente ModbusTCP 
client = ModbusClient(host="192.168.1.140", port=23456) 
#(3)Conectamos el cliente ModbusTCP creado con el servidor ModbusTCP 
client.open() 
#(4)Realizamos diferentes pruebas como por ejemplo: 
#Prueba(1) realizadas hacia el servidor ModbusTCP 
client.read_holding_registers(0) 
#Prueba(2) realizadas hacia el servidor ModbusTCP 
client.write_single_register(1,55) 
#Prueba(3) realizadas hacia el servidor ModbusTCP 
client.write_multiple_registers(1,[1, 2, 3])

# 6.1
#client.write_multiple_registers(5,[1, 2, 3, 4, 5])
#print("value registers for 6.1 are " + str(client.read_holding_registers(5,5)))

# 6.2
#client.write_multiple_registers(10,[1, 2, 3, 4, 5])
#print("value registers for 6.2 are " + str(client.read_holding_registers(10,5)))

#6.3
client.write_multiple_registers(15,[1, 2, 3, 4, 5])
print("value registers for 6.3 are" + str(client.read_holding_registers(5,5)))

j=0
for i, val in enumerate(client.read_holding_registers(15,5)):
    j=val+j
    if val % 2 == 0:
        print("Value " + str(val) + " is even")
    else:
        if val == 0:
            print ("Value 0 is even")
        else:
            print("Value " + str(val) + " is odd")

if j % 2 == 0:
    print("The sum of the register values ​​is even: " + str(j))
else:
    if val == 0:
        print ("Value 0 is even")
    else:
        print("The sum of the register values ​​is odd:  " + str(j))
