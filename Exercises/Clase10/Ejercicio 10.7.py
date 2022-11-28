# -*- coding: utf-8 -*-
"""
Para este ejercicio tiene que estár ejecutandose mediante linea de comando
el script que genera los datos todo el tiempo.

python3 sim_mercado.py

La función generadora vigilar aquí definida monitorea en tiempo real como se 
van generando los datos en tiempo real.
"""

# vigilante.py
import os
import time

def vigilar(archivo_log):
    ''' Funcion generadora que monitorea en tiempo real el archivo_log y
    devuelve mediante el comando yield la última linea generada en el
    archivo_log.
    '''
    
    f = open(archivo_log)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    
    while True:
        line = f.readline() # lee la ultima linea... si es vacía vuelve a iniciar el ciclo (continue)
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line
    

# # Prueba de monitoreo en tiempo real
# for line in vigilar('../Data/mercadolog.csv'):
#         print(line)

if __name__ == '__main__':
    
    import informe_final
    camion = informe_final.leer_camion ('../Data/camion.csv')
    
    for line in vigilar('../Data/mercadolog.csv'): # monitorea en 
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        
        # vigilar mira todas las lineas generadas, si aparece un producto que está en camion se imprimen sus datos
        if nombre in camion: 
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')