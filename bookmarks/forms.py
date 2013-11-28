from django import forms
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta(object):
        model = Bookmark
        fields = ['url', 'title', 'description', 'private']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-block-level'}),
            'description': forms.Textarea(attrs={'class': 'input-block-level'}),
            'compensation': forms.TextInput(attrs={'class': 'input-block-level'}),
            'location': forms.TextInput(attrs={'class': 'input-block-level'}),
            'employer_name': forms.TextInput(attrs={'class': 'input-block-level'}),
            'employer_website': forms.TextInput(attrs={'class': 'input-block-level'}),
            'contact_name': forms.TextInput(attrs={'class': 'input-block-level'}),
            'contact_email': forms.TextInput(attrs={'class': 'input-block-level'}),
        }
