import zipfile
import shutil

"""mi_zip = zipfile.ZipFile("archivo_comprimido", "w")

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()"""

"""zip_abierto = zipfile.ZipFile('archivo_comprimido', 'r')
zip_abierto.extractall()
A diferencia de extactall( ), extract( ) extrae un único archivo (o miembro) del archivo zip, 
por lo que requiere indicarle cuál de ellos será extraído
"""

"""
Shutil puede crear archivos comprimidos de diferentes formatos: “zip”, “tar”, “gztar”, “bztar”, “xztar”, entre otros. 
Por este motivo, cobra importancia indicarle el formato de archivo con el que se va a trabajar.
"""