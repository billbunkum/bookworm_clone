from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/', views.book_detail, name='book_detail'),
]