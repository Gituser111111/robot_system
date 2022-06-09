from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'operation/home.htm',{})
    
def pieChar(request):
	#data = {'key1':'value1','key2':'value2'}
    #return render(request, 'page.html',{'data':data}) 
	result =[['AMAZON.COM', 50 ,'電傷平台'], 
    		['ABBOTT LABORATORIES', 30], 
    		['AES', 15], 
    		['ABIOMED', 5]]


	return render(request, 'operation/pieChar.html',{'result': result})


def member(request, user_id):
	#return render(request, 'operation/menber.html' ,{'data':data})
	#class User():
	#	def __init__(self, name, account, password, email, tel, career, age):
	#		self.name = name
	#		self.account = account
	#		self.password = password
	#		self.email = email
	#		self.tel = tel
	#		self.career = career
	#		self.age = age
	
	try:
		user = User.objects.get(pk=user_id)
	except User.DoesNoExist:
		raise Http404("The user does not exist.")
	#user = get_object_or_404(User, pk=user_id)
	
	return render(request,'operation/member.htm',{'user':user})

def aboutUs(request):
	pass

def knowledge(request):
	pass

def login(requets):
	pass

def member_detail(requet):
	pass

def member_invest(request):
	pass

def register(request):
	pass

