from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib import messages


from .models import Book, Author
from .forms import BookForm

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

def book_new(request, bookshelf=None):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save()
            messages.success(request, "Book Saved!")
            return redirect("books:book_detail", id=book.pk)
    else:
        form = BookForm()

    context = {
        "form": form,
    }

    return render(request, "books/book_edit.html", context)

def book_edit(request, id, bookshelf=None):
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            book = form.save()
            messages.success(request, "Book Saved!")
            return redirect("books:book_detail", id=book.pk)
    else:
        form = BookForm(instance=book)

    context = {
        "form": form,
        "book": book,
    }

    return render(request, "books/book_edit.html", context)
