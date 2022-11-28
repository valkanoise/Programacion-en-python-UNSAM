


cadena = 'Geringoso'
# inicio una variable string vacía dado que variable cadena NO es mutable
capadepenapa = ''

#itero sobre cada letra y construte un nuevo string "capadepenapa", si aparece una vocal
# la reemplaza por 'apa', 'epe', 'ipi', 'opo' o 'upu'.

for c in cadena:
    if c == 'a':
        c = 'apa'
        capadepenapa = capadepenapa + c
    
    elif c == 'e':
        c = 'epe'
        capadepenapa = capadepenapa + c
        
    elif c == 'i':
        c = 'ipi'
        capadepenapa = capadepenapa + c
        
    elif c == 'o':
        c = 'opo'
        capadepenapa = capadepenapa + c
        
    elif c == 'u':
        c = 'upu'
        capadepenapa = capadepenapa + c
    
    else:
        capadepenapa = capadepenapa + c
        

print(capadepenapa)
