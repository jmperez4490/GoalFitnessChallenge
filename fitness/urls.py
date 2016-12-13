from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^Articles/(.*)/',views.blog_article),
	url(r'^Newsletter/', views.subscription),
]
