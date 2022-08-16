'''
El manejo de errores se puede hacer que el código siga ejecutando el codigo sin detenerse. Las palabras clave son:

try:
    #Codigo que se quiere probar
except:
    #Codigo a ejecutar si no hay un error
finally:
    #Codigo que se va a ejectuar de todos modos

--> Puede llevar un else despues del expect
else:
    #Codigo a ejecutar si no hay un error

'''

def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    print("Se hizo correctamente")
finally:
    print("Eso fue todo")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print("Gracias")

pedir_numero()

#Ejercicio 1
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")
    else:
        pass
    finally:
        pass

#Ejercicio 2
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la
        función habitualmente}
        except:
        {Excepción}
    else:
    ...
    etc.
"""

def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        pass
    finally:
        pass

#Ejericio 3
"""
Ejemplo de resolución:
def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")


#MENSAJES EN PANTALLA:
"El archivo no fue encontrado"
"Error desconocido"
"Abriendo exitosamente"
"Finalizando ejecución"

