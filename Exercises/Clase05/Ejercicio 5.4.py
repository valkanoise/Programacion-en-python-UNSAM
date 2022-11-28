import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']


# Se arma el mazo de cartas con comprensión de listas
naipes = [(valor,palo) for valor in valores for palo in palos]

random.shuffle(naipes)
print(naipes[-3:])

# lista.pop() devuelve un elemento de la lista[-1] y lo saca de la lista original
n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')