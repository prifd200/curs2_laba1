from django.urls import path
from . import  views

urlpatterns = [
    path('', views.general, name='home'),
    path('about-us', views.about, name='about'),
    path('mygithub', views.labs, name='labs'),
]