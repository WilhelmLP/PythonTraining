"""
Una funcion generadora que ejecuta una función que generan y cuidan el espacio en el ordenador. 
La principal diferencia con una función generadora es que esta utiliza la palara yield en lugar de return
"""


def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))


def crear_lista2():
    lista = []
    for n in range(1, 6):
        lista.append(n * 10)

    return lista


def generador_lista():
    for x in range(1, 6):
        yield x * 10


print(crear_lista2())
print(generador_lista())

g2 = generador_lista()
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))


def mi_generador2():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x


g3 = mi_generador2()

print(next(g3))
print(next(g3))
print(next(g3))


# Ejercicio 1
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num


generador = secuencia_infinita()


# Ejercicio 2
def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1


generador = multiplos_siete()


# Ejercicio 3
def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()
