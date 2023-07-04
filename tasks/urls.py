from django.urls import path, include
from . import views


urlpatterns = [
        path('overview/', views.overview, name='overview'),
        path('add_task/', views.add_task, name='add_task'),
        path('add_subtask/<task_id>', views.add_subtask, name='add_subtask'),
        path(r'task_view/<task_id>', views.task_view, name='task_view'),
        ]
