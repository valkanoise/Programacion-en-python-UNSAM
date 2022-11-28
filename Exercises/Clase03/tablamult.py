print('       0   1   2   3   4   5   6   7   8   9\n--------------------------------------------')

for i in range(0,10):
    num = str(i) +':'
    print(f'{num:<5}', end= '')
    for j in range(0,10):
        print(f'{i*j:>3}', end= ' ')
        # print('{:3}'.format(i*j), end=' ')
    # imprimo una linea despues de cada i
    print()