from django.shortcuts import render, get_object_or_404
from .models import User, Weight

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



def register(request):
	pass

