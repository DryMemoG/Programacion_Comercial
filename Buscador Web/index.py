from flask import Flask, render_template, request, redirect, url_for
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://drymemog:admin@cluster0.iyble.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.dbURLs
for lista in db.enlace.find({ "keywords": { '$regex': "web" }}):
    print(lista)
@app.route("/")

def inicio():
    return render_template("index.html")

@app.route("/buscador", methods=["POST","GET"])
def fnbuscar():
    palabra=request.form['term']
    client = pymongo.MongoClient("mongodb+srv://drymemog:admin@cluster0.iyble.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client.dbURLs
    resultado=[]
    for lista in db.enlace.find({ "keywords": { '$regex': palabra }}):
        resultado.append(lista)
    for lista in db.enlace.find({ "title": { '$regex': palabra }}):
        resultado.append(lista)
    for lista in db.enlace.find({ "author": { '$regex': palabra }}):
        resultado.append(lista)
    for lista in db.enlace.find({ "description": { '$regex': palabra }}):
        resultado.append(lista)
    busqueda=[]
    for i in resultado:
        dic={"link":i['url'],'titulo':i['title'],'descrip':i['description']}
        busqueda.append(dic)
    return render_template("resultados.html",dato=busqueda)
    
if __name__ == "__main__":
    app.run()