from django import forms

from .models import Book
from core.forms import BootstrapFormMixin

class BookForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Book

        fields = (
            'title',
            'wikipedia_url',
            'bookshelf',
            'authors',
            'genres',
        )