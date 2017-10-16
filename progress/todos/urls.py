from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^adding$', views.adding, name='adding'),
]