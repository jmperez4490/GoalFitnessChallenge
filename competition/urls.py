from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^',views.log_in),
	url(r'^Profile/',views.private_profile),
	url(r'^Public-Profile/',views.public_profile),
]