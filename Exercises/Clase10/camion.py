# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:06:19 2021

@author: FEFe
"""

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, index):
        return self.lotes[index]

    # Este metodo permite buscar nombres en el camion ej 'Lima' in camion -> True
    def __contains__(self, nombre):
        # return any([lote.nombre == nombre for lote in self.lotes]) # usando comprension de listas
        return any(lote.nombre == nombre for lote in self.lotes) # usando expresión generadora

    
    def __repr__(self):
        return f'Camion({self.lotes})'
    
    def __str__(self):
        texto = f'Camion con {self.__len__()} lotes:'
        for lote in self.lotes:
            texto +='\n'+f"Lote de {lote.cajones} cajones de '{lote.nombre}', pagados a ${lote.precio} cada uno"
        
        return texto

    def precio_total(self):
        # return sum([l.costo() for l in self.lotes]) # usando comprensión de listas
        return sum(l.costo() for l in self.lotes) # usando expresión generadora

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
        