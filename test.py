import requests
from bs4 import BeautifulSoup

#URL hard-coded
URL = 'https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-addresses'

#get request
response = requests.get(URL)
response.encoding = 'utf-8'

#check to see if response returned successful
if (response.status_code == 200):
    print ('get request successful')
    soup = BeautifulSoup(response.content, 'html.parser')
    #bodyContent = soup.find(id='mw-content-text')
    bodyContent = soup.find_all('span', class_='article') #find_all returns an iterable; find just returns a single element
    #print (bodyContent.prettify())
    with open('data.txt','w') as f:
        for element in bodyContent:
            pars = element.find_all('a')
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

#response.content returns the raw bytes
#print (response.content)

#response.text just returns the text

#print (response.text)

#response.json() returns a dictionary -> can obtain values of objects by key
