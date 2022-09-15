"""
from django.forms import ModelForm
from django import forms
from models import User
from django.core.exceptions import NON_FIELD_ERRORS



class UserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=('name','account','password','email','tel','career','age','income')
"""
from django import forms
from captcha.fields import CaptchaField
.......
#forget.html中，用於驗證郵箱格式和驗證碼
class ForgetForm(forms.Form):
email=forms.EmailField(required=True)
captcha=CaptchaField(error_messages={'invalid':'驗證碼錯誤'})
#reset.html中，用於驗證新設的密碼長度是否達標
class ResetForm(forms.Form):
newpwd1=forms.CharField(required=True,min_length=6,error_messages={'required': '密碼不能為空.', 'min_length': "至少6位"})
newpwd2 = forms.CharField(required=True, min_length=6, error_messages={'required': '密碼不能為空.', 'min_length': "至少6位"})
