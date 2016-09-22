from django import forms

from .models import Bookcase

class BookcaseForm(forms.ModelForm):

    class Meta:
        model = Bookcase
        fields = ('name', 'description', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "class": "form-control"
        })

        self.fields["description"].widget.attrs.update({
            "class": "form-control"
        })