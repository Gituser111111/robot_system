from django.urls import path
from portfolio.views import ForgetPwdView,ResetView,ModifyView
from . import views


urlpatterns = [   
    path('', views.home, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('knowledge/', views.knowledge, name='knowledge'),
    path('login/', views.login, name = 'login'),
    path('invest/',views.invest),
    path('member/<int:user_id>', views.member),
    path('df/',views.df_db),
    #忘記密碼
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    #重置密碼
    path('reset/<str:active_code>',ResetView.as_view(),name='reset'),
    path('modify/',ModifyView.as_view(),name='modify'),
    
    
]


