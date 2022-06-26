from django import forms
from .models import Foods,OrderModel

class AddForm(forms.ModelForm):

	class Meta:

		model = Foods

		fields = ('Name' , 'Price' , 'Discription')

		widgets = {

			'Name' :forms.TextInput(attrs = {'class': 'form-control' }),

			'Price' :forms.TextInput(attrs = {'class': 'form-control' }),

			'Discription' :forms.Textarea(attrs = {'class': 'form-control'}),
		}



class orderform(forms.ModelForm):

	class Meta:

		model = OrderModel

		fields = ('item','name' , 'email' , 'street' , 'city' , 'state' , 'zip_code')

		widgets = {

			'item' :forms.Select(attrs = {'class': 'form-control'}),
			'name' :forms.TextInput(attrs = {'class': 'form-control' }),

			'email' :forms.TextInput(attrs = {'class': 'form-control' }),

			'street' :forms.TextInput(attrs = {'class': 'form-control'}),

			'city' :forms.TextInput(attrs = {'class': 'form-control'}),

			'state' :forms.TextInput(attrs = {'class': 'form-control'}),

			'zip_code' :forms.TextInput(attrs = {'class': 'form-control'}),

			
			

		}