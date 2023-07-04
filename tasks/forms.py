from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=100)
    body = forms.CharField(max_length=1000)


class SubTaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=100)
    body = forms.CharField(max_length=1000)


class CommentForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=100)
    body = forms.CharField(max_length=1000)
