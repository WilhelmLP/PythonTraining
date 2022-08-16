# Tuplas
#Ocupan menos espacio de memoria, no son mutables, y sirven para almacenar cosas inmutables

mi_tuple = (1,2,3,(10, 20),5)
print(type(mi_tuple))
print(mi_tuple)
print(mi_tuple[-2])

#Se puede hacer casting
mi_tuple = list(mi_tuple)
print(type(mi_tuple))

mi_tuple.append(888)
print(mi_tuple)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

#Se puede agregar un tuple a otras variables
t = (1,2,3,1)
x, y, z, w = t #Esto se puede hacer también con listas y diccionarios
print(x, y, z, w)

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla

print(len(t))
print(t.count(1))
print(t.index(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))