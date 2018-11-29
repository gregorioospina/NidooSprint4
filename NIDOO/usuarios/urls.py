from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^$', views.index),
    url(r'^usuarios/', views.UsuarioList),
    url(r'^capacidades/', views.CapacidadList, name='capacidadList'),
    url(r'^capacidad/(?P<id_capacidad>\d+)/$', views.CapacidadEdit, name='capacidadList'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('social_django.urls')),
]