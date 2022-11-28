# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:41:11 2021

@author: FEFe
"""

import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
from formato_tabla import crear_formateador, imprimir_tabla

formateador = crear_formateador('txt')
imprimir_tabla(camion, ['nombre','precio','cajones'], formateador)
