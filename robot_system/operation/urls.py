from django.urls import path

from . import views

#app_name = 'opertion'
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),   
    path('', views.home, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('knowledge/', views.knowledge, name='knowledge'),
    path('login/', views.login, name = 'login'),
    path('member/',views.member,name = 'member'),
    path('member/<int:user_id>/',views.member ),
    path('pieChar', views.pieChar, name='pieChar'),

]


