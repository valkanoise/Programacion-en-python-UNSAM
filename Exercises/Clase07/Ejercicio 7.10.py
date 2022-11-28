# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:59:24 2021

@author: FEFe
"""

#%%
def valor_absoluto(n):
    '''
    Calcula el valor absoluto de n
    
    Pre: n es un numero real
    Pos: devuelve el valor absoluto(positivo) de n
    '''

    if n >= 0:
        return n
    else:
        return -n

#%%    
def suma_pares(l):
    '''
    Suma los numeros pares incluidos en la lista l.
    
    Pre: la lista l puede recibir cualquier numero
    Pos: devuelve la suma de los numero pares (si hay numeros pares negativos los resta)
    '''
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0
    
    return res

#%%
def veces(a, b):
    ''' 
    Suma b veces al número a
    
    Pre: a puede ser cualquier numero raciona y b debe ser entero y > 0
    Post: devuelve la suma de b veces de a
    '''
    
    
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#%%

def collatz(n):
    '''
    Calcula el numero de pasos hasta que n = 1 según la Conjetura de Collatz
    
    Pre: n debe ser un valor real > 0
    Pos: Devuelve el nro de pasos necesarios hasta que n=1
    
    '''
    res = 1
    
    
    while n!=1:
        # si n es par, 
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
        print(res, n)

    return res