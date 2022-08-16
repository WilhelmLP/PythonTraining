'''
Otra cosa de la herencia es que las clases hijos pueden heredar del padre no solo sus métodos y propiedades,
sino que también una clase hijo puede tener métodos modificados y métodos nuevos que el padre no tiene
Aunado a lo anterior un hijo puede heredar de más de una clase padre

Hay un problema de superposicion de métodos y propiedades de herencia que se puede controlar
'''

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self,edad, color, altura_vuelo):
        super().__init__(edad, color) #Herencias desde el constructor
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')


piolin = Pajaro(3, 'Amarillo', 60)
piolin.hablar()
piolin.volar(100)

#Ejemplo 2
class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja ja")

    def hablar(self):
        print("¿Cómo estas?")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar() #Para hacer que se utilice un metodo de una clase en especifico se pone antes de la que viene por defecto
mi_nieto.reir()

print(Nieto.__mro__) #Establece el orden de herencia

#Ejercicio 1
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass

#Ejercicio 2
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass

#Ejercicio 3
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
