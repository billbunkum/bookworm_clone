from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.bookcase_list, name="bookcase_list"),
    url(r'^(?P<id>\d+)/$', views.bookcase_detail, name="bookcase_detail"),
    url(r'^new/$', views.bookcase_new, name='bookcase_new'),
    url(r'^(?P<id>\d+)/edit/$', views.bookcase_edit, name='bookcase_edit'),
    url(r'^bookshelf/(?P<id>\d+)/$', views.bookshelf_detail, name="bookshelf_detail"),
    url(r'^bookshelf/(?P<id>\d+)/book/new/$', views.bookshelf_book_new, name="bookshelf_book_new"),
    url(r'^(?P<bookcase_id>\d+)/bookshelf/new/$', views.bookshelf_new, name='bookshelf_new'),
    url(r'^bookshelf/(?P<id>\d+)/edit/$', views.bookshelf_edit, name='bookshelf_edit'),
]