from django.shortcuts import render, redirect
from Python_Classes.request_info import request_info
import requests

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

def subscription(request):
	_data = dict(request.POST)
	post_data = {
		'secret': '6LfewgwUAAAAADeXCUyj0DADCrH8Zx7s6l4KIUOv',
		'response':_data['g-recaptcha-response'],
		'remoteip':'',
		}
	del _data['g-recaptcha-response']
	response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=post_data)
	content = response.json()
	content.update(_data)
	db_connect.register_reader(content)
	if content['success']:
		print content
		return render(request, 'fitness/subscription.html',content, content_type = 'text/html')
	else:
		return redirect(_data['refferal_url']+"#error")

def logIn(request):
	return render(request, 'fitness/logIn.html', context)
