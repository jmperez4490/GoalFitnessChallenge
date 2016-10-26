from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^Log-In/',views.logIn),
	url(r'^(.*)/',views.blog_article),
]
