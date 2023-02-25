from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Автор')
    text = forms.CharField(max_length=2500, required=True, label='Текст', widget=widgets.Textarea)
    email = forms.CharField(max_length=500, required=True, label='Email')

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if len(author) < 2:
            raise ValidationError('Имя должно быть больше 2ух символов')
        return author