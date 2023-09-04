import urllib
from bs4 import beautifulsoup4

#url = 'http://py4e-data.dr-chuck.net/known_by_Milosz.html'
url = raw_input('Enter URL:')
count = int(raw_input('Enter count:'))
position = int(raw_input('Enter position:'))-1
html = urllib.urlopen(url).read()

soup = beautifulsoup4(html,"html.parser")
href = soup('a)

for i in range(count):
    link = href[position].get('href', None)
    print href[position].contents[0]
    html = urllib.urlopen(link).read()
    soup = beautifulsoup4(html,"html.parser")
    href = soup('a')
