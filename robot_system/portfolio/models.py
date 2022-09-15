from django.db import models

class User(models.Model):
	name = models.CharField(max_length=10)
	account = models.CharField(max_length=10)
	password = models.CharField(max_length=10)
	email = models.EmailField(max_length=10, default='')
	tel = models.CharField(max_length=10, default='')
	career = models.CharField(max_length=15, default='')
	age = models.CharField(max_length=10, default=0)
	income = models.CharField(max_length=10)

"""class Weight(models.Model):
	name = models.CharField(max_length=50)
	weight = models.FloatField(default=0)

	def get_info(self):
		return self.name, self.weight

""" 
class Company(models.Model):
	name = models.CharField(max_length=10)
	department = models.CharField(max_length=10) 

class MemberInvest(models.Model):
	userID = models.ForeignKey('User',on_delete = models.CASCADE)
	date = models.DateTimeField
	total = models.CharField(max_length =10)
	userROI = models.FloatField()
	userWeights = models.FloatField()
	userShares = models.FloatField()
	
class CompanyInvest(models.Model):
	companyID = models.ForeignKey('Company', on_delete = models.CASCADE)
	userID = models.ForeignKey('User', on_delete = models.CASCADE)
	date = models.DateTimeField
	weights = models.FloatField()
	shares = models.FloatField()
	

	
	
