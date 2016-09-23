from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^new/$', views.book_new, name='book_new'),
    url(r'^(?P<id>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^(?P<id>\d+)/edit/$', views.book_edit, name='book_edit'),
]