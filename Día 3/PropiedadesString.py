nombre = "Danae"
#nombre[0] = "d"
# print(nombre) 'str' object does not support item assignment
### Los strings son inmutables ###

n1 = "Dana"
n2 = "Doramu"
print(n1 + " " + n2)
print(n1 * 2)

poema = """Mil pequeños peces blancos
comosi hirviera
el color del agua"""
print(poema)

print("agua" in poema) #Regresa bool
print("hierva" not in poema)

print(len(poema))


