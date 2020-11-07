from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest

from .models import Project


def home(request: WSGIRequest) -> render:
    project_list = Project.objects.all()
    numbers_project = Project.objects.count()

    context = {
        'project_list': project_list,
        'numbers_of_project': numbers_project,
    }

    return render(request, 'todo_app/index.html', context)
