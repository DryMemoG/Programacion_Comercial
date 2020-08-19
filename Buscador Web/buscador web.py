import re
import urllib3
import pymongo
import pprint

lista = ['http://www.stackoverflow.com']
titulos = []

client = pymongo.MongoClient("mongodb+srv://drymemog:admin@cluster0.iyble.mongodb.net/<dbname>?retryWrites=true&w=majority")

c = 0
#se conecta a la base de datos dbProfesor, sino existe la crea
db = client.dbURLs
link = db.enlace
def metas(html, regex):
    cont = ''
    for x in verificar(html,regex):
        cont = x
    return cont

def insertarURL(json):
    message="Insertado exitosamente"
    try:
        link.insert_one(json)
    except:
        message= "Error!"
    return message

def leer(url):
    html = ''
    try:
        http=urllib3.PoolManager()
        resp = http.request('GET',url)
        html= resp.data.decode('utf-8')
    except:
        pass
    return html

def verificar(url, regex):
    patron = re.compile(regex)
    return patron.findall(html)

while True:
    html = leer(lista[c])
    titulo = verificar(html,'(?<=<title>).+(?=<\\/title>)')
    if len(titulo)>0:
        if titulo[0] not in titulos:
            titulos.append(titulo[0])
            descripcion = metas(html,'(?<=meta\\sname=["|\']description["|\']\\scontent=["|\'])[^"|\']*')
            keywords = metas(html,'(?<=meta\\sname=["|\']keywords["|\']\\scontent=["|\'])[^"|\']*').split()
            autor = metas(html, '(?<=meta\\sname=["|\']author["|\']\\scontent=["|\'])[^"|\']*')
            enlaces = verificar(html,'(?<=href="|href=\')http[^"|\']*')
            for enlace in enlaces:
                if enlace not in lista:
                    lista.append(str(enlace))
            data={
                "title": titulo[0],
                "author": autor,
                "description": descripcion,
                "url": lista[c],
                "keywords": keywords
            }
            message = insertarURL(data)
            print(data, message)
    c = c+1
    if c == len(lista):
        break
