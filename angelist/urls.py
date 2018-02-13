from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$',mainpage),
    url(r'^investors$',home),
    url(r'^company$',companies),
]