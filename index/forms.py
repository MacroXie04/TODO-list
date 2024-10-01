from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# 用户注册
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# 用户登录
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)