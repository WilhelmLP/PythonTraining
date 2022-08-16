'''
Los atributos en las clases se pueden distinguir en dos tipos:
Los que pertenecen a la clase y los atributos de instancia, es decir, atributos que pueden ser
dinstintos en cada instancia de pajaro.
El color podría ser un atributo de instancia por ejemplo y se define en el método constructor
'''

class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('azul', 'Tucan')
print(f'Mi parajaro es un {mi_pajaro.especie} y su color es {mi_pajaro.color}')

print(Pajaro.alas)
print(mi_pajaro.alas)

#Ejercicio 1
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
casa_blanca = Casa('blanco', 4)

#Ejercicio 2
class Cubo:
    caras = 6
    def __init__(self,color):
        self.color = color
cubo_rojo = Cubo('rojo')

#Ejercicio 3
class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje("Humano", True, 17)