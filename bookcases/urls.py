from django.conf.urls import url
>>>>>>> 7423c664f8c8cecd917e65eebda94d66957ae57c

from . import views

urlpatterns = [
    url(r'^$', views.bookcase_list, name='bookcase_list'),
    url(r'^(?P<id>\d+)/$', views.bookcase_detail, name='bookcase_detail'),
]