#Python 2.7
import time
from bs4 import BeautifulSoup as BSHTML
import urllib, urllib2 



# Creates the ID needed for fetching the page for each picture. Range from aa0000 - zz9999
# Will be used a as such: https://prnt.sc/aa0000
def createID():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for letter in letters:
		i = 0
		while i < len(letters):
			letter_comb = letter + letters[i]
			j = 0
			while j <= 9999:
				ID = letter_comb + str(j).zfill(4)
				j += 1		
				getSource(ID) 
			i += 1		

# Fetches the page for each ID
def getSource(ID):

	request_headers = {
	"Accept-Language": "en-US,en;q=0.5",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Referer": "http://thewebsite.com",
	"Connection": "keep-alive" 
	}

	request = urllib2.Request("https://prnt.sc/" + ID, headers = request_headers)

	try:
		resp = urllib2.urlopen(request)
		response = urllib2.urlopen(request).read()

	except urllib2.HTTPError as e:
		response = 'Error'
		pass	

	except urllib2.URLError as e:
		response = 'Error'
		pass

	getImage(response, ID)

# Gets the image from the page we fetched, names it with the same ID and saves in same folder as the script.
def getImage(response, ID):

	timeout = 0 #In case of the server refusing connection due to too many request. Increase the timeout. 
	htmlText = response

	if(htmlText != 'Error'):

		soup = BSHTML(htmlText, features="lxml")
		images = soup.findAll('img', {'id': 'screenshot-image'})

		for image in images:

			print('ID: '+ ID + ' source: ' + image['src']) #Show output with ID and image source.

			if('https' in image['src']):
				urllib.URLopener.version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
				urllib.urlretrieve(image['src'], ID +'.png')

			else:
				urllib.URLopener.version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
				urllib.urlretrieve('http:'+image['src'], ID +'.png')

		time.sleep(timeout) 

	else:
		time.sleep(timeout) 



def downloadImages():
	createID()


#Run the script
downloadImages()
