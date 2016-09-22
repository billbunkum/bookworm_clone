from django import forms

from .models import Bookcase

class BookcaseForm(forms.ModelForm):

    class Meta:
        model = Bookcase
        fields = ('name', 'description', )