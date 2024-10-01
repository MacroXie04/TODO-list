from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='todo_list')

    def __str__(self):
        return f"{self.user.username}'s Todo List"


class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')
    item = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return {
            'todo_list': self.todo_list,
            'item': self.item,
            'is_completed': self.is_completed,
            'created_at': self.created_at,
            'due_date': self.due_date
        }