from random import randint

intentos = 0
numero_secreto = randint(1, 101)
estimado = 0
nombre = input("Hola, ¿cuál es tu nombre?\n")

print(f"Bievenido {nombre}, estoy pensado un número entre 1 y 100\nTienes 8 intentos para empezar a adivinar")

while intentos < 8:
    estimado = int(input("¿Cuál crees que es el número? \n"))
    intentos += 1

    if estimado not in range(1, 101):
        print("Tu numero no está en el rango del 1 al 100")
    elif estimado < numero_secreto:
        print("Mi número es más alto")
    elif estimado > numero_secreto:
        print("Mi número es más bajo")
    elif estimado == numero_secreto:
        print(f"Felicitaciones {nombre}, has adivinado en: {intentos} intentos")
        break
    else:
        print("No es un número, intanta otra vez")

if estimado != numero_secreto:
    print(f" Lo siento, se han agotado los intentos. El número secreto era {numero_secreto}")

