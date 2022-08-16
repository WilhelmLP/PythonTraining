def chequear_3_cifras(numero):
    return numero in range(100, 1000)

num1 = 20
num2 = 99
suma = num1 + num2
resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifras2(lista):

    lista_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_cifras.append(n)
        else:
            pass    #El return no puede ir en un else porque corta la ejecución
    return lista_cifras

lista = [-99, 2343,232,333,45]
ch = chequear_3_cifras2(lista)
print(ch)

#Ejercicio 1
lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

lista_num_positivos = todos_positivos(lista_numeros)
print(lista_num_positivos)

#Ejercicio 2

lista = [1, 50, 500, 5000, 750, 600]
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(1, 1000):
            suma += n
        else:
            pass
    return suma

suma_lista = suma_menores(lista)
print(suma_lista)

#Ejercicio 3

lista_numeros = [1,50,502,5000,755,600,33,61, 2]
def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad

regresa_cantidad_pares = cantidad_pares(lista_numeros)
print(regresa_cantidad_pares)

