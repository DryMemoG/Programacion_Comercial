def primero_segundo(i,j):
    i = str(i)
    jdiv = str(j).split(" ",maxsplit=1)
    if i[0] == jdiv[1][0]:
        return True
    else: 
        return False
print(primero_segundo("Hola wenas", "Hola Adios xd"))

import re
import urllib3

http = urllib3.PoolManager()
respuesta = http.request('GET', 'http://python.org')
cadena = respuesta.data.decode('utf-8')

patron = re.compile('\d') 
cantdigitos= patron.findall(cadena)
patron2 = re.compile('\s\d{1,2}[^0-9]')
cantnum100 = patron2.findall(cadena)
patron3= re.compile('([A-Z]*[a-z]*)')
cantpalabras = patron3.findall(cadena)
print(len(cantdigitos))
print(len(cantnum100))
print(len(cantpalabras))



