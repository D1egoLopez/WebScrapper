from bs4 import BeautifulSoup
import requests
import csv

url_ML = 'https://listado.mercadolibre.com.ar/'
Busc_temp = input('Que ta buscando mi pana?: ')
filename = Busc_temp.replace(' ', '_')
Busqueda = url_ML + Busc_temp.replace(' ', '-')

print(Busqueda)
source = requests.get(Busqueda)

soup = BeautifulSoup(source.content, 'html.parser')

product_info_list = [

]

li_elements = soup.find_all('li', class_= 'ui-search-layout__item')

for li in li_elements:
    product_info = {}
    titulo = li.find('h2', class_='ui-search-item__title',)
    if titulo:
        product_info['titulo'] = titulo.text.strip()
    contenedor_precio = li.find('div', class_='ui-search-price__second-line')
    if contenedor_precio:
        precio = contenedor_precio.find('span', class_='andes-money-amount__fraction')
    if precio:
        product_info['precio'] = precio.text.strip()
    product_info_list.append(product_info)
    url = li.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')
    if url:
        product_info['url'] = url.get('href', '')



for product_info in product_info_list:
    print(product_info)

csv_file = filename + '.csv'
csv_headers = ['Title', 'Price', 'URL']


with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()
    for product_info in product_info_list:
        writer.writerow({'Title': product_info.get('titulo', ''), 'Price': product_info.get('precio', ''), 'URL' : product_info.get('url', '')})





#//li[@class="ui-search-layout__item"]
#//h2[@class="ui-search-item__title"]