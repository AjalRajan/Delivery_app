from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from restaurant.models import Foods , OrderModel
from restaurant.forms import AddForm
from django.urls import reverse_lazy
from django.utils.timezone import datetime


class HomeView(ListView):

	model = Foods
	ordering = ['Price' , 'Name' , 'Pub_date']
	template_name = 'restaurant/home.html'

class AddView(CreateView):

	model = Foods
	form_class = AddForm
	template_name = 'restaurant/add.html'	


class DeleteView(DeleteView):

	model = Foods
	
	template_name = 'restaurant/delete.html'	

	success_url = reverse_lazy('home')

class AccountView(ListView):


	model = OrderModel
	

	template_name = 'restaurant/account.html'

	def get(self, request, *args, **kwargs):

		today = datetime.today()
		orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)
		
		total_revenue = 0

		for order in orders:

			total_revenue += order.price

		context = {

			'orders':orders,
			'total_revenue': total_revenue,
			'total_orders':len(orders)
		}


		return render(request , 'restaurant/account.html' , context)

	
	def test_func(self):
		return self.request.user.groups.filter(name='Staff').exists()