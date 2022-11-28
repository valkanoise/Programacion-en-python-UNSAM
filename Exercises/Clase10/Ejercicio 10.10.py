# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:32:21 2021

@author: FEFe
"""

from vigilante import vigilar
import csv


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv') # productor
    rows = parsear_datos(lines) # procesamiento
    for row in rows: # consumidor
        print(row)