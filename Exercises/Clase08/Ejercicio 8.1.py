


def vida_en_segundos(fecha_nac):
    from datetime import datetime
    '''
    le pasás tu fecha de nacimiento y te devuelve la cantidad de segundos que 
    viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento). 
    
    
    Pre: fecha_nac es un string en formato 'dd/mm/AAAA' 
    (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales)
    
    Post: Devuelve un objeto float con la cantidad de segundos totales vividos
    '''
    
    hoy = datetime.now()
    nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    total_vivido = hoy - nacimiento
    total_vivido_segundos = total_vivido.total_seconds()
    
    return total_vivido_segundos

#%%
if __name__ =='__main__':
    vivido = vida_en_segundos('27/12/1983')
    print(f'Has vivido un total de {vivido:.2f} segundos')