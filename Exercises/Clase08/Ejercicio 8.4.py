''' Desarrollo de la función dias_habiles'''


from datetime import datetime, timedelta

inicio = '20/9/2020'
fin = '10/10/2020'
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

# Con las fechas ingresadas las convierto a objetos datetime
inicio = datetime.strptime(inicio, '%d/%m/%Y')
fin = datetime.strptime(fin, '%d/%m/%Y')

# Calculo la diferencia de dias con la resta y metodo days que devuelve un int
delta_dias = (fin - inicio).days


lista_dias = []

for i in range(delta_dias + 1):
    dia = inicio + timedelta(days = i) # a la fecha de inicio le sumo un delta en cada iteracion
    dia_string = dia.strftime('%d/%m/%Y') # a cada fecha le hago su stringformat
    
    # si dia_string no está en feriado y dia no es sab o dom --> se agrega a la lista         
    if dia_string not in feriados and dia.weekday() not in [5,6]:
        lista_dias.append(dia_string)
    
    print(dia)
    
#%% Función días_habiles

def dias_habiles(inicio, fin, feriados = []):
    '''
    Ingresando una fecha de inicio, fecha de fin y una lista de feriados,
    devuelve una lista conteniendo los días hábiles.
    
    Pre: las fechas ingresadas son strings
    Post: La lista contiene fechas en formato string
    '''
    
    from datetime import datetime, timedelta
    
    inicio = datetime.strptime(inicio, '%d/%m/%Y')
    fin = datetime.strptime(fin, '%d/%m/%Y')
    delta_dias = (fin - inicio).days
    
    
    lista_dias = []
    for i in range(delta_dias + 1):
        dia = inicio + timedelta(days = i) 
        dia_string = dia.strftime('%d/%m/%Y')
        
        
        if dia_string not in feriados and dia.weekday() not in [5,6]:
            lista_dias.append(dia_string)
        
    return lista_dias

#%% Prueba funcion días_habiles()
inicio = '20/9/2020'
fin = '31/12/2020'
feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

lista_sin_feriados = dias_habiles(inicio, fin)
lista_con_feriado = dias_habiles(inicio, fin, feriados)

