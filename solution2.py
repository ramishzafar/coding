import urllib.request
from bs4 import BeautifulSoup

#url = 'http://py4e-data.dr-chuck.net/known_by_Milosz.html'
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')

if __name__== '__main__':
    for i in range(count):
        link = href[position].get('href', None)
        print (href[position].contents[0])
        html = urllib.request.urlopen(link).read()
        soup = BeautifulSoup(html,"html.parser")
        href = soup('a')
