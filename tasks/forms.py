from django import forms
# from django.forms import ModelForm
# from .models import Task, SubTask, Comment


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=100, required=False)
    body = forms.CharField(max_length=1000)


class SubTaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=100, required=False)
    body = forms.CharField(max_length=1000)


class CommentForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    body = forms.CharField(max_length=1000)
