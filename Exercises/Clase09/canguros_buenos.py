# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:29:02 2021

@author: FEFe
"""
#%% Mi clase Canguro
class Canguro(object):
    def __init__(self, nombre, contenido = []):
        self.nombre = nombre
        #### OJO ####
        # hay que copiar la lista sino la comparten todas las instancias de la clase Canguro
        self.contenido_marsupio = contenido.copy() 
    
    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
        
    def __str__(self):
        return f'{self.nombre} tiene en su marsupio: {self.contenido_marsupio}'


#%% Clase Canguros malos

class Canguro1:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        
        #### ERROR ACÁ ####
        ''' El error consistía en que los contenidos_marsupio eran los mismos
        en la madre canguro y en el hijo canguro, por ende compartían la lista,
        para solucionarlo copio la listas al crearla y son independientes los
        contenidos entre madre e hijo '''
        
        self.contenido_marsupio = contenido.copy()

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%% Pruebas
if __name__ == '__main__':
        
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    
    print(madre_canguro)
    print(cangurito)