import os
import shutil
import send2trash

"""shutil.move('curso.txt', 'C:\\Users\\willy\\OneDrive\\Documentos\\04-Udemy\\Federico Garay\\PythonTotal')
print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('Texto de Prueba')
archivo.close()

print(os.listdir())"""

#un and mv
#shutil.rmtree -> elimina todo dentro de una carpeta permanentemente

#send2trash.send2trash('curso.txt')

#print(os.walk('C:\\Users\\willy\\OneDrive\\Documentos\\04-Udemy\\Federico Garay\\PythonTotal'))

ruta = 'C:\\Users\\willy\\OneDrive\\Documentos\\04-Udemy\\Federico Garay\\PythonTotal'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {ruta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        if arch.startswith('2015'):
            print(f'\t{arch}')
    print('\n')