



from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name ='Home'),
    path('about', views.about, name ='about'),
    path('services', views.services, name ='service'),
    path('contacts', views.contacts, name ='contact'),

]