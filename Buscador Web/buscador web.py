import re
import urllib3
urls=[]
urlt=[]
sitios=""

def visitador(url,b):
    http = urllib3.PoolManager()
    respuesta = http.request('GET', url)
    cadena = respuesta.data.decode('utf-8')
    patron = re.compile('href="http.{0,}')
    direcciones = patron.findall(cadena)
    if b == 1:
        b = 0
        for i in direcciones:
            link=i.split('"')
            urls.append(link[1])
    else:
        for i in direcciones:
            link=i.split('"')
            urlt.append(link[1])
            print(link[1])
b = 1       
visitador("http://www.python.org",b)
for i in urls:
    print("Sitios en: "+i )
    visitador(i,0)
    print("********************")

 

