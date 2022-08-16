palabra = "Python"
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#Otra forma:
palabra2 = "Python3.10"
lista2 = [letra2 for letra2 in palabra2]
print(lista2)

lista3 = [n / 2 for n in range(0, 21, 2) if n * 2 > 10]
print(lista3)

lista4 = [x if x % 2 == 0 else 'No es par' for x in range(0, 10)]
print(lista4)

#Ejercicio de Conversión
pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [v ** 2 for v in valores]

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [v for v in valores if v % 2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados_fahrenheit - 32) * (5 / 9) for grados_fahrenheit in temperatura_fahrenheit]
print(grados_celsius)