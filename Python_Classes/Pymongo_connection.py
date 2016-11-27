from pymongo import MongoClient

class Pymongo_connection():
	"""docstring for Pymongo_connection"""
	def __init__(self):
		try:
			self.client = MongoClient('mongodb://localhost:27017')
		finally:
			self.client = MongoClient('mongodb://root:BTExjh5R@104.154.150.130:27017')

	def search_database(self, collection, table, query):
		db = self.client[collection][table]
		if query[1] != None:
			info = db.find(query[0],query[1])
		else:
			info = db.find(query[0])
		_data = []
		for _info in info:
			_info['_id'] = str(_info['_id'])
			_data.append(_info)
		return _data

	def insert_record(self, collection, table, data):
		db = self.client[collection][table]
		print db.insert(data)
