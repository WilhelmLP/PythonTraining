mi_edad = 2022 - 1994
print(mi_edad)


mi_dinero = 8400.50
mi_renta = 3500
mi_colegiatura = 1765.50
mi_internet = 450
suma_gastos = mi_internet + mi_colegiatura + mi_renta
print("Mi total despues de pagar es:", mi_dinero - suma_gastos)


print("Tipos de datos númericos: ")
print(type(mi_edad))
print(type(mi_dinero))
print(type(suma_gastos))

edad = int(input("Dime tu edad:"))
print("Tu edad es", edad)

nueva_edad = 1 + edad
print("El proximo año tu edad será {}".format(nueva_edad))

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))