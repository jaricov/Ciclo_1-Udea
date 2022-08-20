"""import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx2.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data=input('Enter url:')
url = urllib.request.urlopen(data, context=ctx).read()

info = json.loads(url)
comments = info['comments']

count=0
for item in comments:
    #print('Name', item['name'])
    #print('count', item['count'])
    count=count+item['count']
print(count)

import re
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)


import re
s = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
result = re.findall('(?<=[https]:[/][/])([A-Za-z0-9.]*)', s)
print(result)"""


import re

s = 'ABCAC'

print(re.match('A', s) == True)