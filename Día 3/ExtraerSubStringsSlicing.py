# Slicing o cadenas de substrings

texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)

fragmento = texto[2:5]
print(fragmento)

fragmento = texto[:5]
print(fragmento)

fragmento = texto[2: 10: 2] #punto de inicio, punto de llegada, distribución
print(fragmento)

fragmento = texto[::3]
print(fragmento)

fragmento = texto[::-1]
print(fragmento)