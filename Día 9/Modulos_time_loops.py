import time
import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


"""inicio = time.time()
prueba_for(1500)
final = time.time()
print(inicio - final)

inicio = time.time()
print(prueba_while(1500))
final = time.time()
print(inicio - final)"""

declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion_timeit_for = timeit.timeit(declaracion, mi_setup, number=10000)
print(duracion_timeit_for)

declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion_timeit_while = timeit.timeit(declaracion2, mi_setup2, number=10000)
print(duracion_timeit_while)

"""
La función timeit  requiere que la declaración y el setup sean pasados como strings 
para evitar que sean ejecutados normalmente por el intérprete (lo que de otro modo arrojaría un error de sintaxis). 
Es decir, si no pasáramos estos argumentos a la función como strings, sino como código Python, entonces los mismos se 
ejecutarían normalmente devolviendo un resultado en lugar del bloque de código en sí que queremos evaluar. 
La función timeit luego se encarga de transformar estos objetos en código que Python puede reconocer y ejecutar 
la cantidad de repeticiones suficientes para alcanzar conclusiones con respecto al tiempo.
"""