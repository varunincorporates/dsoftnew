from django import forms
from django.forms import DateInput
from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class ReadOnly(forms.DateInput):
    input_type = 'readonly'


class TimeInput(forms.DateInput):
    input_type = 'time'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_name', 'password1', 'password2' ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class ReferalForm(forms.ModelForm):
    class Meta:
        model = Referal
        fields = ('myname', 'mymobile', 'referalname', 'referalmobile', 'referalemail')


class FeasableForm(forms.ModelForm):
    class Meta:
        model = Feasable
        fields = '__all__'


class NewcustomerForm(forms.ModelForm):
     class Meta:

        widgets = {'dob': DateInput(), 'poidate': DateInput(), 'poadate': DateInput()}

        model = Newcustomer
        fields = '__all__'
        labels = {
            'first_name': _('First_Name'),
            'last_name': _('Last_Name'),
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
        exclude = ('profile_id', 'user')
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Newcustomer
        fields = (
           'first_name','last_name', 'mobileno' , 'address', 'email',
            'poi','poiref','poitype','poiby','poidate',
            'poa', 'poaref', 'poatype', 'poaby', 'poadate','active',
        )
        labels = {
            'poi': _('Proof Of Identity'),
            'poa': _('Proof Of Address'),
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
        exclude = ('profile_id','user')
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


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
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


class ComplainForm1(forms.ModelForm):
    class Meta:
        model = Newcomplain
        fields = ('name', 'mobile', 'email', 'accountno', 'category', 'subject', 'note', 'status')
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
        widgets = {'dateapproval': DateInput() , 'time1approval': TimeInput() }
        model = Installation
        fields = ('phone', 'building', 'flatno', 'type', 'voip', 'userid', 'dateapproval','time1approval',  'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'voip': _('VOIP'),
            'userid': _('UserID'),
            'remarks': _('Comments'),
            'dateapproval': _('ApprovalDate'),
            'time1approval': _('ApprovalTime'),
            'dateococ': _('OCOC_Date'),

        }


class InstallForm(forms.ModelForm):
    class Meta:
        widgets = {'visitdate': DateInput(), 'dateinstalled': DateInput(), 'cablingdate': DateInput()}
        model = Installation
        fields = ('__all__')
        exclude = ('name',)
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'voip': _('VOIP'),
            'userid': _('UserID'),
            'remarks': _('Comments'),
            'dateapproval': _('ApprovalDate'),
            'cablingby': _('CablingDoneBy'),
            'cablingdate': _('CablingDate'),
            'datepayment': _('PaymentRealisedDate'),
            'dateinstalled': _('Installation_Date'),
            'datewo': _('WorkOrderCompletedDate'),
            'visitby': _('VisitBy'),
            'visitdate': _('DateOfVisit'),
            'feedbackdate': _('CustomerFeedbackDate'),
        }
        help_texts = {
            'building': _('Your Society Name'),
            'mobile': _('Your mobile number for correspondence'),
            'email': _('Your eMail number for correspondence'),
            'accountno': _('Your DSoft Consumer Account Number'),
        }


class InstallococForm(forms.ModelForm):
    class Meta:
        widgets = {'dateococ': DateInput(), 'timeococ': TimeInput()}
        model = Installation
        fields = ('phone', 'building', 'flatno', 'type', 'voip', 'userid', 'dateococ','timeococ', 'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'voip': _('VOIP'),
            'userid': _('UserID'),
            'remarks': _('Comments'),
            'dateococ': _('OCOC_Date'),
            'timeococ': _('OCOC Time'),
        }


class InstallcableForm(forms.ModelForm):
    class Meta:
        widgets = {'cablingdate': DateInput(), 'cablingtime': TimeInput()}
        model = Installation
        fields = ('phone', 'building', 'flatno', 'cablingby', 'cablingdate',  'cablingtime', 'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'cablingby': _('CablingDoneBy'),
            'cablingdate': _('CablingDate'),
            'cablingtime': _('CablingTime'),
            'remarks': _('Comments'),
            'dateococ': _('OCOC_Date'),
        }


class InstallpayForm(forms.ModelForm):
    class Meta:
        widgets = {'datepayment': DateInput(), 'timepayment': TimeInput() }

        model = Installation
        fields = ('phone', 'building', 'flatno', 'macid', 'ontdetails','ontsrno', 'datepayment', 'timepayment', 'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'cablingby': _('CablingDoneBy'),
            'datepayment': _('PaymentRealisedDate'),
            'timepayment': _('PaymentRealisedTime'),
            'remarks': _('Comments'),
            'dateococ': _('OCOC_Date'),
            'macid': _('MacID'),
            'ontdetails': _('ONT_Details'),
            'ontsrno': _('ONT_SrNo'),
        }


class InstallstatusForm(forms.ModelForm):
    class Meta:
        widgets = {'datepayment': DateInput(), 'timepayment': TimeInput() }

        model = Installation
        fields = ('status', 'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'cablingby': _('CablingDoneBy'),
            'datepayment': _('PaymentRealisedDate'),
            'timepayment': _('PaymentRealisedTime'),
            'remarks': _('Comments'),
            'dateococ': _('OCOC_Date'),
            'macid': _('MacID'),
            'ontdetails': _('ONT_Details'),
            'ontsrno': _('ONT_SrNo'),
        }



class InstalldateForm(forms.ModelForm):
    class Meta:
        widgets = {'dateinstalled': DateInput(), 'timeinstalled': TimeInput()}
        model = Installation
        fields = ('phone', 'building', 'flatno', 'dateinstalled', 'timeinstalled','remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'cablingby': _('CablingDoneBy'),
            'datepayment': _('PaymentRealisedDate'),
            'remarks': _('Comments'),
            'dateinstalled': _('Installation_Date'),
            'timeinstalled': _('Installation_Time'),
        }


class InstallwoForm(forms.ModelForm):
    class Meta:
        widgets = {'datewo': DateInput(), 'visitdate': DateInput(), 'timewo': TimeInput() }
        model = Installation
        fields = ('phone', 'building', 'flatno', 'visitby', 'visitdate', 'datewo', 'timewo', 'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'cablingby': _('CablingDoneBy'),
            'datepayment': _('PaymentRealisedDate'),
            'remarks': _('Comments'),
            'datewo': _('WorkOrderCompletedDate'),
            'timewo': _('WorkOrderCompletedTime'),
            'visitby': _('VisitBy'),
            'visitdate': _('DateOfVisit'),
        }


class InstallfeedForm(forms.ModelForm):
    class Meta:
        widgets = {'feedbackdate': DateInput(), 'feedbacktime': TimeInput()}
        model = Installation
        fields = ('phone', 'building', 'flatno', 'feedbackdate','feedbacktime', 'remarks')
        labels = {
            'phone': _('PhoneNumber'),
            'building': _('BuildingName'),
            'flatno': _('FlatNo'),
            'cablingby': _('CablingDoneBy'),
            'datepayment': _('PaymentRealisedDate'),
            'remarks': _('Comments'),
            'datewo': _('WorkOrderCompletedDate'),
            'visitby': _('VisitBy'),
            'feedbackdate': _('CustomerFeedbackDate'),
            'feedbacktime': _('CustomerFeedbacktime'),
        }
