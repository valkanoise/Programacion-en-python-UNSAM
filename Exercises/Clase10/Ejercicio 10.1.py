# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:38:57 2021

@author: FEFe
"""

f = open('../Data/camion.csv')

it = f.__iter__()

print(next(it))
print(it.__next__())
print(next(it))