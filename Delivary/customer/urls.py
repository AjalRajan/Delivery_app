
from django.urls import path
from customer.views import *
urlpatterns = [

    path('' , CustomerView.as_view() , name = 'chome'),
    path('order_food' , Addorder.as_view() , name = 'order')
]



