from django.shortcuts import render
from .forms import RentalForm
# Create your views here.


def home(request):


    return render(request,'index.html',{})



def rent(request):

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = RentalForm()

    return render(request,'rent.html',{'form': form})


