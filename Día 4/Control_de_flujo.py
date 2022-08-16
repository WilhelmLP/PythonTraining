if 10 > 9 :
    print("Es correcto")

x = 5 == 2

if x:
    print("Es correcto")
else:
    print("Es incorrecto")

mascota = 'Perro'

if mascota == 'Gato':
    print("Esto es un Perro")
elif mascota == 'Perro':
    print("Tienes un Perro")
else:
    print("Esto no es un Perro")


print("Verificando edad y califación: \n")

edad = 16
calificacion = 9

if edad <= 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No has aprobado')
else:
    print("Eres mayor de edad")

num1 = 1 #input("Ingresa un número:")
num2 = 1 #input("Ingresa otro número:")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")


print("###Ejercicio de condución ###")
edad = 16
tiene_licencia = False

if edad > 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")


habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True  and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")





