from django.shortcuts import render
from django.http import HttpResponse

from .models import Bookcase

def bookcase_list(request):
    bookcases = Bookcase.objects.all()

    context = {
        "bookcases": bookcases,
    }
    return render(request, "bookcases/bookcase_list.html", context)