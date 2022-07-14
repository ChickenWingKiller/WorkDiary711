from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('create', views.journal_create, name='create'),
    path('list', views.journal_list, name='list'),
]