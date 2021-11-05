from django.contrib import admin
from django.urls import path, include
from .views import index, todo_list, todo_detail, todo_delete , todo_update

app_name = 'todolist'

urlpatterns = [
    path('', index, name='todo-index'),
    path('todolist/', todo_list, name='todo-list'),
    path('task/<int:task_id>/view', todo_detail, name='todo-details'),
    path('task/<int:task_id>/delete', todo_delete, name='todo-delete'),
    path('task/<int:task_id>/update', todo_update, name='todo-update')

]
