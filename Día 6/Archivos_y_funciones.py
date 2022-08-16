def abrir_leer(archivo):
    abrir = open(archivo)
    return abrir.read()

abrir_leer('Prueba.txt')

def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")

def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()