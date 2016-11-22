from Pymongo_connection import Pymongo_connection

class request_info:
	def __init__(self):
		self.db = Pymongo_connection()

	def get_top_blogs(self):
		_data = [
			{},
			{
				"title":1,
				"summary":1,
				"uri":1,
				"timestamp":1,
				"image":1
			}
		]
		return self.db.search_database("Articles_List", "Articles", _data)

	def get_blog(self, title):
		_data = [
			dict(
				uri = title
			),
			None
		]
		return self.db.search_database("Articles_List", "Articles", _data)

	def get_blog_list(self,text):
		_data = [
			{
				"uri":{"$ne":text}
			},
			{
				"title":1,
				"uri":1
			}
		]
		return self.db.search_database("Articles_List", "Articles", _data)

