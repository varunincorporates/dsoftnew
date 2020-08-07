from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('success', success, name='success'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('destinations', views.destinations, name='destinations'),
    path('about', views.about, name='about'),
    path('slider', views.slider, name='slider'),
    path('friends', views.friends, name='friends'),
    path('managecustomer', views.managecustomer, name='managecustomer'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('product', views.product, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.createorder, name='create_order'),
    path('update_order/<str:pk>/', views.updateorder, name='update_order'),
    url(r'^display_contact$', display_contact, name="display_contact"),
    url(r'^display_customer$', display_customer, name="display_customer"),
    url('add_contact', views.add_contact, name="add_contact"),
    url('add_customer', views.add_customer, name="add_customer"),
    url('add_referal', views.add_referal, name="add_referal"),
    url(r'^contact/edit_item/(?P<pk>\d+)$', views.edit_contact, name="edit_contact"),
    url(r'^referal/edit_item/(?P<pk>\d+)$', views.edit_referal, name="edit_referal"),
    url('add_feasable', views.add_feasable, name="add_feasable"),
    url(r'^display_feasable$', display_feasable, name="display_feasable"),
    url(r'^feasable/edit_item/(?P<pk>\d+)$', views.edit_feasable, name="edit_feasable"),
    url(r'^feasable/delete_item/(?P<pk>\d+)$', views.delete_feasable, name="delete_feasable"),
    url(r'^display_plan$', display_plan, name="display_plan"),
    url(r'^display_referal$', display_referal, name="display_referal"),
    url('add_plan', views.add_plan, name="add_plan"),
    url('add_newcustomer', views.add_newcustomer, name="add_newcustomer"),
    url(r'^plan/edit_item/(?P<pk>\d+)$', views.edit_plan, name="edit_plan"),
    url(r'^customer/edit_item/(?P<pk>\d+)$', views.edit_customer, name="edit_customer"),
    url(r'^plan/delete_item/(?P<pk>\d+)$', views.delete_plan, name="delete_plan"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
