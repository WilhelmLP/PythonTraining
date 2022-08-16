'''
El módulo RE de expresiones regulares es aquel que nos permite hacer busquedas avanzadas en texto que respeten un
determinado formato especifo. Es decir, se construye un patrón determinado para encontrar coincidencias por medio
de una corroboración.
Hay caracteres especiales para usar las expresiones regulares

/d ->   dígito numerico           v\d\.\d\d
/w ->   caracter alfanumérico     \w\w\w-\w\w
/s ->   espacio en blanco         número\s\d\d
/D ->   NO númerico               \D\D\D\D\D
/W ->   NO es alfanumerico        \W\W\W\W\W
/S ->   NO espacio blanco         \S\S\S\S

Tambien hay caracteres cuantificadores
+ ->    1 o más veces             código_\d-\d+
{n} ->  Se repite n veces         \d-\d{4}
{n, m} -> Se repite n a m veces   \w{3,5}
{n,} -> desde n hacia arriba      -\d{4,}-
* ->    0 o más veces             \w\s*\w
? ->    1 o 0                     casas?
'''

import re

texto = "Si neceistas ayuda, llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

busqueda = re.findall(patron, texto)
print(len(busqueda)) #No imprime el largo del texto, sino la repetición de la palabra en la variable patron


for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


texto2 = "Llama al numero 561-068-0774 ya mismo"
patron2 = re.compile('(\d{3})-(\d\d\d)-(\d{4})')
resultado2 = re.search(patron2, texto2)
print(resultado2.group(2))

clave = input("Clave: ")
patron3 = r'\D{1}\w{7}'
chequear = re.search(patron3, clave)
print(chequear)

texto3 = "No atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes', texto3)
buscar = re.search(r'...demos....', texto3)
print(buscar.group())

#buscar = re.search(r'[^\D$]', texto) Escluir el patron
buscar = re.findall(r'[^\s]*', texto)
print(''.join(buscar))

#Ejercicio 1

def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


#Ejercicio 2

def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


#Ejercicio 3
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
