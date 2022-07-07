from django.urls import path
from . import views           # .is placed because views in from same directory
urlpatterns = [

    path('',views.authlogin, name = 'login'),
    path('registration/',views.authregistration, name = 'registration'),
    path('forget-password/',views.forgetpassword, name = 'forgetpassword'),
    path('logout/',views.authlogout, name = 'logout'),
]
