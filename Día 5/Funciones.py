'''
Las funciones sirven para ejectuar un conjunto de instricciones que pueden ser reutilizdas en diferentes partes del
código. La funciones también reciben parametros.

def mi_funcion (nombre):
    print(f"Hello {nombre}")

mi_funcion("Willy")
>> Hello  Willy
'''

def saludar_persona(nombre):
    '''
    Esta función sirve para saludar a las personas
    y este es un comentario de documentación
    :return: especifica que retorna la función
    '''

    print(f"Hola {nombre}")

#Está sería la llamada a la función
nom = input("Escribe tu nombre: ")
saludar_persona(nom)


def cuadrado(un_numero):
    print(un_numero ** 2)

un_numero = 10
cuadrado(un_numero)