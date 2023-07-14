from django.urls import path, include
from . import views


urlpatterns = [
        path('overview/', views.overview, name='overview'),
        path('add_task/', views.add_task, name='add_task'),
        path('add_subtask/<task_id>', views.add_subtask, name='add_subtask'),
        path('add_comment/<id>/<task>', views.add_comment,
             name='add_comment'),
        path(r'task_view/<task_id>', views.task_view, name='task_view'),
        path('edit_task/<task_id>', views.edit_task, name='edit_task'),
        path('delete_task/<task_id>', views.delete_task, name='delete_task'),
        path('delete_subtask/<id>', views.delete_subtask, name='delete_subtask'),
        path('delete_comment/<id>', views.delete_comment, name='delete_comment'),
        ]
