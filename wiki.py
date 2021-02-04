import requests
from bs4 import BeautifulSoup

#URL hard-coded
URL = 'https://en.wikipedia.org/wiki/Earth'

#get request
response = requests.get(URL)
response.encoding = 'utf-8'

#check to see if response returned successful
if (response.status_code == 200):
    print ('get request successful')
    soup = BeautifulSoup(response.content, 'html.parser')
    #bodyContent = soup.find(id='mw-content-text')
    bodyContent = soup.find_all('div', class_='mw-parser-output')
    #print (bodyContent.prettify())
    for element in bodyContent:
        pars = element.find_all('p')
        for p in pars:
            print(p)
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')

#response.content returns the raw bytes
#print (response.content)

#response.text just returns the text

#print (response.text)

#response.json() returns a dictionary -> can obtain values of objects by key
