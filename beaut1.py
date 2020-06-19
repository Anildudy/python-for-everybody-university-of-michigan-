import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url:")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
a=0
b=0
while b<6:
    a=0
    for tag in tags:
        a += 1
        url= tag.get('href',None)
        name = tag.contents[0]
        if a==18:
            break
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    b += 1
c=0
for tag in tags:
    c += 1
    str = tag.contents[0]
    if c==18:
        break
print(str)
