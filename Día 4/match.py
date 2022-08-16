"""
Match es una nueva forma de tratar las condiciones del flujo de nuestro programa.
Antes de Python 3.10 no existia, pero actualemente es como un switch en otros lenguajes, ya que busca por coincidencias
en cada caso para poder ejecutar unas instrucciones

match variable:
    case "coincidencia":
        instrucciones
    case "coincidencia":
        instrucciones

No obstante el match se diferencia del if, elif y else en que busca coincidencias en patrones de listas, variables o dic.
"""
#Ejemplo 1
serie = 'N2'

match serie:
    case 'N1':
        print('MacBook')
    case 'N2':
        print('Razer')

#Ejemplo 2

cliente = {'nombre': 'Guillermo',
           'edad': 28,
           'ocupacion': 'Programador'}

videojuegos = {'titulo': 'Dark Souls',
               'ficha_tecnica': {
                   'consola': 'PlayStation',
                   'creador': 'Hydeitaka Miyasaki',
                   'anio': 2010
               }}

elementos = [cliente, videojuegos, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'consola': consola,
                                'creador': creador,
                                'anio': anio}}:
            print("Es un videjojuego")
            print(titulo, consola, creador)
        case _:
            print("No hay coincidencias")
