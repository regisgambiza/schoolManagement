from django import forms
from django.forms import ModelForm
from .models import Learner


class MyForm(ModelForm):
    class Meta:
        model = Learner
        fields = ['first_name', 'last_name', 'date_of_birth', 'grade']
