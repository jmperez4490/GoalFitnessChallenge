from pymongo import MongoClient, DESCENDING
from django.conf import settings

class Pymongo_connection():
	"""docstring for Pymongo_connection"""
	def __init__(self):
		self.client = MongoClient(settings.MONGODB_CONFIG)

	def search_database(self, collection, table, query, _limit = 1):
		db = self.client[collection][table]
		if query[1] != None:
			info = db.find(query[0],query[1]).sort("timestamp",DESCENDING).limit(_limit)
		else:
			info = db.find(query[0]).sort("timestamp",DESCENDING).limit(_limit)
		_data = []
		for _info in info:
			_info['_id'] = str(_info['_id'])
			_data.append(_info)
		return _data

	def insert_record(self, collection, table, data):
		db = self.client[collection][table]
		print db.insert(data)

	def query_search(self, collection, table, query, _limit = 15):
		db = self.client[collection][table]
		info = db.find(
			{
				"$text": {
					"$search":query
				}
			},
			{
				"score":{
					"$meta":"textScore"
				},
				"summary":1,
				"body":1,
				"uri":1,
				"timestamp":1,
				"title":1
			}
		).sort("textScore",DESCENDING).limit(_limit)
		_data = dict()
		for _info in info:
			_info['_id'] = str(_info['_id'])
			_data.update({_info['_id']:_info})
		return _data
