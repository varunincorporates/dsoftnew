from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = '__all__'

class ReferalForm(forms.ModelForm):
    class Meta:
        model = Referal
        fields = ('myname', 'mymobile', 'referalname', 'referalmobile','referalemail')


class FeasableForm(forms.ModelForm):
    class Meta:
        model = Feasable
        fields = ('city', 'building', 'area', 'pincode')


class NewcustomerForm(forms.ModelForm):
    class Meta:
        model = Newcustomer
        fields = ('name', 'address', 'mobileno', 'email', 'adharcardno', 'adharcard', 'panno', 'pan', 'drivinglicenceno', 'drivinglicence',   'electricityno' , 'electricitybill')
        labels = {
            'pan': _('PAN_Scan'),
            'panno': _('PAN No.'),
            'adharcardno': _('AadhaarNo'),
            'adharcard':_('AadhaarScan'),
            'drivinglicenceno':_('Driving Licence'),
            'drivinglicence':_('D.L. Scan'),
            'electricityno':_('Electricity Consumer No.'),
            'electricitybill':_('Electricity Bill Scan')

        }
        help_texts = {
            'pan': _('Permanent Account Number'),
            'adharcardno': _('Aadhaar Card Unique Number')
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Newcustomer
        fields = ('name', 'address', 'mobileno', 'email', 'adharcardno', 'adharcard', 'panno', 'pan', 'drivinglicenceno', 'drivinglicence',   'electricityno' , 'electricitybill')
        labels = {
            'pan': _('PAN_Scan'),
            'panno': _('PAN No.'),
            'adharcardno': _('AadhaarNo'),
            'adharcard':_('AadhaarScan'),
            'drivinglicenceno':_('Driving Licence'),
            'drivinglicence':_('D.L. Scan'),
            'electricityno':_('Electricity Consumer No.'),
            'electricitybill':_('Electricity Bill Scan')

        }
        help_texts = {
            'pan': _('Permanent Account Number'),
            'adharcardno': _('Aadhaar Card Unique Number')
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }



class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('benefits', 'validity', 'value')

class FaqForm(forms.ModelForm):
    class Meta:
        model = Salesfaq
        fields =  '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Myorder
        fields = '__all__'
