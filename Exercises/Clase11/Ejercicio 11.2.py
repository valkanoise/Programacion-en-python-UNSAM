# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:28:40 2021

@author: FEFe
"""

def triangular(n):
    '''
    Función que calcula recursivamente el n-ésimo número triangular de n
    '''

    if n == 0:
        num_trian = 0
        return num_trian
    
    else:
        num_trian = n + triangular(n - 1)        
        return num_trian
        