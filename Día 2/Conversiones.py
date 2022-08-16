#Conversiones con Python

num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3)  #Elimina decimales, no hace redondeo
print(num4)
print(type(num4))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)
print(type(nueva_edad))