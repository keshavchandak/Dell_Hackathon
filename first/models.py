from django.db import models

"""

class Login(models.Model):
	username=models.CharField(max_length = 10)
	password=models.Password(max_length=10)

	def __str__(self):
		return self.username

class Inventory(models.Model):
	model_No=models.CharField(max_length=20)
	model_price=models.Integer()
	model_availability=models.BooleanField()

	def __str__(self):
		return self.model_No

class Cart(models.Model):
	items=models.ManytoOne()

"""

class First(models.Model):
	text = models.CharField(max_length = 40)
	complete = models.BooleanField(default = False)

	def __str__(self):
		return self.text
