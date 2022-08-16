mi_archivo = open('Prueba.txt')

#print(mi_archivo.read())

#for l in mi_archivo:
    #print("Aqui dice: " + l)

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())

una_linea = mi_archivo.readline()
print(una_linea.find('tercera'))

#todas = mi_archivo.readlines()
#todas = todas.pop()

mi_archivo.close()

#Ejercicio 1
archivo = open("Prueba.txt")
lineas = archivo.readlines()
print(lineas[1])

# Alternativa de solución admitida:
# lineas = archivo.readline()
# lineas = archivo.readline()
# print(lineas)
