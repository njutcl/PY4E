import json
from urllib.request import urlopen

url=input('url-')
html=urlopen(url).read()

info = json.loads(html)
print('User count:', len(info))
count=0
for item in info['comments']:

  count+=item['count']
print(count)