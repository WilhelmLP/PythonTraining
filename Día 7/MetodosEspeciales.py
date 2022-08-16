'''
Los metodos especiales en Python son los que tienen __nombre__ guion bajo al princio y al final de sus nombres, como
__init__ o __mro__, __bases__, __subclasses__
'''

mi_lista = [1,1,1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass
mi_objeto = Objeto()
print(mi_objeto)

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print(f'Se ha eliminado {self.titulo} de {self.autor}')

mi_cd = CD('Metallica', 'Master of Puppets', 10)

print(str(mi_cd))
print(len(mi_cd))

del mi_cd

#Ejercicio 1
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'\"{self.titulo}\", de {self.autor}'

#Ejercicio 2
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

#Ejercicio 3
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")