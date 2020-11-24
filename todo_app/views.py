from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.handlers.wsgi import WSGIRequest

from django.views.generic import (
    TemplateView,
    FormView,
    View,
    edit,
)

from django.contrib.auth import (
    forms,
    logout,
    views,
)
from django.views.generic import (
    TemplateView,
    FormView,
    View,
)

from django.core.handlers.wsgi import WSGIRequest

from django.shortcuts import redirect


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


class LoginView(views.LoginView):
    template_name = 'todo_app/login.html'

    def get_success_url(self) -> super:
        return super(LoginView, self).get_success_url()


class LogoutView(View):
    def get(self, request: WSGIRequest) -> redirect:
        logout(request)
        return redirect('login')


class CreateProject(edit.CreateView):
    model = models.Task
    template_name = 'todo_app/CRUD/create_project.html'
    fields = '__all__'
    success_url = '/'


class UpdateProject(edit.UpdateView):
    model = models.Task
    template_name = 'todo_app/CRUD/update_project.html'
    fields = '__all__'
    success_url = '/'


class DeleteProject(edit.DeleteView):
    model = models.Task
    template_name = 'todo_app/CRUD/delete_project.html'
    fields = '__all__'
    success_url = '/'
