from django.shortcuts import render, redirect
from . import models, forms
from .models import Task
# from forms import TaskForm


def overview(request):
    if request.user.is_authenticated:
        return render(request, 'tasks/overview.html/')
    return redirect('/users/dashboard/')

def add_task(request):
    form = forms.TaskForm()
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            new_task = models.Task(title=form.cleaned_data['title'], subtitle=form.cleaned_data['subtitle'],
                                   body=form.cleaned_data['body'], user=request.user)
            print(f'Form processed, task created: {new_task}')
            new_task.save()
            return render(request, 'tasks/add_task.html', context={'form': form, 'complete': True})

    return render(request, 'tasks/add_task.html', context={'form': form})

def task_view(request, task_id):
    task = request.user.tasks.filter(id=task_id).first()
    return render(request, 'tasks/task_view.html', context={'task': task})


def add_subtask(request, task_id):
    form = forms.SubTaskForm()
    task = request.user.tasks.filter(id=task_id).first()
    if request.method == 'POST':
        form = forms.SubTaskForm(request.POST)
        if form.is_valid():
            new_subtask = models.SubTask(task=task, user=request.user, title=form.cleaned_data['title'],
                                         subtitle=form.cleaned_data['subtitle'], body=form.cleaned_data['body'])
            new_subtask.save()
            return redirect(f'/task_view/{task.id}')
    return render(request, 'tasks/add_subtask.html', context={'form': form, 'task': task})

def add_comment(request, id, is_task: bool):
    form = forms.CommentForm()
    task = request.user.tasks.filter(id=id).first() if is_task else None
    subtask = request.user.tasks.subtasks.filter(id=id) if not is_task else None
    # TODO: FINISH
    # if request.method == 'POST':
        # if task:
        #     new_task_comment = 
    return render(request, 'tasks/add_comment/', context={'task': task, 'subtask': subtask, 'form': form} )


        




