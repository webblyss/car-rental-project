from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='cars/')
    price = models.IntegerField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True,)


    def __str__(self) -> str:
        return f'{self.model}-{self.make}'

class Rental(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField() 
    car = models.ForeignKey(Car, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return f'{self.customer_name} - car : {self.car.model}'






