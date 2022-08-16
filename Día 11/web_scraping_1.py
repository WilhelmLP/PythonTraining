import bs4
import requests

#Extraer el titulo de la pagina
resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('title'))

#Extraer un parrafo
parrafo_especial = soup.select('p')[3].getText()
print(parrafo_especial)

#Extraer una clase completa
columna_lateral = soup.select('.post-header')

for p in columna_lateral:
    print(p.getText())




