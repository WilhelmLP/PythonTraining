lista = [1, 2, 3, 4]

for numero in lista:
    print(numero)

print("Utilizando el range(5)")
for numero in range(5):
    print(numero)

for numero in range(10, 51, 2):
    print(numero)

lista = list(range(1, 11))
print(lista)

#Ejercicio 3
suma_cuadrados = 0

for i in range(1, 16):
    suma_cuadrados += i ** 2

