from django.contrib import admin
from .models import Destination, Contactme, Offer, Engineer, Feasable


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'img','desc','price','offer')


admin.site.register(Destination, DestinationAdmin)


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
