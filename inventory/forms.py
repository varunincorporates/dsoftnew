from django import forms
from .models import *


class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name',   'img', 'desc', 'mrp', 'prp', 'war', 'category','abc','fms','freezepur','freezesales','offer', 'hnscode', 'gstper', 'uom')


class OilForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'desc', 'mrp', 'prp', 'category', 'hnscode', 'gstper', 'uom')


class M3Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'desc', 'mrp', 'prp', 'category', 'hnscode', 'gstper', 'uom')


class OthersForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'desc', 'mrp', 'prp', 'category', 'hnscode', 'gstper', 'uom')