from django.shortcuts import render, get_object_or_404

from .models import Book

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)

    context = {
        "book": book,
    }

    return render(request, "books/book_detail.html", context)
