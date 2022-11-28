# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:29:02 2021

@author: FEFe
"""

class Canguro(object):
    def __init__(self, nombre, contenido = []):
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy() # hay que copiar la lista sino la comparten todas las instancias de la clase Canguro
        
    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
        
    def __str__(self):
        return f'{self.nombre} tiene en su marsupio: {self.contenido_marsupio}'

if __name__ == '__main__':
        
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    
    print(madre_canguro)
    print(cangurito)