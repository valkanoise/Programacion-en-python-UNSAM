# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:14:40 2021

@author: FEFe
"""

def medidas_hoja_A(N):
    
    # caso base
    if N == 0:
        # devuelve la tupla de A0 = (alto, ancho)
        alto = 841
        ancho = 1189
        medidas = alto, ancho
        return medidas
    
    # casos recursivos
    else:
        medidas = medidas_hoja_A(N-1)
        alto = medidas[0]
        ancho = medidas[1]
        
        # Determino quién es mayor, si alto o ancho y los divido por // 2
        if alto > ancho:
            medidas = (alto//2,ancho)
        
        else:
            medidas = (ancho//2, alto)
        
        return medidas
    
       
        