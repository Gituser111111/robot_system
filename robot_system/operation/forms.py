from django import models
from Admin.models import *

class User_forms(forms.ModelForm):
    class Mata:
        model = User
        fields=[
            'userName',
            'userAccount',
            'userPassword'
        ]
    weights = {
        'userPassword' : forms.passwordInput()
    }