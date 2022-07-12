from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^users$', views.user_list, name='user_list'),
    re_path(r'^users/register/$', views.register, name='register'),
    re_path(r'^users/login/$', views.login, name='login'),
]