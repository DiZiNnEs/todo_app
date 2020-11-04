from django.contrib import admin
from .models import (
    Project,
    Task,
    Executor,
)

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Executor)