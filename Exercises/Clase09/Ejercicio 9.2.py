# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:44:21 2021

@author: FEFe
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        costo = self.cajones * self.precio
        return costo
    
    def vender (self, venta):
        self.cajones -= venta
        