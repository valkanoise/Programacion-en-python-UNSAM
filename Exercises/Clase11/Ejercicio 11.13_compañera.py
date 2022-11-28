# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:31:30 2021

@author: FEFe
"""
 
def medidas_hoja_A(N, verbose = False):
    '''
    Ingresa nro entero N>0, indica hoja A(N)
    Devuelve medidas de la hoja formato tupla: medidas[0] = ancho // medidas[1] = largo 
    Dimensiones en mm
    '''
    
    if N == 0: # Caso base -- hoja A0
        ancho = 841
        largo = 1189 
        if verbose:
            print(f'A{N}-- ancho:{ancho}, largo:{largo}')
        return (ancho,largo)
    
    else:
        medidas = medidas_hoja_A(N-1) # Recursión
               
        if medidas[1] > medidas[0]:          
            medidas = (medidas[1]//2, medidas[0])
            if verbose:
                print(f'A{N}-- ancho:{medidas[0]}, largo:{medidas[1]}')
            
        elif medidas[1] < medidas[0]:
            medidas = medidas_hoja_A(N-1)
            medidas = (medidas[0]//2, medidas[1])
            if verbose:
                print(f'A{N}-- ancho:{medidas[0]}, largo:{medidas[1]}')
        
    return medidas