class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'Pío, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')

piolin = Pajaro('amarollo', 'canario')
print(piolin)
piolin.piar()
piolin.volar(50)

#Ejercicio 1
class Perro:
    def ladrar(self):
        print("Guau!")
doramu = Perro()
doramu.ladrar()

#Ejercicio 2
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
merlin = Mago()
merlin.lanzar_hechizo()

#Ejercicio 3
class Alarma:
    def postergar(self, cantidad_minutos):
        self.cantidad_minutos = cantidad_minutos
        print(f"La alarma ha sido pospuesta {self.cantidad_minutos} minutos")

alerta = Alarma()
alerta.postergar(5)