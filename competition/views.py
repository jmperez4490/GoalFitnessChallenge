from django.shortcuts import render, redirect
from Python_Classes.request_info import request_info

# Create your views here.
def private_profile(request):
	return render(request, 'competition/private_profile.html')

def public_profile(request):
	return render(request, 'competition/public_profile.html')

def log_in(request):
	return render(request, 'competition/log_in.html')