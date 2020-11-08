from django.shortcuts import (
    render,
    redirect,
)

from django.contrib import messages

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required

from django.core.handlers.wsgi import WSGIRequest

from .models import Project


@login_required(login_url='login')
def home(request: WSGIRequest) -> render:
    projects = Project.objects.prefetch_related('tasks')
    context = {
        'projects': projects,
    }

    return render(request, 'todo_app/index.html', context)


def register_page(request: WSGIRequest) -> redirect or render:
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.info(request, 'Some forms are wrong')
                print('form isn\'t valid')
        else:
            print('Method isn\'t POST')

        context = {'form': form}
        return render(request, 'todo_app/register.html', context)


def login_page(request: WSGIRequest) -> redirect or render:
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = AuthenticationForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_is_authenticate = authenticate(request, username=username, password=password)

            if user_is_authenticate is not None:
                login(request, user_is_authenticate)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
                print('user is none')
        else:
            print('request isn\'t POST method')

        return render(request, 'todo_app/login.html', {'form': form})


def user_logout(request: WSGIRequest) -> redirect:
    logout(request)
    return redirect('login')
