from django.db import models

"""
class User (models.Model):
    userName = models.CharFieled(max_length=20, null = False)
    userAccount = models.CharFieled(max_length=20, null = False)
    userPassward = models.CharFieled(max_length=50)

    def __str__(self):
        return self.userName

class Company (models.Model):
    companyName = models.CharFieled(max_length = 30, null = False)
    companyDepart = models.CharFieled(max_length = 10, null = False)

    def __str__(self):
        return self.companyName, self.companyDepart

class Price (models.Model):
    date = models.DateTimeField(auto_now = True)
    company_id = models.ForeignKey('Company')
    price = models.IntegerField()
    ROI = models.FloatField()



class Menber_invest (models.Model):
    date = models.DateTimeField(auto_now = True)



class Investcombination(models.Model):
    company_id = models.ForeignKey('Company')
    weights = models.ArraryField(models.CharFieled())
    shares = models.FloatField()

"""

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=100)
	user_account = models.CharField(max_length=50)
	user_password = models.CharField(max_length=50)
	user_email = models.EmailField(max_length=150)
	user_tel = models.CharField(max_length=10)
	user_career = models.CharField(max_length=15)
	user_age = models.IntegerField()


class Department(models.Model):
	name = models.CharField(max_length=100)
    
class Company(models.Model):
	name = models.CharField(max_length=100)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

"""
class Invest_combination(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	weights = models
	shares
	conbination_id

class Member_invest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	combination = models.ForeignKey(Invest_combination, on_delete=models.CASCADE)
	date = models.DateTimeField()
	total = models.IntegerField(default=0)




class Price(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	date = models.DateTimeField('Closing price')
	ROI = models.FloatField(default=0)
	
	"""
