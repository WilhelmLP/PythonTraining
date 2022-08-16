mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

resultado = len(mi_lista)
print(resultado)

resultado = mi_lista[0:1]
print(resultado)

mi_lista2 = ['d', 'e', 'f']
print(mi_lista + mi_lista2)
print(mi_lista)
print(mi_lista2)

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista3[0] = "Alfa"
mi_lista3.append('g') #Agrega elemento a la lista
print(mi_lista3)

eliminado = mi_lista3.pop(0) #Elimina el ultimo elemento de la lista si no se especifica por el indice
print(eliminado)
print(mi_lista3)

#Ordenar las listas con .sort()
lista = ['g', 'o', 'b', 'n', 'c']
lista.sort()
lista2 = lista
print(lista2) #Así guarda el ordenamiento y no queda el objeto NoneType

lista.reverse()
print(lista)
