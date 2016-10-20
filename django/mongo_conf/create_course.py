from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.book2study
cursos = db.cursos

last_id =  str(db.seqs.find_and_modify(
        query={ 'collection' : 'cursos_collection' },
        update={'$inc': {'id': 1}},
        fields={'id': 1, '_id': 0},
        new=True).get('id'))

print last_id

curso = {
        "_id": last_id,
		"name": "curso "+ last_id,
	}

cursos.insert_one(curso)
