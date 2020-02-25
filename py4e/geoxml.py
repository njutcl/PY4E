import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:



    url = 'http://py4e-data.dr-chuck.net/comments_369367.xml'
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print(counts)
    count=0
    for i in counts:
        i.text=int(i.text)
        count+=i.text
    print(count)