from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField(default = 0.00)
	quantity = models.IntegerField(default = 0)
	

	def __str__(self):
		return self.title

class OrderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)


	def __str__(self):
		return self.title

class Order(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.User