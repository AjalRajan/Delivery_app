from django.shortcuts import render
from restaurant.models import OrderModel,Foods
from django.views.generic import ListView,CreateView
from restaurant.forms import orderform

class CustomerView(ListView):


	model = Foods

	template_name = 'customer/chome.html'

class Addorder(CreateView):


	model = OrderModel

	form_class = orderform
	
	template_name = 'customer/order.html'
