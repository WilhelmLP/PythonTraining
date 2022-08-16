from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/willy/OneDrive/Documentos/04-Udemy/Federico Garay/PythonTotal/CarpetaDesdePython/prueba.txt')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('El archivo sí existe, genial!')

ruta_Windows = PureWindowsPath(carpeta)
print(ruta_Windows)
