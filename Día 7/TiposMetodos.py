'''
Decoradores
-> Metodos de instancia
    // Accede y modifica atributos del objeto, acceder a otros métodos y modificar el estado de la clase
-> Metodos de clase : @classmethod
    // No necesitan una instancia para poder ejecutarse
-> Metodo estático : @staticmethod
    // Los metodos estaticos no pueden acceder a los atributos de la clase ni a los atributos de las instancias, es decir
    son metodos que son inmutables dentro de la clase, es decir, son cosas que no se quiere que se modifique.
'''

class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'Pío, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'Negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(3)
piolin = Pajaro('Amarillo', 'Canario')
piolin.pintar_negro()
piolin.volar(50)

piolin.alas = False
print(piolin.alas)
Pajaro.mirar()

#Ejercicio 1
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

#Ejercicio 2
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

#Ejercicio 3
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1