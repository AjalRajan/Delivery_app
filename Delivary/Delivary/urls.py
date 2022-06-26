
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('restaurant.urls')),
    path('' , include('django.contrib.auth.urls')),
    path('customer/' , include('customer.urls')),
   

]
