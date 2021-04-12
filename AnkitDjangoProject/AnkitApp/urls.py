
from django.urls import path
from AnkitApp import views

urlpatterns = [     
    path('', views.home, name='Home'),
    path('about', views.about, name='About'),
    path('contact', views.contact, name='Contact Us'),
    path('portfolio', views.portfolio, name='Portfolio'), 

]