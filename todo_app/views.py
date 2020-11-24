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

    def get_context_data(self, **kwargs) -> dict[str, models]:
        return {'projects': models.Project.objects.prefetch_related('tasks')}


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
