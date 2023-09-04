# import libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 

# Prompt for URL
url = input('Enter url:')
print('Retrieving', url)

total = 0
count = 0

# Retrieve XML data
uh = urllib.request.urlopen(url)
data=uh.read()
print('Retrieved', len(data), 'characters')

# Parse XML data
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')



if __name__== '__main__':
    for item in lst:
        count = count + 1
        t = item.find('count').text
        total = total + float(t)


    print('Count:', count)
    print('Sum:', total)    




