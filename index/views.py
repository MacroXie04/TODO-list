from .forms import UserLoginForm, UserRegisterForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import TodoItemForm
from .models import TodoItem
from .models import TodoList
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout


@login_required(login_url='/login/')
def complete_todo(request, item_id):
    todo_item = get_object_or_404(TodoItem, id=item_id)
    if todo_item.todo_list.user != request.user:
        return HttpResponseForbidden("You are not allowed to complete this item.")
    todo_item.is_completed = True
    todo_item.save()
    return redirect('index')


@login_required(login_url='/login/')
def delete_item(request, item_id):
    todo_item = get_object_or_404(TodoItem, id=item_id)
    if todo_item.todo_list.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this item.")
    todo_item.delete()
    return redirect('index')


@login_required(login_url='/login/')
def web_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.todo_list = request.user.todo_list
            todo_item.save()
            return redirect('index')
    else:
        form = TodoItemForm()

    todo_items = TodoItem.objects.filter(todo_list=request.user.todo_list)
    items_completed = todo_items.filter(is_completed=True)
    items_not_completed = todo_items.filter(is_completed=False)

    content = {
        'form': form,
        'todo_name': request.user.todo_list,
        'items_completed': items_completed,
        'items_not_completed': items_not_completed,
    }

    return render(request, 'index.html', content)


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
