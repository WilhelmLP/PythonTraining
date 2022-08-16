"""
Random es un método para poder crear números aleatorios de manera muy facil
randint() número entero aleatorio que viene desde random de python
uniform()
random()
choice()
shuffle()
"""

from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = round(uniform(1, 5), 2) #decimal
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['Azul', 'Rojo', 'Amarillo', 'Blanco', 'Negro']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5, 50, 5))
shuffle(numeros) #No se puede almacenar en una lista
print(numeros)