#import libraries
import urllib.request, json

#prompt url
address = input('Enter location: ')
print('Retrieving', address)

#open url and read contents
with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

#print number of characters retrieved
print('Retrieved', len(str(raw)), 'characters')

#get comments
data = raw.get("comments")

num = total = 0

if __name__== '__main__':
    for i in range(len(data)):
        tmp = data[i]
        value = tmp.get("count")
        num = num + 1
        total = total + int(value)
    
    print ("count:", num)
    print("Sum:", total)
