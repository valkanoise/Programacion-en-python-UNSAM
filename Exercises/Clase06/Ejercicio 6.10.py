
import rebotes
import hipoteca
import informe_funciones
import fileparse
help(fileparse)
dir(fileparse)

camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)


from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
