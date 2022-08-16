archivo = open("Prueba1.txt", "w") #r, w, a
archivo.write('Soy el nuevo texto')
archivo.write('Hola')
archivo.write('Mundo')
archivo.write('''
Hola Mundo,
este archivo se edito desde Python''')

archivo.writelines(['Tamibién se puede', 'utilizar otro metodo', 'llamado', 'Writelines'])

lista = ['HOLA', 'MUNDO', 'DESDE', 'PYTHON']
for p in lista:
    archivo.writelines(p + '\n')

archivo = open("Prueba1.txt", "a")
archivo.writelines('Amo a Doramu')

archivo.close()

archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")

archivo = open("mi_archivo.txt", "r")
print(archivo.read())

archivo = open('mi_archivo.txt', 'a')
archivo.writelines("Nuevo inicio de sesión")
archivo.close()

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

archivo.close()

archivo = open('mi_archivo.txt', 'r')
print(archivo)

archivo.close()

print('Ejercicio 3')

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
for rg in registro_ultima_sesion:
    archivo.writelines(rg + '\t')
archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())

'''
Hay que tener cuidado de utilizar la r, w y a, ya que pueden hacer sobreescritura en textos y no poder devolver lo
que ya se encontraba en él. R es para lectura, w es para escritura o sobre escritirua y a es de añadir
'''