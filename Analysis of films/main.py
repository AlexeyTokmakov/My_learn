
from bs4 import BeautifulSoup
import requests
from lxml import html


USER_ID= 12345
URL = 'https://www.kinopoisk.ru/top/'

r=requests.get(URL)
with open('kinopoisk.html','w') as output_file:
    output_file.write(r.text)


html_doc=open('kinopoisk.html').read()

soup=BeautifulSoup(html_doc,'lxml')

for i in range(249):
    i+=1
    name="top250_place_" + str(i)
    print(name)
    film=soup.find('tr',{'id':name})
    name_film=film.find(class_='all').next_element
    print(name_film)



