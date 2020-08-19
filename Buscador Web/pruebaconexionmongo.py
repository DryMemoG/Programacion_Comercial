import datetime
import pymongo
import pprint

#conexion a la base de datos en Atlas, consultar su cadena en el panel
client = pymongo.MongoClient("mongodb+srv://drymemog:admin@cluster0.iyble.mongodb.net/<dbname>?retryWrites=true&w=majority")

#se conecta a la base de datos dbProfesor, sino existe la crea
db = client.dbProfesor

#seleccion la coleccion dbProfesor, sino existe la crea
profesor = db.profesor

#crea un documento con los datos que se van a almacenar
profesorDocumento = {
    "nombreCompleto": {"nombre": "Guillermo", "apellido": 'Galindo'},
    "dpi": "12345678979465",
    "cursos": ["Programacion Comercial", "Programacioón de dispositivos móviles"]
}

#inserta el documento
profesor.insert_one(profesorDocumento)

#para mostrar los datos insertados, los buscamos por medio de find_one
#pprint es una libreria pretty print, para mostrar con un formato mas claro los
#datos obtenidos
pprint.pprint (profesor.find_one ({"nombreCompleto.apellido":"Galindo"}))