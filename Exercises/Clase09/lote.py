# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:44:21 2021

@author: FEFe
"""
# si una clase no tiene clase base se suele usar 'object' como clase base
class Lote(object):
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    
    def costo(self):
        costo = self.cajones * self.precio
        return costo
    
    def vender (self, ncajones):
        self.cajones -= ncajones
        