from os import kill
from re import sub
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models, forms
from .models import Task, SubTask
import logging

logging.basicConfig(filename="tasks.log", encoding="utf-8")
logger = logging.getLogger(__name__)

# from forms import TaskForm


def overview(request):
    if request.user.is_authenticated:
        return render(request, "tasks/overview.html/")
    return redirect("/users/dashboard/")


def add_task(request):
    form = forms.TaskForm()
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            new_task = models.Task(
                title=form.cleaned_data["title"],
                subtitle=form.cleaned_data["subtitle"],
                body=form.cleaned_data["body"],
                user=request.user,
            )
            print(f"Form processed, task created: {new_task}")
            new_task.save()
            logger.info(f"POST request made to add_task by {request.user}")
            return redirect('task_view', task_id=new_task.id)
            # return render(
            #     request, "tasks/add_task.html", context={"form": form, "complete": True}
            # )
    logger.info(f"GET request made to add_task by {request.user}")
    return render(request, "tasks/add_task.html", context={"form": form})


def task_view(request, task_id):
    task = request.user.tasks.filter(id=task_id).first()
    return render(request, "tasks/task_view.html", context={"task": task})


def add_subtask(request, task_id):
    form = forms.SubTaskForm()
    task = request.user.tasks.filter(id=task_id).first()
    if request.method == "POST":
        form = forms.SubTaskForm(request.POST)
        if form.is_valid():
            new_subtask = models.SubTask(
                task=task,
                user=request.user,
                title=form.cleaned_data["title"],
                subtitle=form.cleaned_data["subtitle"],
                body=form.cleaned_data["body"],
            )
            new_subtask.save()
            logger.info(
                f"POST request made to add_subtask by ' \
                        f'{request.user.username}"
            )
            return redirect(f"task_view", task_id=task.id)
    logger.info(f"GET request made to add_subtask by {request.user.username}")
    return render(
        request, "tasks/add_subtask.html", context={"form": form, "task": task}
    )


def add_comment(request, id, task):
    task = request.user.tasks.filter(id=id).first() if task else False
    subtask = request.user.tasks.subtasks.filter(id=id) if not task else False
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            if task:
                new_task_comment = models.Comment(user=request.user,
                                                  task=task,
                                                  subtask=None,
                                                  title=form.cleaned_data['title'],
                                                  body=form.cleaned_data['body'],)
                new_task_comment.save(force_insert=True)
                return redirect(f"task_view", task_id=task.id)
            new_subtask_comment = models.Comment(user=request.user,
                                              task=None,
                                              subtask=subtask,
                                              title=form.cleaned_data['title'],
                                              body=form.cleaned_data['body'],)
            new_subtask_comment.save(force_insert=True)
            return redirect(f"task_view", task_id=subtask.task.id)
    form = forms.CommentForm()
    task = request.user.tasks.filter(id=id).first() if task else None
    subtask = request.user.tasks.subtasks.filter(id=id) if not task else None
    logger.info(f"GET request made to add_comment by {request.user.username}")
    return render(
        request,
        "tasks/add_comment.html",
        context={"task": task, "subtask": subtask, "form": form},
    )


def edit_task(request, task_id):
    task = request.user.tasks.filter(id=task_id).first()
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.subtitle = form.cleaned_data['subtitle']
            task.body = form.cleaned_data['body']
            task.save()
            return redirect('task_view', task_id=task.id)
    form = forms.TaskForm(dict(title=task.title, subtitle=task.subtitle, body=task.body))
    return render(request, 'tasks/edit_task.html', context={'form': form})


def delete_task(request, task_id):
    task = request.user.tasks.filter(id=task_id).first()
    if task.user == request.user:
        task.delete()
        return redirect('overview')
    return redirect('overview')

def delete_subtask(request, id):
    subtask = request.user.subtasks.filter(id=id).first()
    if subtask.user == request.user:
        subtask.delete()
        return redirect('overview')
    return redirect('overview')

def delete_comment(request, id):
    comment = request.user.comments.filter(id=id).first()
    if comment.user == request.user:
        comment.delete()
        return redirect('overview')
    return redirect('overview')



