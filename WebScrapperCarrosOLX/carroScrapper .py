from bs4 import BeautifulSoup
import requests
from getpass import getpass 
from twilio.rest import Client
import time
import schedule
ssid = #ssid
token = #token
#olx
#data:
base_url = "https://www.olx.pt/carros-motos-e-barcos/carros/braga/"
querry_parameters = "?search%5Bfilter_float_price%3Ato%5D=1500&search%5Bfilter_float_year%3Ato%5D=2004&search%5Bfilter_float_year%3Afrom%5D=1998&search%5Bfilter_float_quilometros%3Ato%5D=200000&search%5Bdescription%5D=1"

URL = base_url + querry_parameters
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
#class = marginright5 link linkWithHash detailsLink
list_price = []
list_nome = []
list_link = []
z = 0
# nome do carro
def infos():
    results_nome = soup.find_all(class_='marginright5 link linkWithHash detailsLink')
    for f in results_nome:
        a_nome = str(f).split("strong>")
        b_nome = str(a_nome[1]).replace('<'," ") 
        c_nome = str(b_nome).replace("/", " ")
        list_nome.append(c_nome)
    

    results_link = soup.find_all(class_='marginright5 link linkWithHash detailsLink')
    for f in results_link:
        a_link = str(f).split(" ")
        b_link = a_link[6].split("href=")
        c_link = b_link[1].split(">")
        d_link = c_link[0]
        list_link.append(d_link)

    #preco
    result_price = soup.find_all(class_ = "wwnormal tright td-price")

    for i in result_price:
        a_price = str(i).split("strong>")
        b_price = str(a_price[1]).replace('<'," ") 
        c = str(b_price).replace("/", " ")
        list_price.append(c)

    print(list_link)
    print(list_nome)
    print(list_price)
    exit()
      
def messenger():
    infos()
    TWILIO_ACCOUNT_SID = #ssid
    AUTH_TOKEN =#token

    client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)
    z = 0
    while z <= len(list_link)-1:
        message = client.messages \
            .create(
                body=str(list_nome[z]) + "\n" + str(list_link[z]) + "\n" + str(list_price[z]) ,
                from_='#number',
                to='#number'
            )
        z = z+1
    z = 0
    list_link.clear()
    list_nome.clear()
    list_price.clear()
    print(message.sid)
    exit()


