from django import forms

from .models import Bookcase, Bookshelf
from core.forms import BootstrapFormMixin

class BookcaseForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Bookcase
        fields = ('name', 'description', )

class BookshelfForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Bookshelf
        fields = ('shelf_label', )