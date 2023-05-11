from django.shortcuts import redirect, render,get_object_or_404
from .models import Car,Rental
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def home(request):
    car = Car.objects.all()
    return render(request,'index.html',{'car':car})



def rent(request,pk):

    obj = get_object_or_404(Car, id=pk)
    context = {'data': obj}

    car_id = obj.id

    if request.method == 'POST':
        pick_date = request.POST['pickup-date']
        return_date = request.POST['return-date']
        customer_name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['driver-age']
        customer_license = request.POST['driver-Licenses']

        customer = Rental.objects.create(customer_name=customer_name,customer_email = email,customer_phone=phone,customer_age=age,customer_licenses=customer_license,start_date=pick_date,end_date=return_date,car_id=car_id)

        customer.save()
        print('car rent successfully')
        messages.info(request,'car rent successfully')
        return HttpResponseRedirect(request.path_info)
    else:
        return render(request,'rent.html',context)


