from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest

from .models import (
    Project,
    Task,
)


def home(request: WSGIRequest) -> render:
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'todo_app/index.html', context)
