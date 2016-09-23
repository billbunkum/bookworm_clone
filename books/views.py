from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Q

from .models import Book, Author

def book_list(request):
    query_set = Book.objects.all()

    query = request.GET.get('q')
    if query:
        authors = Author.objects.filter(name__icontains=query)
        query_set = query_set.filter(
            Q(title__icontains=query) |
            Q(authors__in=authors)
        )
        query_set = query_set.distinct()

    books = query_set

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
