from django.conf.urls import url
from django.urls import path
from .import views
from .views import *

urlpatterns=[
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('destinations', views.destinations, name='destinations'),
    path('about', views.about, name='about'),
    path('friends', views.friends, name='friends'),
    path('managecustomer', views.managecustomer, name='managecustomer'),
    url(r'^display_contact$', display_contact, name="display_contact"),
    url('add_contact', views.add_contact, name="add_contact"),
    url(r'^contact/edit_item/(?P<pk>\d+)$', views.edit_contact, name="edit_contact"),
    url('add_feasable', views.add_feasable, name="add_feasable"),
    url(r'^display_feasable$', display_feasable, name="display_feasable"),
    url(r'^feasable/edit_item/(?P<pk>\d+)$', views.edit_feasable, name="edit_feasable"),
    url(r'^feasable/delete_item/(?P<pk>\d+)$', views.delete_feasable, name="delete_feasable"),
    url(r'^display_plan$', display_plan, name="display_plan"),
    url('add_plan', views.add_plan, name="add_plan"),
    url(r'^plan/edit_item/(?P<pk>\d+)$', views.edit_plan, name="edit_plan"),
    url(r'^plan/delete_item/(?P<pk>\d+)$', views.delete_plan, name="delete_plan"),

]