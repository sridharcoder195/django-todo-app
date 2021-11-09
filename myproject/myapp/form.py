from .models import a
from django import forms


class myform(forms.ModelForm):
    class Meta:
        model = a()
        fields = ['name', 'priority', 'date',]
