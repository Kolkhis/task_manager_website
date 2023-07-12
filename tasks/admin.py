from django.contrib import admin
from .models import Task, SubTask, Comment

admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Comment)

# Register your models here.
