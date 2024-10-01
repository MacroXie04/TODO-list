from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import TodoItem

# 用户注册
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# 用户登录
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# 创建TODOItem
class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['item', 'is_completed', 'due_date']
