from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from .models import Bookcase

def bookcase_list(request):
    bookcases = Bookcase.objects.annotate(shelf_count=Count('bookshelf')).all()

    context = {
        "bookcases": bookcases,
    }
    return render(request, "bookcases/bookcase_list.html", context)