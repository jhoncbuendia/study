import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.book2study

db.seqs.insert({
    'collection' : 'admin_collection',
    'id' : 0
})


last_id =  str(db.seqs.find_and_modify(
        query={ 'collection' : 'admin_collection' },
        update={'$inc': {'id': 1}},
        fields={'id': 1, '_id': 0},
        new=True).get('id'))


db.cursos.create_index([('_id', pymongo.ASCENDING)], unique=True)
cursos = db.cursos




curso = {
        "_id": last_id,
		"img_url": "https://static.student-cdn.com/media/cache/city_preview_desktop/mstr/country/united-states/city/philadelphia/heroImage/image-nv6bdu.jpeg",
		"nombre": "curso 8",
		"puede_trabajar": "no",
		"costo_seguro_medico": "100 ",
		"actividades": [
			"actividad 1"
		],
		"categoria": 1,
		"nivel": "principiante",
		"plan": [
			{
				"id": 1,
				"nombre": "plan 1",
				"precio": 100,
				"descuento": 0,
				"fecha_creacion": "2016-07-17T00:53:35.889146Z",
				"resume_es": "resume es 1",
				"resume_ing": "resume ing 2"
			},
			{
				"id": 2,
				"nombre": "plan 2",
				"precio": 23,
				"descuento": 12,
				"fecha_creacion": "2016-07-17T18:15:30.667030Z",
				"resume_es": "resume es 2",
				"resume_ing": "resume ing 2"
			},
			{
				"id": 3,
				"nombre": "plan 3",
				"precio": 200,
				"descuento": 100,
				"fecha_creacion": "2016-07-21T22:35:42.461322Z",
				"resume_es": "resume es 3",
				"resume_ing": "resume ing 3"
			}
		],
		"precio_colombia": 33,
		"precio_newzealand": 100,
		"alojamiento": [
			{
				"id": 1,
				"nombre": "alojamiento 1",
				"costo": "100"
			},
			{
				"id": 2,
				"nombre": "alojamiento 2",
				"costo": "300"
			}
		],
		"pais": "canada",
		"escuela": "Escuela 1",
		"numero_horas_semana": "1"
	}

cursos.insert_one(curso)
