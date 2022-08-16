import bs4
import requests

#Crear url sin número de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

#Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

#Iterar la paginación
for pagina in range(1 ,51):

    #Crear soup en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_base.format(pagina))
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #Iterar en los libros
    for libro in libros:

        #Revisa si tienen 5 o 4 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            #Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

#Ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    with open('lista_libros.txt', 'a') as archivo:
        archivo.writelines('\n'.join(titulos_rating_alto))
        archivo.close()




