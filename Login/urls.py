from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken

from Login import views

urlpatterns = [
    re_path(r'^', CustonAuthToken.as_view()),
    #Hola soy roberto

    re_path(r'example_List2/$', views.Example2List2.as_view()),
]