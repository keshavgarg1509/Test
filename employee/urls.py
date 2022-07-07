from django.urls import path
from . import views # .is placed because views in from same directory
urlpatterns = [
    path('',views.employee),
    path('profile/',views.profile, name='profile')
]
