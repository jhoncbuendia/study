import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.book2study

db.seqs.insert({
    'collection' : 'cursos_collection',
    'id' : 0
})

db.cursos.create_index([('_id', pymongo.ASCENDING)], unique=True)
cursos = db.cursos
