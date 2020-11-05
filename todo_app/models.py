from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=32, null=True)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
