#%% Abrir archivos comprimidos

import gzip

with gzip.open('Data/camion.csv.gz', 'rt') as f:
    for linea in f:
        print(linea, end= '')
        
        