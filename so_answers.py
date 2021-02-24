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
    
    bodyContent = soup.find_all('div', class_='answer')
    #find_all returns an iterable; find just returns a single element
    #tags = soup.find_all(True)
    
    with open('so_output.txt','w',encoding='utf-8') as f:
        for tag in bodyContent:
            print(tag)
            f.write(str(tag))
    f.close()
    
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')