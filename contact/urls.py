from django.urls import path
from . import views           # .is placed because views in from same directory
urlpatterns = [

    path('contact/',views.contact, name = 'contact'),
]
