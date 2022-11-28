# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:32:25 2021

@author: FEFe
"""

import pandas as pd
import os
import seaborn as sns


# abro los datos y genero un data frame con todos los datos
directorio = '../Data'
archivo =  'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)


# Elijo columnas de interés y creo dataframe df_lineal
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]

# Cuento las especies
especies_mas_frecuentes = df_lineal['nombre_cientifico'].value_counts()
# Imprimo las 10 especies más frecuentes
print(especies_mas_frecuentes[0:10])

# Selecciono algunas especies de interés y armo un dataframe
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

# boxplot usando diametro a la altura del pecho
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

# Boxplot usando altura
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
