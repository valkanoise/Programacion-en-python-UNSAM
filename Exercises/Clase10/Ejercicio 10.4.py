# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:02:55 2021

@author: FEFe
"""
def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

for line in open('../Data/camion.csv'):
        print(line, end='')

print()
print('############')
print()

for line in filematch('../Data/camion.csv', 'Naranja'):
        print(line, end='')
