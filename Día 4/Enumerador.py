"""
Enumerate
Nos facilita entrar a los indices de una colección
"""

lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

print("\n")

print("Utilizando enumerate()\n")
lista2 = ['a', 'b', 'c', 'd']
for indice, item in enumerate(lista2):
    print(indice, item)
print("\n")

print("Utiliznado el enumerate con el range\n")
for indice, item in enumerate(list(range(1,6))):
    print(indice, item)
print("\n")

#Se puede usar para crear Tuples con el enumerate()
mis_tuples = list(enumerate(lista))
print(mis_tuples)

#Ejercicio 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#Ejercico 2
texto = "Python"
lista_indices = list(enumerate(texto))
print(lista_indices)

#Ejercicio 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)