
from django.urls import path
from restaurant.views import *
urlpatterns = [
    
    path("" , HomeView.as_view() , name = 'home'),

    path("add_food" , AddView.as_view() , name = 'add'),
    
    path("delete_food<int:pk>/" , DeleteView.as_view() , name = 'delete'),

    path("account/" , AccountView.as_view() , name = 'account'),
]



