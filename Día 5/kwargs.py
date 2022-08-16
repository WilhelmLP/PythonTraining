'''
Los kwargs son argumentos que hacen referencia a tipos diccionarios
'''

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x = 3, y = 5, z = 2))

def suma2(num1, num2, *args, **kwargs):
    print(f'El primer valor es: {num1}')
    print(f'El segundo valor es: {num2}')

    for arg in args:
        print(f'Arg es igual a {arg}')

    for clave, valor  in kwargs.items():
        print(f'{clave} : {valor}')

args = [124,123,123,2134]
kwargs = {'x': 'uno', 'y' : 'dos', 'z' : 'tres'}

suma2(1011,12, *args, **kwargs)

#Ejercico 1:
def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

x = cantidad_atributos(a = 1, b = 2, c = 3)
print(x)

#Ejercicio 2
def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(clave)
        lista.append(valor)
    return lista

def_lista_atributos = lista_atributos(c = 12, d = 22, e = 15)
print(def_lista_atributos)

#Ejercicio 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')