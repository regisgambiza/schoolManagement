from django import forms
from django.forms import ModelForm
from .models import Learner, Pace


class MyForm(ModelForm):
    class Meta:
        model = Learner
        fields = ['first_name', 'last_name', 'date_of_birth', 'grade']


class Issue_pace_form(ModelForm):
    class Meta:
        model = Pace
        fields = ['learner', 'subject', 'pace_number', 'completed']