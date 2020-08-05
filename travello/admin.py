from django.contrib import admin
from .models import *


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'img','desc','price','offer')


admin.site.register(Destination, DestinationAdmin)


class NewcustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','mobileno','email')


admin.site.register(Newcustomer, NewcustomerAdmin)



class ContactmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject','message' )


admin.site.register(Contactme, ContactmeAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'img' ,'desc','tempelate')


admin.site.register(Offer, OfferAdmin)


class EngineerAdmin(admin.ModelAdmin):
    list_displaye = ('name')


admin.site.register(Engineer, EngineerAdmin)


class FeasableAdmin(admin.ModelAdmin):
    list_displaye = ('city', 'building', 'area', 'pincode')


admin.site.register(Feasable, FeasableAdmin)


class PlanAdmin(admin.ModelAdmin):
    list_displaye = ('benefits', 'validity', 'value')


admin.site.register(Plan, PlanAdmin)


class ReferalAdmin(admin.ModelAdmin):
    list_displaye = ('myname', 'mymobile', 'referalname','referalmobile')


admin.site.register(Referal, ReferalAdmin)
