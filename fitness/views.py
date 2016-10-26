from django.shortcuts import render

# Create your views here.
def index(request):
	context = {}
	return render(request, 'fitness/index.html',context)

def blog_article(request,text):
	print text
	context = {}
	return render(request, 'fitness/blog.html',context)

def logIn(request):
	context = {}
	return render(request, 'fitness/logIn.html', context)

def clean_array(path, index = 0):
	if path[index] == "":
		del path[index]
		index = index + 1
		if len(path) > 1:
			return clean_array(path, index)
		else:
			return path
	else:
		index = index + 1
		if len(path) < index:
			return clean_array(path, index)
		else:
			return path