from django.db import models
from django.urls import reverse


class Foods(models.Model):

	Name = models.CharField(max_length=50)
	Price = models.IntegerField()
	Discription = models.CharField(max_length=250)
	Pub_date = models.DateField(auto_now_add=True)
	category = models.ManyToManyField('Category', related_name = 'item')

	def __str__(self):

		return self.Name

	def get_absolute_url(self):

		return reverse('home')

		

class Category(models.Model):

	Name = models.CharField(max_length=50)

	def __str__(self):

		return self.Name




class OrderModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    
    price = models.DecimalField(max_digits=7, decimal_places=2)

    item = models.ManyToManyField('Foods', related_name = 'order' , blank=True)

    name = models.CharField(max_length=50, blank=True)
    
    email = models.CharField(max_length=50, blank=True)
    
    street = models.CharField(max_length=50, blank=True)
    
    city = models.CharField(max_length=50, blank=True)
    

    state = models.CharField(max_length=15, blank=True)
    
    zip_code = models.IntegerField(blank=True, null=True)
    
    

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'


    def get_absolute_url(self):

    	return reverse('cart')