'''
El polimorfismo es el segundo de los pilares de la POO. Viene de Poli que es muchos y morfos que es forma.
Esto aplicado a la programación hace referencia a que los objetos pueden adoptar multiples metodos o propiedades
que son identicas o similares en su declaración y de ahí que puedan aplicarse cosas como la iteración o un flujo
control
'''

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice mouu')

class Obeja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca1 = Vaca('Aurora')
objea1 = Obeja('Nube')

animales = [vaca1, objea1]
for animal in animales:
    print("*" * 10)
    animal.hablar() #Esto es el Polimorfismo en un Loop
    print("*" * 10 + '\n')

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(objea1)

#Ejercicio 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))

#Ejercicio 2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

Voldemort = Mago()
Legolas = Arquero()
Sekiro = Samurai()
personajes = [Legolas, Voldemort, Sekiro]

for personaje in personajes:
    personaje.atacar()

#Ejercico 3
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()