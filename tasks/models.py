from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Models go here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task {self.id}: Author={self.user.name}, {self.title=}, {self.subtitle=}"

    def __repr__(self):
        return f"<Task {self.id}> owned by {self.user.name}"



class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=50)
    body = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"SubTask {self.id}: Author={self.user.name}, {self.title=}, {self.subtitle=} "

    def __repr__(self):
        return f"<SubTask {self.id}> owned by {self.user.name}"


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

    def __repr__(self):
        return f"<Comment {self.id}> owned by {self.user.name}"


