def buscar_precio(fruta):
    with open('Data/precios.csv') as f:
        archivo = f.read() #abro todo el archivo y lo leo como string
        if fruta in archivo: #busco si dentro del archivo como string está la fruta
            archivo = archivo.split('\n') #si la fruta está lo separo por lineas '\n' y se crea una lista se lineas
            for fila in archivo: # itero entre los elementos de la lista = filas
                fila = fila.split(',') # fruta y precio están separadas por ','
                if fila[0] == fruta: # busco la fruta de interés en la posición 0 y si está imprimo el precio
                    print (f'El precio de un cajón de {fruta} es: {fila[1]}')
        else: # si la fruta de interés no está en el string de todas las frutas y sus precios imprime que la fruta no está
            print(f'{fruta} no figura en el listado de precios.')
            
            
buscar_precio('Frambuesa')