from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, null=True)
    executor = models.ManyToManyField(Executor)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=32, null=True)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.name
