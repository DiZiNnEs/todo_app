from django.shortcuts import render, redirect

from django.views.generic.base import View

from django.core.handlers.wsgi import WSGIRequest

from django.utils.decorators import method_decorator

from django.views.generic import (
    TemplateView,

)

from django.contrib.auth import (
    forms,
    decorators,
    authenticate,
    login,
    logout
)

from . import models


class HomeView(TemplateView):
    template_name = 'todo_app/index.html'

    def get_context_data(self, **kwargs):
        return {'projects': models.Project.objects.prefetch_related('tasks')}


class RegisterView(View):
    template_name = 'todo_app/register.html'
    form = forms.UserCreationForm

    def get(self, request: WSGIRequest) -> render:
        try:
            form = self.form()
            return render(request, self.template_name, {'form': form})
        except:
            raise

    def post(self, request: WSGIRequest) -> redirect or render:
        try:
            form = self.form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        except:
            raise


class LoginView(View):
    template_name = 'todo_app/login.html'
    form = forms.AuthenticationForm

    def get(self, request: WSGIRequest) -> render:
        try:
            form = self.form()
            return render(request, self.template_name, {'form': form})
        except:
            raise

    def post(self, request: WSGIRequest) -> render or redirect:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_is_authenticate = authenticate(request, username=username, password=password)

            if user_is_authenticate is not None:
                login(request, user_is_authenticate)
                return redirect('home')
        except:
            raise


class LogoutView(View):
    def get(self, request: WSGIRequest) -> redirect:
        logout(request)
        return redirect('login')
