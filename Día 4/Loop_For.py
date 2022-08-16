"""
Loop For:

For en Python es un blucle que se busca utilizar en casos de hacer iteraciones
Hay más de un uso de For dónde se puede iniciarlizar la variable, establecer las condiciones internas como en otros
leguanjes, pero en Python es para iteraciónes, para loops que son indeterminados y condicionales, está while

"""

#Ejemplo 1
lista = ['a', 'b', 'c']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"La letra es: {letra} y está en el indice {numero_letra}")
    print(f"{numero_letra} : {letra}")

#Ejemplo 2
lista2 = ['Danae', 'Guillermo', 'Doramu', 'Erika', 'Raul', 'Pili', 'Lalo', 'Alejandra', 'Elena', 'Karla']
letras = input("Introduce una letra: ").upper()
for nombre in lista2:
    if nombre.startswith(letras):
        print(f"\t{nombre} sí empieza con {letras}")
    else:
        print(f"\t{nombre} no empieza con {letras}")

#Ejemplo 3
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print(mi_valor, "al final de la iteración")

#Ejemplo 4
palabra = 'Python'
for letra in palabra:
    print(letra)

#Ejemplo 5
for num1, num2, num3 in [[1,2,3], [4,5,6], [7,8,9]]:
    print(num1, num2, num3)

#Ejemplo 6
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

print("Imprimiendo por ITEMS")
for item in dic.items():
    print(item)

print("Imprimiendo por VALOR")
for item in dic.values():
    print(item)

#Ejercicio 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero
print(suma_numeros)

#Ejercicio 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero%2 == 0:
        suma_pares += numero
    elif numero%2 == 1:
        suma_impares += numero

print(suma_pares)
print(suma_impares)
