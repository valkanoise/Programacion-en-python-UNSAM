# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:38:39 2021

@author: FEFe
"""

def es_potencia(n,b):
    # Casos base
    if n== 1:
        return True
    if n < 1:
        return False
    
    # ciclos recursivos
    else:
        return es_potencia(n/b, b)
    