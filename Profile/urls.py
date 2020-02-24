from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Profile import views

urlpatterns = [
    re_path(r'ProfileList/$', views.ProfileList.as_view()),
    re_path(r'ProfileList/CiudadList/$', views.CiudadList.as_view()),
    re_path(r'ProfileList/GeneroList/$', views.GeneroList.as_view()),
    re_path(r'ProfileList/OcupacionList/$', views.OcupacionList.as_view()),
    re_path(r'ProfileList/EstadoList/$', views.EstadoList.as_view()),
    re_path(r'ProfileList/EstadoCivilList/$', views.EstadoCivilList.as_view()),
]