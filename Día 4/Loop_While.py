"""
El Loop While

Este bucle no depende de las interaciones en una lista, tupla, diccionaro, etc. sino que se ejecuta mientras una determinada
condición se cumpla. Esto quiere decir que puede ser un bucle dónde si la condición se cumple siempre, siempre se estará
ejecutando el conjunto de instrucciones que estan dentro del While. Por eso hay que saber cuando hay que romper un bluce
para evitar un ciclo infinito.

while una_condicon:
    #un_codigo
else:
    #otro_codigo

Hay palabras clave para evitar que pasen los bluces infinitos tanto en los for como en los while y son:
break, continue, pass
"""
#Ejemplo 1
monedas = 5
while monedas > 0:
    print(f"Tengo {monedas}")
    monedas -= 1
else:
    print("No tengo más dinero")

#Ejemplo 2
respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

#Ejemplo 3
respusta = 's'
while respuesta == 's':
    pass
print("Hola se uso un PASS")

#Ejemplo 4
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

nombre2 = input("Tu nombre: ")
for letra in nombre2:
    if letra == 'r':
        continue
    print(letra)

#Ejercicio 1
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

#Ejercicio 2
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
        continue

#Ejercicio 3
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero > 0:
        print(numero)
    else:
        break
