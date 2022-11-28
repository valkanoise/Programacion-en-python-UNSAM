# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:04:30 2021

@author: FEFe
"""

'''
Definí una función llamada archivos_png(directorio) que arme una lista 
de todos los archivos .png que se encuentren en algún subdirectorio 
directorio dado.
'''
import os

  
def archivos_png(directorio):
    '''
    Arma una lista de todos los archivos .png que se encuentren en algún 
    subdirectorio / directorio dado.
    '''
    
    lista_archivos = []
    for root, dirs, files in os.walk(directorio):
       for name in files:
           if 'png' in name:
               lista_archivos.append(name)

    return lista_archivos

# Código para funcionar desde linea de comando y recibiendo y parámetro
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        raise SystemExit(f'ERROR: Este script precisa un parametro conteniendo un directorio')
    else:
        print(archivos_png(sys.argv[1]))
        
### Para que funcione hay que ejecutar por linea de comando:
### python3 listar_imgs.py ../Data/ordenar