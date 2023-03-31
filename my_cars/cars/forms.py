import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Car


class AddCarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mark'].empty_label = 'Марка не выбрана'
        self.fields['body'].empty_label = 'Кузов не выбран'

    class Meta:
        model = Car
        fields = ('mark', 'model', 'slug', 'complect', 'body', 'description', 'year', 'photo',)
        wigets = {
            'model': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 50}),
        }

    def clean_year(self):
        year = self.cleaned_data['year']
        if year > datetime.datetime.today().year:
            raise ValidationError('Год не может быть больше текущего!')
        return year
