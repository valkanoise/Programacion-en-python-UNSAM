def cant_digitos(n):
    
    # caso base
    if n < 10:
        cifras = 1
        return cifras
        
    else:
        cifras = cant_digitos(n / 10)
        cifras += 1
        return cifras