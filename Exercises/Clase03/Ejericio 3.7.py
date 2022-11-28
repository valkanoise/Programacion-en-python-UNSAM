data = [4, 9, 1, 25, 16, 100, 49]

print(min(data))

print(max(data))

print(sum(data))


#%% Probá iterar sobre los datos.

for x in data:
        print(x)

#%%
for n, x in enumerate(data):
        print(n, x)
  
#%% Si queremos imprimir al objeto enumerate() se puede hacer lista o dict
print(list(enumerate(data)))
[(0, 4), (1, 9), (2, 1), (3, 25), (4, 16), (5, 100), (6, 49)]


print(dict(enumerate(data)))
{0: 4, 1: 9, 2: 1, 3: 25, 4: 16, 5: 100, 6: 49}