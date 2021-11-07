from django.urls import path, include
from .views import index, movies_list, movies_delete, movies_update, movies_details, movies_create

app_name = 'movies'

urlpatterns = [
    path('', movies_list, name='movies-list'),
    path('movie/<int:pk>/view', movies_details, name='movies-details'),
    path('movie/<int:pk>/delete', movies_delete, name='movies-delete'),
    path('movie/<int:pk>/update', movies_update, name='movies-update'),
    path('create', movies_create, name='movies-create'),
]
