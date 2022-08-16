
nombre = input("¿Cual es tu nombre?")
ventas = input("Diga la cantidad de su ventas totales al mes: ")

ventas = int(ventas)

comision = ventas * 13 / 100
comision = round(comision, 2)

print(f"Hola {nombre} tus comisiones de este mes son de ${comision}")