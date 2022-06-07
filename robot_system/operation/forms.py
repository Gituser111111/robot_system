from django import models
from Admin.models import *
from store.models import Category


class User_forms(forms.ModelForm):
    class Mata:
        model = User
        fields=['__all__',
           # 'user_name',
           # 'user_account',
           # 'user_password',
           # 'user_email',
           # 'user_tel',
           # 'user-career',
           # 'user_age',

        ]
    weights = {
        'userPassword' : forms.passwordInput()
    }