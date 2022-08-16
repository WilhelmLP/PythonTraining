from random import *

nombre = input("introduce tu nombre: ")
numero = randint(1, 101)
print("pense un numero entre el 1 y el 100, adivina cual es, tienes 8 intentos")

oportunidades = 1
while oportunidades < 9:
    print(f"oportunidad: {oportunidades}")
    intento = int(input("Introduce un numero: "))
    if intento not in range(1, 101):
        print("Numero no permitido")
    elif intento < numero:
        print("tu numero es mas pequeno del que pense, intenta de nuevo")
    elif intento > numero:
        print("Tu numero es mayor al que pense, intenta de nuevo")
    else:
        print(f"haz Ganado, felicidades {nombre}")
        juego = input("Juegas de nuevo: (s/n): ")
        match juego:
            case "s":
                print(f"Comienza el juego")
                numero = randint(1, 101)
                oportunidades = 0
                continue
            case "n":
                print(f"Nos vemos luego {nombre}")
                break
    oportunidades += 1
    if oportunidades == 9:
        print(f"has  perdido {nombre}")
        juego = input("Juegas de nuevo: (s/n): ")
        match juego:
            case "s":
                print(f"Comienza el juego")
                numero = randint(1, 101)
                oportunidades = 0
                continue
            case "n":
                print(f"Nos vemos luego {nombre}")
                break
else:
    print(f"Fin del juego, el numero era: {numero} suerte para la proxima {nombre}")