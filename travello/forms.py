from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_name', 'password1', 'password2' ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = '__all__'


class ReferalForm(forms.ModelForm):
    class Meta:
        model = Referal
        fields = ('myname', 'mymobile', 'referalname', 'referalmobile', 'referalemail')


class FeasableForm(forms.ModelForm):
    class Meta:
        model = Feasable
        fields = ('city', 'building', 'area', 'pincode')


class NewcustomerForm(forms.ModelForm):
    class Meta:
        model = Newcustomer
        fields = (
            'name', 'address', 'mobileno', 'email', 'adharcardno', 'adharcard', 'panno', 'pan', 'drivinglicenceno',
            'drivinglicence', 'electricityno', 'electricitybill', 'profile_id')
        labels = {
            'mobileno': _('Mobile'),
            'pan': _('PAN'),
            'panno': _('PAN'),
            'adharcardno': _('Aadhaar'),
            'adharcard': _('Aadhaar'),
            'drivinglicenceno': _('D.L.'),
            'drivinglicence': _('D.L.Image'),
            'electricityno': _('Electricity'),
            'electricitybill': _('Electricity')

        }
        help_texts = {
            'name': _('Your full name'),
            'address': _('Complete address with landmarks and pincode'),
            'mobileno': _('Mobile Number for correspondence'),
            'email': _('eMail Address for correspondence'),
            'pan': _('Scan image of PAN Card'),
            'panno': _('Permanent Account Number'),
            'adharcardno': _('Aadhaar Card Unique Number'),
            'adharcard': _('Scan Image of Aadhaar Card'),
            'drivinglicenceno': _('Driving Licence Number'),
            'drivinglicence': _('Driving Licence Card Image'),
            'electricityno': _('Electricity Consumer No.'),
            'electricitybill': _('Electricity Bill Scan')
        }
        exclude = ('profile_id',)
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Newcustomer
        fields = (
            'name', 'address', 'mobileno', 'email', 'adharcardno', 'adharcard', 'panno', 'pan', 'drivinglicenceno',
            'drivinglicence', 'electricityno', 'electricitybill')
        labels = {
            'pan': _('PAN_Scan'),
            'panno': _('PAN.No.'),
            'adharcardno': _('AadhaarNo'),
            'adharcard': _('AadhaarScan'),
            'drivinglicenceno': _('Driving Licence'),
            'drivinglicence': _('D.L. Scan'),
            'electricityno': _('Electricity Consumer No.'),
            'electricitybill': _('Electricity Bill Scan')

        }
        help_texts = {
            'pan': _('Permanent Account Number'),
            'adharcardno': _('Aadhaar Card Unique Number')
        }
        exclude = ('profile_id',)
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class FaqForm(forms.ModelForm):
    class Meta:
        model = Salesfaq
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Myorder
        fields = '__all__'


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Newcomplain
        fields = ('name', 'mobile', 'email', 'accountno', 'category', 'subject', 'note')
        labels = {
            'name': _('Name'),
            'accountno': _('Account_Number'),
        }
        help_texts = {
            'name': _('Your full name with last name'),
            'mobile': _('Your mobile number for correspondence'),
            'email': _('Your eMail number for correspondence'),
            'accountno': _('Your DSoft Consumer Account Number'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class InstallationForm(forms.ModelForm):
    class Meta:
        model = Installation
        fields = ( 'phone', 'building', 'flatno', 'type', 'voip','userid', 'remarks')




