import urllib.request, urllib.parse, urllib.error
import json

link = input("Enter url:")
print("Retrieving",link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

ct = 0
sum = 0
for item in js['comments']:
    ct += 1
    sum += int(item['count'])

print('Count:',ct)
print('Sum', sum)
