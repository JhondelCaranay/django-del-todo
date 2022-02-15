from django.urls import path
from .views import index, create_todo, todo_delete, todo_detail, todo_edit


urlpatterns = [
    path('', index, name='index'),
    path('create/', create_todo, name='create-todo'),
    path('todo/<id>/', todo_detail, name='todo'),
    path('todo-delete/<id>/', todo_delete, name='todo-delete'),
    path('edit-delete/<id>/', todo_edit, name='todo-edit'),
]
