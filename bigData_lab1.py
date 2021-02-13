import requests
from bs4 import BeautifulSoup
import mysql.connector 
from mysql.connector import (connection)

import requests 
from functools import partial

URL = 'https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-addresses'
pref = 'https://www.infoplease.com'
properLink = 'primary-sources/government/presidential-speeches/state-union-addresses'

#attempt connection to mysql database 'DataExtraction' - local dB
try:
  cnx = mysql.connector.connect(user='testUser',
                                database='DataExtraction')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

#get request
response = requests.get(URL)
response.encoding = 'utf-8'

#check to see if response returned successful
if (response.status_code == 200):
    print ('get request successful')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    bodyContent = soup.find_all('span', class_='article') #find_all returns an iterable; find just returns a single element

    for elements in bodyContent:
      links = elements.find_all('a') #find each link in the content extracted
      for link in links:
        print(link.get('href'))


      # if links == "":
      #   print('No link found')
      # elif properLink not in links:
      #   print('This? : ' + links)

      # print (pref + links)
      
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')