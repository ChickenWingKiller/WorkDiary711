from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('create', views.journal_create, name='create_journal'),
    path('list', views.journal_list, name='list_journal'),
    path('list_date', views.journal_date, name='list_own_journal_date'),
    re_path(r'^list_date/(?P<user_pk>[0-9]+)/$', views.other_journal_date, name='list_other_journal_date'),
    re_path(r'detail/(?P<journal_pk>[0-9]+)/$', views.journal_detail, name = 'journal_detail'),
]