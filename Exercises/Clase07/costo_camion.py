# -*- coding: utf-8 -*-


import csv
import informe_final

def costo_camion(nombre_archivo):
        
    record = informe_final.leer_camion(nombre_archivo)
    costo_total = sum([fruta['cajones']*fruta['precio'] for fruta in record])
       
    return costo_total
 
    
def f_principal(lista_argv):

    
    #Levanto un error si se ingresan mal los datos requeridos
    if len(lista_argv) != 2:
        raise SystemExit('Error! Se requieren 2 parametros: \n 1.Nombre Script \n 2.Archivo_camion')
    
    print('Costo total:',costo_camion(lista_argv[1]))


#%% Ejecución por sys.argv y linea de comando

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    
    
#%% Prueba desde linea de comando interactiva (python3 -i)
'''
import costo_camion
costo_camion.f_principal(['costo_camion.py', '../Data/camion.csv'])
'''