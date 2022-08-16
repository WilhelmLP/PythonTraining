#Sets
#Son tipos de datos que admiten elementos únicos y sus elementos son inmutables
#No puede incluir listas ni diccionarios

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
print(len(mi_set))

#Se pueden hacer consultas dentro de un set
print(2 in mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#Union de sets con método union
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1 .union(s2)
print(s3)

#Médotos: add, remove, discard, pop, clear
s3.add(6)
print(s3)

s3.remove(1)
print(s3)

sorteo = s1.pop()
print(sorteo)

s1.clear() #Deja vacio el set
print(s1)