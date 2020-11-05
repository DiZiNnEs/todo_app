from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest

from .models import Project


def home(request: WSGIRequest) -> render:
    project_list = Project.objects.all()
    number_tasks_project = Project.objects.count()

    context = {
        'project_list': project_list,
        'number_of_tasks_in_project': number_tasks_project,
    }

    return render(request, 'todo_app/index.html', context)
