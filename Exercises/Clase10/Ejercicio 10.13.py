# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:13:06 2021

@author: FEFe
"""

nums = [1, 2, 3, 4, 5]
cuadrados = (x*x for x in nums)
cuadrados
# <generator object <genexpr> at 0x109207e60>
for n in cuadrados:
    print(n)
 
# si volves a iterar sobre cuadrados no devuelve nada porque ya corriste antes
for n in cuadrados:
    print(n)