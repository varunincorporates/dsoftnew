from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = ('name',   'email',  'subject', 'message')


class FeasableForm(forms.ModelForm):
    class Meta:
        model =  Feasable
        fields = ('city', 'building', 'area', 'pincode')


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('benefits', 'validity', 'value')


