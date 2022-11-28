
def incrementar(s):
    ''' Función que toma una lista binaria s de cualquier longitud y
    devuelve su función incrementada.
    Por ej. si recibe [0,0] devuelve [0,1]
    '''

    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    
    return s

def listar_secuencias(n):
    ''' Función que crea una lista binaria de n cantidad de ceros. A partir
    de esta lista creará todas las listas binarias posibles para la longitud
    igual a n mediante el incremento paso a paso.
    Por ej. si recibe n=2 crea la lista = [[0,0],[0,1],[1,0],[1,1]]
    '''
    # creo una lista con n cantidad de 0's
    secuencia = [0]*n
    
    # creo una lista vacía donde almacenar la secuencias binarias
    lista = []
    
    for i in range(2**n):
        # almaceno la primer secuencia binaria
        lista.append(secuencia)
        # a cada secuencia le calculo su incremental
        secuencia = incrementar(secuencia[:]) # le pido que copie a la secuencia sino salen todas listas iguales con un solo "vector"

    
    return lista
        
if __name__ == '__main__':
    
    print(incrementar([0, 0, 0, 0, 0]))
    print(incrementar([0, 0, 0, 0, 1]))
    print(incrementar([0, 0, 0, 1, 0]))
    print(incrementar([1, 1, 1, 1, 1]))
    print(listar_secuencias(3))