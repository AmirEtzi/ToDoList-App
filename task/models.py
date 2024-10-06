from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ToDoTask(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now())
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
