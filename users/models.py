from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    

class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)


class SubTask(models.Model):
    id = models.UUIDField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=1000)


