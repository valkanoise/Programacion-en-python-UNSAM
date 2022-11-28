import numpy as np

a = np.arange(1,20,2)


b = np.linspace(1,19, 10)

print(type(a[0]))
print(type(b[0]))

a = 

'''ambos vectores son iguales, pero arange genera datos del type int32
y linspace del tipo float64. 
Float64 (64bits = 8 bytes) ocupa del doble de memoria que int 32 (32 bits = 4 bytes)'''