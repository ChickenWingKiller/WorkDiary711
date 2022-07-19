from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^all/$', views.user_list, name='user_list'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.login_test, name='login'),
    path('s/', views.s, name='test'),
    path('test/', views.test, name='t1'),
    path('login_test', views.login_test, name='lt')
]