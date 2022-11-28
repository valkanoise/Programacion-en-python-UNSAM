# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:01:17 2021

@author: FEFe
"""

class FormatoTabla(object):
    
    def encabezado(self, headers):
        headers = tuple(headers) # lo hago tuple para poder imprimirlo con el formato de abajo
        print('%10s %10s %10s %10s' % headers)
        print(('-'*10 + ' ')*len(headers))

    def fila(self, rowdata):
        rowdata = tuple(rowdata) # lo hago tuple para poder imprimirlo con el formato de abajo
        print('%10s %10s %10s %10s' % rowdata)

#%%
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
#%%        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
#%%        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def fila(self, data_fila):
        print('<tr>', end = '')
        for d in data_fila:
            print(f'<td>{d}</td>', end='')
        print('</tr>')