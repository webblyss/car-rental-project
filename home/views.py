from django.shortcuts import render
from .models import Car
# Create your views here.


def home(request):
    car = Car.objects.all()
    return render(request,'index.html',{'car':car})



def rent(request,pk):

    car = Car.objects.get(pk=pk)

    return render(request,'rent.html',{'data':car})


