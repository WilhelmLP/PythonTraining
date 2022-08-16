'''
Los principios básicos de la POO son
Herencia, Polimorfismo, Cohesion, Abstracción, Acoplamiento, Encapsulamiento

La Herencia es un proceso mediante el cual se crea una clase (llamada hija) desde otra clase (llamada padre) y se
heredan atributos y métodos del hijo al padre. Lo anterior porque se sigue el DRY (Dont Repeat Yourself)

Ejemplo:

class Animal:
    def nacer(self):
    def morir(self):
    def respirar(self):

class Pajaro(Animal):
    [... código]
'''

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

print(Pajaro.__bases__) #Me devuelve de dónde hereda
print(Animal.__subclasses__()) #Devuelve todas las herencias de la clase

piolin = Pajaro(2, 'Azul')
piolin.nacer()
print(piolin.color)

#Ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

#Ejercicio 2
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

#Ejercicio 3
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass