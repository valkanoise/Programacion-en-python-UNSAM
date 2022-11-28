def pascal(n,k) :
    
    # Creo una función auxiliar que calcula todos los valores de un nivel
    def aux(n):
        # Caso base
        if n == 0 :
            return [1]
        
        # Casos recursivos
                
        else :
            line = [1]
    
            # Recursive Case
            # Creo una lista con todas las filas k para determinada fila n 
            previousLine = aux(n - 1)
            for i in range(len(previousLine) - 1):
                line.append(previousLine[i] + previousLine[i + 1])
            line += [1]
        return line
    
    # A patir de la lista con todos los valores elijo la columna k de interés
    lista = aux(n)
    return lista[k]

#%% Prueba

if __name__ == '__main__':
    print(pascal(5, 2))