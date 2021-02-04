import requests
#print ('hihihihihihihi')

#URL hard-coded
URL = 'https://en.wikipedia.org/wiki/Earth'

#get request
response = requests.get(URL)

#check to see if response returned successful
if (response.status_code == 200):
    print ('get request successful')
elif (response.status_code == 204):
    print('no content found')
else:
    print ('not found')

#response.content returns the raw bytes
response.encoding = 'utf-8'
print (response.text)
