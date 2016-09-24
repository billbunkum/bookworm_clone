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

    if book.bookshelf:
        breadcrumbs = (
            ("Bookcases", reverse("bookcases:bookcase_list")),
            (book.bookshelf.bookcase.name,
                reverse("bookcases:bookcase_detail", args=[book.bookshelf.bookcase.pk])),
            (book.bookshelf.shelf_label,
                reverse("bookcases:bookshelf_detail", args=[book.bookshelf.pk])),
            (book.title, ),
        )
    else:
        breadcrumbs = (
            ("Books", reverse("books:book_list")),
            (book.title, ),
        )

    context = {
        "book": book,
        "breadcrumbs": breadcrumbs
    }

    return render(request, "books/book_detail.html", context)

def book_new(request, bookshelf=None):
    form_kwargs = {}

    if bookshelf:
        form_kwargs = {
            "initial": {"bookshelf": bookshelf}
        }

        breadcrumbs = (
            ("Bookcases", reverse("bookcases:bookcase_list")),
            (bookshelf.bookcase.name,
                reverse("bookcases:bookcase_detail", args=[bookshelf.bookcase.pk])),
            (bookshelf.shelf_label,
                reverse("bookcases:bookshelf_detail", args=[bookshelf.pk])),
        )
    else:
        breadcrumbs = (
            ("Books", reverse("books:book_list")),
        )

    if request.method == "POST":
        form = BookForm(request.POST, **form_kwargs)

        if form.is_valid():
            book = form.save()
            messages.success(request, "Book Saved!")
            return redirect("books:book_detail", id=book.pk)
    else:
        form = BookForm(**form_kwargs)

    context = {
        "form": form,
        "breadcrumbs": breadcrumbs,
    }

    return render(request, "books/book_edit.html", context)

def book_edit(request, id):
    book = get_object_or_404(Book, pk=id)

    if book.bookshelf:
        breadcrumbs = (
            ("Bookcases", reverse("bookcases:bookcase_list")),
            (book.bookshelf.bookcase.name,
                reverse("bookcases:bookcase_detail", args=[book.bookshelf.bookcase.pk])),
            (book.bookshelf.shelf_label,
                reverse("bookcases:bookshelf_detail", args=[book.bookshelf.pk])),
            (book.title, reverse("books:book_detail", args=[book.pk]))
        )
    else:
        breadcrumbs = (
            ("Books", reverse("books:book_list")),
            (book.title, reverse("books:book_detail", args=[book.pk]))
        )

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
        "breadcrumbs": breadcrumbs,
    }

    return render(request, "books/book_edit.html", context)
