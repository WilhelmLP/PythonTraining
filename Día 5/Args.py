'''
Las palabras *args y **kwargs son convenciones pero no son palabras reservadas del lenguaje. Se utilizan para
poder representar un argumento en una función que no se sabe su extensión o su valor, entre otras cosas.
'''

def suma(a,b):
    return a + b

print(suma(5, 6))

#Argumento con número indefinido
def multiplicacion(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(multiplicacion(234,2))

def suma_args(*args):
    return sum(args)

print(suma_args(1243,124,123,12344))

#Ejercicio 1
def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg**2
    return total

print(suma_cuadrados(1,2,3))

#Ejercicio 2
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    return suma

#Ejercicio 3
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'