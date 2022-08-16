from collections import Counter, defaultdict, namedtuple, deque

numeros = [8,8,6,7,6,5,5,4,4,4,0,9,1,2,3,1,2,4,5,6]
frase = 'al pan pan y al vino vino'

print(Counter('Mississipi'))
print(Counter(frase.split()))
print(Counter(numeros))

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,4])
print(serie)
print(serie.most_common()) #Devuelve una tuple
print(list(serie)) #Casting a una lista

mi_diccionario = {'uno': 'verde', 'dos': 'azul', 'tres': 'verde'}
print(mi_diccionario['tres'])

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos']) #Construye un nuevo valor con base a una busqueda que debio arrojar valor

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
novia = Persona('Danae', 150, 55)
print(novia.nombre)
print(novia[2])

#Ejemplo 1
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)

#Ejemplo 2
mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44

#Ejemplo 3

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])