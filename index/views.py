from django.shortcuts import render
from .models import about,slider
from .models import client
# Create your views here.


def home(request):
    aboutdata = about.objects.all()
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    context = {
        'about': aboutdata,
        'slider': sliderdata,
        'client': clientdata
    }

    return render(request,'index.html',context)

def aboutus(request):
    data="This is our about page"
    return render(request,'about.html')
