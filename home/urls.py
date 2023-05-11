from django.urls import path
from .views import home,rent


app_name = 'home'

urlpatterns = [
    path('',home,name = 'home'),
    path('rent',rent,name='rent')
]


