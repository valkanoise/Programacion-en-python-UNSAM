# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:30:19 2021

@author: FEFe
"""

class TorreDeControl:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self, arribos=[], partidas=[]):
        '''Crea una cola vacia.'''
        self.arribos = arribos
        self.partidas = partidas

    def nuevo_arribo(self, vuelo):
        '''Encola el elemento x.'''
        self.arribos.append(vuelo)

    def nueva_partida(self, vuelo):
        
        self.partidas.append(vuelo)
        
    def asignar_pista(self):
        if len(self.arribos) == 0 and len(self.partidas) == 0:
            print('No hay vuelos en espera.')
        if len(self.arribos) > 0:
            vuelo_asignado = self.arribos.pop(0)
            print(f'El vuelo {vuelo_asignado} aterrizó con éxito.')
        elif len(self.partidas) > 0:
            vuelo_asignado = self.partidas.pop(0)
            print(f'El vuelo {vuelo_asignado} despegó con éxito.')


    def ver_estado(self):
        esperando_aterrizar = ", ".join(self.arribos)
        esperando_despegar = ", ".join(self.partidas)
        print(f'Vuelos esperando para aterrizar: {esperando_aterrizar}')
        print(f'Vuelos esperando para despegar: {esperando_despegar}')
        
#%% Prueba

if __name__ == '__main__':
    import torre_control
    torre = torre_control.TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    # Vuelos esperando para aterrizar: AR156, AR32
    # Vuelos esperando para despegar: KLM1267
    torre.asignar_pista()
    # El vuelo AR156 aterrizó con éxito.
    torre.asignar_pista()
    # El vuelo AR32 aterrizó con éxito.
    torre.asignar_pista()
    # El vuelo KLM1267 despegó con éxito.
    torre.asignar_pista()
    # No hay vuelos en espera.