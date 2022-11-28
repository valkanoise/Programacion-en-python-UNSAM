# Con esto en mente, ¿podrías explicar el siguiente comportamiento?

# bool("False")
# True

#porque a la función bool se le ingresó un STRING no vacio...



#Ejemplos de los resultados que se pueden obtener usando la función bool()

# Here are a few cases, in which Python’s bool() method returns false. 
# Except these all other values return True. 

# If a False value is passed.
# If None is passed.
# If an empty sequence is passed, such as (), [], ”, empty string, etc
# If Zero is passed in any numeric type, such as 0, 0.0 etc
# If an empty mapping is passed, such as {}.
# If Objects of Classes having __bool__() or __len()__ method, returning 0 or False
 
# Returns False as x is False
x = False
print(bool(x))
 
# Returns True as x is True
x = True
print(bool(x))
 
# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x==y))
 
# Returns False as x is None
x = None
print(bool(x))
 
# Returns False as x is an empty sequence
x = ()
print(bool(x))
 
# Returns False as x is an empty mapping
x = {}
print(bool(x))
 
# Returns False as x is 0
x = 0.0
print(bool(x))
 
# Returns True as x is a non empty string
x = 'GeeksforGeeks'
print(bool(x))

# Returns Fase as x is a  empty string
x = ''
print(bool(x))