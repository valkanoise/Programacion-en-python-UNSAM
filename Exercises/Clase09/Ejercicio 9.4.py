# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:23:13 2021

@author: FEFe
"""

import costo_camion
import informe


a = costo_camion.costo_camion('../Data/camion.csv')
print('Costo camion = ', a, '\n')

informe.informe_camion('../Data/camion.csv', '../Data/precios.csv')