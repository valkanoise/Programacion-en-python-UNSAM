# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:25:40 2021

@author: FEFe
"""
import os
import time

def vigilar(archivo_log):
    ''' Funcion generadora que monitorea en tiempo real el archivo_log y
    devuelve mediante el comando yield la última linea generada en el
    archivo_log.
    '''
    
    f = open(archivo_log)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF, con esto readline() siempre lee la ultima linea
    
    while True:
        line = f.readline() # lee la ultima linea... si es vacía vuelve a iniciar el ciclo (continue)
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line
        
        
def filematch(lines, substr):
    ''' funcion que busca la presencia de un substring en lines.
    si el substr está presente se imprime esa linea'''
        for line in lines:
            if substr in line:
                yield line
                
                
lines = vigilar('../Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja') 
for line in naranjas:
    print(line)