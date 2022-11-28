'''Se modifica el script para que tome datos con columnas en distinto orden.
Para ello el script usarÃ¡ ZIP para crear dict y poder trabajar con KEY 
y no por su posiciÃ³n en el archivo csv.'''

import csv
import informe_funciones

def costo_camion(nombre_archivo):
    ''' 
    Función que calcula el costo del camion. Para ello se remite a dos
    modulos. En primer lugar al modulo informe_funciones que a su vez 
    se remite al modulo fileparse con su función parse_csv para crear la 
    variable record. 
    La variable record es una lista que contiene varios diccionarios, 
    cada uno con información relativa a una fruta {nombre, cajones, precio}.
    '''
        
    record = informe_funciones.leer_camion(nombre_archivo)
    costo_total = sum([fruta['cajones']*fruta['precio'] for fruta in record])
       
    return costo_total
 
#%% Prueba

# if __name__=='__main__':
#     costo = costo_camion('../Data/camion.csv')
#     print('Costo total:', costo)
