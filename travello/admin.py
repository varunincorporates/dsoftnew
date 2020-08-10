from django.contrib import admin
from .models import *


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'img','desc','price','offer')


admin.site.register(Destination, DestinationAdmin)

class NewcomplainAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'mobile','note' )


admin.site.register(Newcomplain, NewcomplainAdmin)

class ComplainAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Complain, ComplainAdmin )

class NewcustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','mobileno','email')
    list_filter= ('date_created',)
    search_fields= ['name','address','mobileno']


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
    list_display = ('city', 'building', 'area', 'pincode')


admin.site.register(Feasable, FeasableAdmin)


class PlanAdmin(admin.ModelAdmin):
    list_display = ('benefits', 'validity', 'value')


admin.site.register(Plan, PlanAdmin)


class ReferalAdmin(admin.ModelAdmin):
    list_display = ('myname', 'mymobile', 'referalname','referalmobile')
    list_filter = ('referalmobile',)
    search_fields = ['referalname','referalmobile','mymobile']


admin.site.register(Referal, ReferalAdmin)



class TagAdmin(admin.ModelAdmin):
    list_displaye = ('tag')


admin.site.register(Tag, TagAdmin)


class MyorderAdmin(admin.ModelAdmin):
    list_display = ('product','status')

admin.site.register(Myorder, MyorderAdmin)

