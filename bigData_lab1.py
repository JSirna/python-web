import requests
from bs4 import BeautifulSoup
import mysql.connector 
from mysql.connector import (connection)
from functools import partial
import csv
import os.path

URL = 'https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-addresses'
pref = 'https://www.infoplease.com'
properLink = '/primary-sources/government/presidential-speeches/state-union-addresses'

#check to see if response returned successful
def attemptRequest(url):
    #get request
    response = requests.get(url)
    response.encoding = 'utf-8'

    #check to see if response returned successful
    if (response.status_code == 200):
        print ('get request successful')
        # retrieve content
        soup = BeautifulSoup(response.content, 'lxml')
        linkList = []
        linkList = extractLinks(soup)
        extractData(linkList)
    elif (response.status_code == 204):
        print('no content found')
    else:
        print ('not found')

#extracts the list of links given from the website
def extractLinks(soup): 
  listStuff = []
  bodyContent = soup.find_all('span', class_='article')
  for elements in bodyContent:
      links = elements.find_all('a') #find each link in the content extracted
      for link in links:
          linkText = link.get('href')
          if linkText == "":
              print('No link found')
          else:
              listStuff.append(pref + linkText)

  return listStuff

#attempt second request to each URL in linkList
def extractData(links):
  count = 0
  fname = ''
  s_path = '/home/jsdev/Documents/Github/python-web/addresses/'
  dbl_array = [[]]
  for l in links:
    # Create a new URL and web request to access each link individually
    URL = l
    response = requests.get(URL)
    response.encoding = 'utf-8'
    if (response.status_code == 200):
      soup2 = BeautifulSoup(response.content, 'lxml')

      td = [] #list for all matching fields -> goes into csv file
      # find the content containing Name and Date fields
      content = soup2.div.find('article').find_all('div', class_='titlepage')
      
      for head in content:
        if head.text == '':
          head.find_all('h1', class_='page-title')
          td = head.text.split('(')
        else:
          td = head.text.split('(') # returns a list of name and date
        print(td[0])
        #print(td[1])
        td.append(l) # add in the URL
          
      # find the content containing the address text
      content = soup2.div.find('article').find_all('p')
      combinedPars = ''
      for addr in content:
        combinedPars += addr.text
      count += 1
      fname = 'InfoUnionAddress_' + str(count) + '.txt'
      completeName = os.path.join(s_path, fname)
      td.append(completeName) #add file path
      # create text files
      # with open(completeName,'w') as f:
      #   f.write(combinedPars)
      # f.close()

      # append address text to list
      #td.append(combinedPars)
      dbl_array.append(td)
      with open('data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Name', 'Date', 'Link to Address', 'Location to Text file/Filename','Address Text'])
        spamwriter.writerows(dbl_array)
      csvfile.close()

    elif (response.status_code == 204):
        print('no content found')
    else:
        print ('not found')

# MySQL connection and data creation in Table
def createTable():
  #attempt connection to mysql database 'DataExtraction' - local dB
  try:
    cnx = mysql.connector.connect(user='testUser',
                                  database='DataExtraction')
    # Check MySQL DB tables; if they don't exist then add them
    mycursor = cnx.cursor()

    # Create Table


    mycursor.execute("SHOW TABLES")
    for x in mycursor:
      print(x) 
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()

# Run
attemptRequest(URL)
