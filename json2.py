import urllib.request, urllib.parse, urllib.error
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

add = input('Enter address:')

parms = dict()
parms['address']=add
parms['key']=api_key
url = serviceurl + urllib.parse.urlencode(parms)

print("Retrieving",url)

html = urllib.request.urlopen(url).read().decode()
print("Retrieved",len(html),"characters")

try:
    js = json.loads(html)
except:
    js = None

placeId = js['results'][0]['place_id']
print("Place id:",placeId)
