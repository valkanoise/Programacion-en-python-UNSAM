# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:28:35 2021

@author: FEFe
"""

from vigilante import vigilar
import csv

lines = vigilar('../Data/mercadolog.csv')
# uso csv.reader para que los datos sean parseados y se arme por cada linea una []
rows = csv.reader(lines)
for row in rows:
    print(row)