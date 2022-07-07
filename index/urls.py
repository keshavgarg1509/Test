from django.urls import path
from . import views           # .is placed because views in from same directory
urlpatterns = [

    path('',views.home, name = 'home'),
    path('aboutus/',views.about, name= 'about'),
]
