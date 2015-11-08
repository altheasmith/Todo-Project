from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.TextField()
    owner = models.ForeignKey(User)
    due_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.task
