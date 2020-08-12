import re

cadena = "a3bcde1fa5"
patron = re.compile('a[3-5]+') 
print(patron.findall(cadena)) 

import urllib3

http = urllib3.PoolManager()
respuesta = http.request('GET', 'http://docs.python.org')
html = respuesta.data.decode('utf-8')
print (html)