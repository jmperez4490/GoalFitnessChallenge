from Pymongo_connection import Pymongo_connection
from datetime import datetime
class request_info:
	def __init__(self):
		self.db = Pymongo_connection()

	def get_top_blogs(self, limit):
		_data = [
			{
				"timestamp":{"$lte":datetime.utcnow()}
			},
			{
				"title":1,
				"summary":1,
				"uri":1,
				"timestamp":1,
				"image":1
			}
		]
		return self.db.search_database("Articles_List", "Articles", _data, limit)

	def get_blog(self, title):
		_data = [
			dict(
				uri = title
			),
			None
		]
		return self.db.search_database("Articles_List", "Articles", _data)

	def get_blog_list(self,text, limit):
		_data = [
			{
				"uri":{
					"$ne":text
				},
				"timestamp":{
					"$lte":datetime.utcnow()
				}
			},
			{
				"title":1,
				"uri":1
			}
		]
		return self.db.search_database("Articles_List", "Articles", _data, limit)

	def register_reader(self, information):
		self.db.insert_record("Articles_List","Newsletter",information)

