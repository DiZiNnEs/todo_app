from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.handlers.wsgi import WSGIRequest

from django.views.generic import (
    TemplateView,
    FormView,
    View
)

from django.contrib.auth import (
    forms,
    authenticate,
    login,
    logout,
)

from . import models


class HomeView(TemplateView):
    template_name = 'todo_app/index.html'

    def get_context_data(self, **kwargs) -> dict[str, models.Project]:
        return {'projects': models.Project.objects.prefetch_related('tasks')}


class ProjectView(TemplateView):
    template_name = 'todo_app/view_project.html'

    def get_context_data(self, **kwargs):
        return {'project': models.Task.objects.get(id=self.kwargs['pk'])}


class RegisterView(FormView):
    template_name = 'todo_app/register.html'
    form_class = forms.UserCreationForm
    success_url = '/login/'

    def form_valid(self, form: forms.UserCreationForm) -> super:
        form.save()
        return super(RegisterView, self).form_valid(form)


class LoginView(View):
    template_name = 'todo_app/login.html'
    form = forms.AuthenticationForm

    def get(self, request: WSGIRequest) -> render:
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request: WSGIRequest) -> render or redirect:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_is_authenticate = authenticate(request, username=username, password=password)

            if user_is_authenticate is not None:
                login(request, user_is_authenticate)
                return redirect('home')
        except ValueError:
            return redirect('login') + HttpResponse('Login or password incorrect')


class LogoutView(View):
    def get(self, request: WSGIRequest) -> redirect:
        logout(request)
        return redirect('login')
