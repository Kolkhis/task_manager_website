from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Task {self.id}: Author={self.user.name}, {self.title=}, {self.subtitle=}"



class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"SubTask {self.id}: Author={self.user.name}, {self.title=}, {self.subtitle=} "


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment {self.id}: Author={self.user.name}, {self.title=}"


