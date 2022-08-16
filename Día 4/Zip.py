"""
La función ZIP parece una función no muy utlizada pero sirve para convionar 2 o más listas entrelzando sus elementos en
tuples.
Suponiendo que ese tienen 2 listas, lo que se obtiene al aplicar ZIP es obtener una lista de tuplas

nombres = ['Guillermo', 'Danae',  'Doramu']
edades = [28, 27, 4]

combinado = list(zip(nombres, edades))
>> [('Guillermo', 28), ('Danae', 27) , ('Doramu', 4)]
"""

nombres = ['Guillermo', 'Danae',  'Doramu']
edades = [28, 27, 4]
ciudades = ['Canada', 'Estados Unidos', 'México',]

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")

#Ejercicio 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinado = list(zip(capitales, paises))

for capital, pais in combinado:
    print(f"La capital de {pais} es {capital}")

#Ejercicio 2
marcas = ['Vans', 'Samsumg', 'Razer']
productos = ['Tenis', 'Celulares', 'PC']

mi_zip = list(zip(marcas, productos))
print(type(mi_zip))

#Ejercicio 3

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))
