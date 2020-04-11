# Dump-all-pictures-from-https-prnt.sc
This script dumps all the pictures from https://prnt.sc.

# Dependencies
- Python 2.7
- Import time
- Import BeautifulSoup
- Import urllib, urllib2 

# Background
Users can upload pictures to https://prnt.sc that are made publicly availalbe. The way the access to each picture is structured is through 
a sequence consisting of two letters and a four digit number. In totalt making a code consisting of 6 characters. Letters range from aa - zz and numbers from 0000 - 9999.

An example of the url for one picture is: https://prnt.sc/aa0000

# What the script does and how it works
- The script generates the code for each possible picture
- It navigates to that URL (e.g. https://prnt.sc/aa0000)
- Fetches the underlying URL for the image from the HTML source
- Downloads the image in the same folder as the script resides and names it with its corresponding code.


