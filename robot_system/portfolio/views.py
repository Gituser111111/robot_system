from django.shortcuts import render, get_object_or_404
from .models import User#, Weight
from django.views.generic import View
import numpy as np
import pandas as pd
from django.core.mail import send_mail


def home(request):
    return render(request, 'portfolio/home.htm',{})
    
def member(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'portfolio/member.htm', {'user':user})
 
 
def invest(request):
    w = Weight.objects.all()
    weight = [[x.name, x.weight] for x in w]
    return render(request, 'portfolio/invest.htm', {'weight': weight})
	
	
def aboutUs(request):
    return render(request, 'portfolio/aboutUs.htm' ,{})

def knowledge(request):
    return render(request, 'portfolio/knowledge.htm',{})

def login(request):
    return render(request, 'portfolio/login.htm',{})

def df_db(request):
    #db_query = df_2_db.objects.all()
    
    data = np.array([x for x in range(12)]).reshape((4, 3))
    df = pd.DataFrame(list(data),columns=['AMAZON.COM', 'ABBOTT LABORATORIES', 'AES'])
    
    df_f = df.iloc[2:3]
        
    return render(request, 'portfolio/df.htm',{'df':df_f} )
    


def register(request):
	pass

class ForgetPwdView(View):
	'''忘記密碼'''
	def get(self,request):
		forget_form=ForgetForm()
		return render(request,'forget.htm',{'forget_form':forget_form})
	def post(self,request):
		forget_form = ForgetForm(request.POST)
		if forget_form.is_valid():
			email=request.POST.get('email','')
			send_register_email(email,'forget')
			return render(request,'sendSuccess.htm')
		else:
			return render(request,'forget.htm',{'forget_form':forget_form})


class ResetView(View):
	'''重置密碼'''
	def get(self,request,active_code):
		record=EmailVerifyRecord.objects.filter(code=active_code)
		print(record)
		if record:
			for i in record:
				email=i.email,is_register=UserProfile.objects.filter(email=email)
				if is_register:
					return render(request,'pwdReset.htm',{'email':email})
		return redirect('index')
#因為<form>表單中的路徑要是確定的，所以post函式另外定義一個類來完成
class ModifyView(View):
	"""重置密碼post部分"""
	def post(self,request):
		reset_form=ResetForm(request.POST)
		if reset_form.is_valid():
			pwd1=request.POST.get('newpwd1','')
			pwd2=request.POST.get('newpwd2','')
			email=request.POST.get('email','')
			if pwd1!=pwd2:
				return render(request,'pwdReset.htm',{'msg':'密碼不一致！'})
			else:
				user=UserProfile.objects.get(email=email)
				user.password=make_password(pwd2)
				user.save()
				return redirect('index')
		else:
			email=request.POST.get('email','')
			return render(request,'pwdReset.htm',{'msg':reset_form.errors})
