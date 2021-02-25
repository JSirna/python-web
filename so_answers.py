import requests
from bs4 import BeautifulSoup

#URL hard-coded
URL = 'https://stackoverflow.com/questions/3665115/how-to-create-a-file-in-memory-for-user-to-download-but-not-through-server'

#get request
response = requests.get(URL)
response.encoding = 'utf-8'

if (response.status_code == 200):
    print ('get request successful')
    soup = BeautifulSoup(response.content, 'lxml')
    
    bodyContent = soup.find('div', class_='answer')
    for c in bodyContent.descendants:
        print (c)
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')