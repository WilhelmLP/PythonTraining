'''
Hay decoradores en python son funciones que modifican el comportamiento de otras funciones
'''


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mi_funcion = mayuscula
mi_funcion('Python')


def una_funcion(funcion):
    return funcion


una_funcion(mayuscula("Probando"))


def cambiar_letras(tipo):
    def mayuscula2(texto):
        print(texto.upper())

    def minuscula2(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula2
    elif tipo == "min":
        return minuscula2


operacion = cambiar_letras('may')
operacion('palabra')

def decorar_saludo(funcion2):

    def otra_funcion(palabra):
        print('Hola soy la funcion que decora')
        funcion2(palabra)
        print('adios de la función que decora')
    return otra_funcion

@decorar_saludo
def mayusculas3(texto):
    print(texto.upper())

def minuscula3(texto):
    print(texto.lower())

mayusculas3("Esta texto funciona con decorador")

mayuscula_decorada = decorar_saludo(mayusculas3)
mayuscula_decorada('Guillermo')