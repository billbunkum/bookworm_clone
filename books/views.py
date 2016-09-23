from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import Book

def book_list(request):
    books = Book.objects.all()

    breadcrumbs = (
        ('Books', ),
    )

    context = {
        "books": books,
        "breadcrumbs": breadcrumbs,
    }
    return render(request, "books/book_list.html", context)

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    breadcrumbs = None

    if book.bookshelf:
        breadcrumbs = (
            ("Bookcases", reverse("bookcases:bookcase_list")),
            (book.bookshelf.bookcase.name,
                reverse("bookcases:bookcase_detail", args=[book.bookshelf.bookcase.pk])),
            (book.bookshelf.shelf_label,
                reverse("bookcases:bookshelf_detail", args=[book.bookshelf.pk])),
            (book.title, ),
        )

    context = {
        "book": book,
        "breadcrumbs": breadcrumbs
    }

    return render(request, "books/book_detail.html", context)
