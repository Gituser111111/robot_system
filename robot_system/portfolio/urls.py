from django.urls import path

from . import views


urlpatterns = [   
    path('', views.home, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('knowledge/', views.knowledge, name='knowledge'),
    path('login/', views.login, name = 'login'),
    path('invest/',views.invest),
    path('member/<int:user_id>', views.member),
    
    
]


