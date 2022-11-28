import seaborn as sns
import numpy as np
import pandas as pd
import os

#%% 1 

# Defino directorio y nombre de cada set de datos, ambos están en el mismo dir
directorio = '../Data'
archivo_arbolado_parques = 'arbolado-en-espacios-verdes.csv'
archivo_arbolado_veredas = 'arbolado-publico-lineal-2017-2018.csv'

# Armo el path para cada uno de los sets de datos
fname_parques = os.path.join(directorio,archivo_arbolado_parques)
fname_veredas = os.path.join(directorio,archivo_arbolado_veredas)

# Genero los data frames para cada uno de los sets de datos
df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)


#%% 2

# Selecciono columnas de interes según el DataFrame dado que usan distintos nombres para las columnas
cols_parques = ['altura_tot', 'diametro', 'nombre_cie']
cols_veredas = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']

# Selecciono las filas referidas a las Tipas y las columnas de interes y armo dataframes nuevos usando metodo copy()
# Cada dataframe llama distinto a las tipas
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_veredas].copy()

# Cambio nombres a las columas de los dataframes para que tengan los mismos nombres en las columnas altura y diamtero
df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura"})
df_tipas_veredas = df_tipas_veredas.rename(columns={"altura_arbol": "altura", "diametro_altura_pecho": "diametro"})

#%% 3

# Agrego columna ambiente a los dataframes, a cada uno le agrego un vector generado con np con la longitud de cada dataframe
df_tipas_parques['ambiente'] = np.array(['parques']*len(df_tipas_parques))
df_tipas_veredas['ambiente'] = np.array(['vereda']*len(df_tipas_veredas))

#%% 4

# Juntos los dataframes de Tipas para parques y veredas
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#%% 5

df_tipas.boxplot('diametro',by = 'ambiente') # no hay diferencias en el diametro de las tipas según el ambiente
df_tipas.boxplot('altura',by = 'ambiente') # las tipas crecen más altos en los parques

