import os

#ruta = os.getcwd() #chdir(), #makedirs(), #rmdir()
ruta = os.chdir('C:\\Users\\willy\\OneDrive\\Documentos\\04-Udemy\\Federico Garay\\PythonTotal')

archivo = open('OtroArchivoPythonTotal.txt')
print(archivo.read())

#Crea carpetas
#otra_carpeta = os.makedirs('C:\\Users\\willy\\OneDrive\\Documentos\\04-Udemy\\Federico Garay\\PythonTotal\\CarpetaDesdePython')

elemento = os.path.basename(archivo)
print(elemento)

elemento = os.path.dirname(archivo)

'''
Usar otra forma de lectura
'''

otro_archivo = open('C:\\Users\\willy\\OneDrive\\Documentos\\04-Udemy\\Federico Garay\\PythonTotal\\CarpetaDesdePython\\OtroArchivoPythonTotal.txt')
print(otro_archivo.read())

'''
Hay un modulo que contempla otros SO llamado Path de la librería Pathlib, el cual es un objeto
'''
from pathlib import Path

carpeta = Path('/Users/willy/OneDrive/Documentos/04-Udemy/Federico Garay/PythonTotal/CarpetaDesdePython/OtroArchivoPythonTotal.txt')
archivo = carpeta / 'OtroArchivoPythonTotal.txt' #concatenación para crear rutas

mi_archivo = open(archivo)
print(mi_archivo.read())
