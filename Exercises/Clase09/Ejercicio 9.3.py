# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:55:01 2021

@author: FEFe
"""

import fileparse
import lote

with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

# Para cada producto dentro del dict creo un lote. Hay 7 producto por ende se crea una lista con 7 lotes
camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]

# Se arma una lista con los costos de cada lote y se suman
costo = sum([c.costo() for c in camion])

