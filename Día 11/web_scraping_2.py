import bs4
import requests

pagina = requests.get('https://www.escueladirecta.com/courses')
formato = bs4.BeautifulSoup(pagina.text, 'lxml')

imagenes = formato.select('.course-box-image')[0]['src']
print(imagenes)

#Guardar imagen
imagene_curso_1 = requests.get(imagenes)
archivo = open('mi_imagen.jpg', 'wb')
archivo.write(imagene_curso_1.content)
archivo.close()


"""print(imagene_curso_1.content)"""

"""for i in imagenes:
    print(i)"""