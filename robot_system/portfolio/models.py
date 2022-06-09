from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)
	account = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=150, default='')
	tel = models.CharField(max_length=10, default='')
	career = models.CharField(max_length=15, default='')
	age = models.IntegerField(default=0)
	income = models.IntegerField(default=1000)

class Weight(models.Model):
	name = models.CharField(max_length=50)
	weight = models.FloatField(default=0)

	def get_info(self):
		return self.name, self.weight

 
class Company(models.Model):
	name = models.CharField(max_length=100)
	department = models.CharField(max_length=15) 
