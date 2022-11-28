# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:25:20 2021

@author: FEFe
"""

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)


# Selecciono un fragmento de interes, contiene los datos de un día con 168 filas

dh = df['12-25-2014':].copy()

#%% 

# Hay que modificar delta_t (nro entero) y delta_h (float) para que ambas series sen lo mas parecidas
delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 18.2 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
