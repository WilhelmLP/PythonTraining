'''
En las funciones existe el return que es un tipo de valor que se puede almacenar en una variable en cuyo caso es lo que
devuelve la ejecución de nuestra función.
Puede que una función devuelva ciertos procesos por los que paso un flujo de información y eso haya que almacenarlo en
una variable para pasar a otras funciones.
'''

def sumar(num1, num2):
    return num1 + num2

x = sumar(10, 10)
print(x)

def multiplicar(num1, num2):
    return num1 * num2

y = multiplicar(5, 10)
print(y)

print(multiplicar(2, 10)) #Impresión directa del resultado de una función por parametros

#Trabajando con las variables cuyos valores se asignaron a traves de parametros en una función
z = x + y
print(z)


def dividir(num1, num2):
    division = num1 / num2
    return division

r = dividir(x, y)
print(r)

def potencia(num1, num2):
    operacion = num1 ** num2
    return operacion

p = potencia(x, y)
print(p)

#Ejercicio de Conversor de monedas
def usd_a_eur(dolares):
    euros = dolares * 0.90
    return euros

dolares = 1
d = usd_a_eur(dolares)
print(d)

def eur_a_usd(euros):
    dolares = euros * 0.85
    return dolares

euros = 1
e = eur_a_usd(euros)
print(e)


def invertir_palabra(palabra):
    operacion = palabra[::-1].upper()
    return operacion

palabra = "Python"
invertido = invertir_palabra(palabra)
print(invertido)