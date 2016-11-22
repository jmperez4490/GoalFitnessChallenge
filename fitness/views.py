from django.shortcuts import render
from Python_Classes.request_info import request_info

db_connect = request_info()

# Create your views here.
def index(request):
	context = dict(
			data = db_connect.get_top_blogs()
		)
	return render(request, 'fitness/index.html',context)

def blog_article(request,text):
	context = dict( 
			data = db_connect.get_blog(text),
			blog_list = db_connect.get_blog_list(text)
		)
	return render(request, 'fitness/blog.html',context, content_type = 'text/html')

def logIn(request):
	return render(request, 'fitness/logIn.html', context)
