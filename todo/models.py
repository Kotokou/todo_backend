from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField()
    favourite = models.BooleanField()
    list = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)


class TodoList(models.Model):
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"
