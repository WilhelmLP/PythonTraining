text = input("Ingrese su texto: ")
letras = []

text = text.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tarecera letra: ").lower())

print("\n")
print("Cantidad de letras: ")
cantidad_letas1 = text.count(letras[0])
cantidad_letas2 = text.count(letras[1])
cantidad_letas3 = text.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letas1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letas2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letas3} veces")

print("\n")
print("Cantidad de palabras: ")
palabras = text.split()
print(f"Hemos encontrado  {len(palabras)} palabras en tu texto")

print("\n")
print("Letras de inicio y de fin: ")
letra_inicio = text[0]
letra_final = text[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_final}")

print("\n")
print("Texto invertido: ")
palabras.reverse()
text_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés, va a decir: '{text_invertido}'")

print("\n")
print("Buscando la palabra 'Python")
buscar_python = 'Python' in text
dic = {True : "sí", False : "no"}
print(f"La palabra Python {dic[buscar_python]} se encuentra en el texto")
