
texto = "Este es un texto de Guillermo"
resultado = texto[2].upper()
resultado = texto.lower()
print(resultado)

#Uso del método de split / devuelve una lista
resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)

#Uso del método de join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))

#Uso del método find
resultado = texto.find("W")
print(resultado)

#Uso del método replace
resultado = texto.replace("Guillermo", "Willy")
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))


