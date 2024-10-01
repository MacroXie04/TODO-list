from .forms import UserLoginForm, UserRegisterForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import TodoItemForm
from .models import TodoItem
from .models import TodoList


@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.todo_list = request.user.todo_list  # Assuming each user has a TodoList
            todo_item.save()
            return redirect('index')
    else:
        form = TodoItemForm()

    todo_items = TodoItem.objects.filter(todo_list=request.user.todo_list)
    return render(request, 'index.html', {'form': form, 'todo_items': todo_items})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            TodoList.objects.create(user=user)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})