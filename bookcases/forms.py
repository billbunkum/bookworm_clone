from django import forms

from .models import Bookcase
from core.forms import BootstrapFormMixin

class BookcaseForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Bookcase
        fields = ('name', 'description', )