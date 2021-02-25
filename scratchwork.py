#use for the dirty links behind the scenes

import requests
from bs4 import BeautifulSoup

#URL hard-coded
URL = 'http://www.thecramped.com/what-we-use/'

#get request
response = requests.get(URL)
response.encoding = 'utf-8'

if (response.status_code == 200):
    print ('get request successful')
    soup = BeautifulSoup(response.content, 'lxml')
    with open('linkScraper.html','w') as f:
        for stuff in soup:
            print(stuff)
            f.write(str(stuff))
    f.close()
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')