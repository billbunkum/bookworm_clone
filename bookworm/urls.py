from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookcases/', include('bookcases.urls', namespace='bookcases')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^', include('core.urls', namespace='core'))
]
