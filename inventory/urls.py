from django.conf.urls import url
from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.inventory, name='inventory'),
    url(r'^accessory$', display_accessory, name="display_accessory"),
    url(r'^oil$', display_oil, name="display_oil"),
    url(r'^3m$', display_3m, name="display_3m"),
    url(r'^others$', display_others, name="display_others"),
    url(r'^add_accessory$', add_accessory, name="add_accessory"),
    url(r'^add_oil$', add_oil, name="add_oil"),
    url(r'^add_3m$', add_3m, name="add_3m"),
    url(r'^add_others$', add_others, name="add_others"),
    url(r'^accessory/edit_item/(?P<pk>\d+)$', edit_accessory, name="edit_accessory"),
    url(r'^oil/edit_item/(?P<pk>\d+)$', edit_oil, name="edit_oil"),
    url(r'^m3/edit_item/(?P<pk>\d+)$', edit_3m, name="edit_3m"),
    url(r'^others/edit_item/(?P<pk>\d+)$', edit_others, name="edit_others"),
    url(r'^accessory/delete_item/(?P<pk>\d+)$', delete_accessory, name="delete_accessory"),
    url(r'^oil/delete_item/(?P<pk>\d+)$', delete_oil, name="delete_oil"),
    url(r'^m3/delete_item/(?P<pk>\d+)$', delete_3m, name="delete_3m"),
    url(r'^others/delete_item/(?P<pk>\d+)$', delete_others, name="delete_others")
]