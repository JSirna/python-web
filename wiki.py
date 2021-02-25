import requests
from bs4 import BeautifulSoup

#URL hard-coded
URL = 'https://en.wikipedia.org/wiki/Cyrillic_script'

#get request
response = requests.get(URL)
response.encoding = 'utf-8'

#check to see if response returned successful
if (response.status_code == 200):
    print ('get request successful')
    soup = BeautifulSoup(response.content, 'lxml')
    
    bodyContent = soup.find_all('div', class_='mw-parser-output') 
    #find_all returns an iterable; find just returns a single element
    tags = soup.find_all(True)
    with open('output.txt','a',encoding='utf-8') as f:
        for element in bodyContent:
            pars = element.find_all(['p','h1','h2','h3','ul'])
            if None in pars:
                continue
            for p in pars:
                print (p.text)
                data = p.text + '\n'
                f.write(data)

    f.close()
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')
