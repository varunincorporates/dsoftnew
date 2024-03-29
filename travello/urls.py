from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', success, name='success'),
    path('register', views.register , name='register'),
    path('indexdas', views.indexdas , name='indexdas'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('destinations', views.destinations, name='destinations'),
    path('about', views.about, name='about'),
    path('document', views.document, name='document'),
    path('slider', views.slider, name='slider'),
    path('friends', views.friends, name='friends'),
    path('userpage', views.userpage, name="userpage"),
    path('managecustomer', views.managecustomer, name='managecustomer'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('maindashboard', views.maindashboard, name='maindashboard'),
    path('dashcomplain', views.dashcomplain, name='dashcomplain'),
    path('product', views.product, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.createorder, name='create_order'),
    path('update_order/<str:pk>/', views.updateorder, name='update_order'),
    path('edit_inst/<str:pk>/', views.edit_inst, name='edit_inst'),
    path('edit_feedback/<str:pk>/', views.edit_feedback, name='edit_feedback'),
    path('edit_pay/<str:pk>/', views.edit_pay, name='edit_pay'),
    path('edit_status/<str:pk>/', views.edit_status, name='edit_status'),
    path('edit_date/<str:pk>/', views.edit_date, name='edit_date'),
    path('edit_wo/<str:pk>/', views.edit_wo, name='edit_wo'),
    path('edit_customer/<str:pk>', views.edit_customer,name='edit_customer'),
    path('edit_ococ/<str:pk>/', views.edit_ococ, name='edit_ococ'),
    path('edit_cable/<str:pk>/', views.edit_cable, name='edit_cable'),
    path('update_complain/<str:pk>/', views.updatecomplain, name='update_complain'),
    path('update_order1/<str:pk>/', views.updateorder1, name='update_order1'),
    url(r'^display_contact$', display_contact, name="display_contact"),
    url(r'^display_customer$', display_customer, name="display_customer"),
    url('add_contact', views.add_contact, name="add_contact"),
    url('add_dashcustomer', views.add_dashcustomer, name="add_dashcustomer"),
    url('add_customer', views.add_customer, name="add_customer"),
    url('add_referal', views.add_referal, name="add_referal"),
    url(r'^contact/edit_item/(?P<pk>\d+)$', views.edit_contact, name="edit_contact"),
    url(r'^referal/edit_item/(?P<pk>\d+)$', views.edit_referal, name="edit_referal"),
    url('add_feasable', views.add_feasable, name="add_feasable"),
    url(r'^display_feasable$', display_feasable, name="display_feasable"),
    url(r'^feasable/edit_item/(?P<pk>\d+)$', views.edit_feasable, name="edit_feasable"),
    url(r'^customer1/edit_item/(?P<pk>\d+)$', views.edit_ord, name="edit_ord"),
    url(r'^feasable/delete_item/(?P<pk>\d+)$', views.delete_feasable, name="delete_feasable"),
    url(r'^dashcomplain/delete_item/(?P<pk>\d+)$', views.delete_dashcomplain, name="delete_dashcomplain"),
    url(r'^dashboard/delete_item/(?P<pk>\d+)$', views.delete_dashboard, name="delete_dashboard"),
    url(r'^customer/delete_item/(?P<pk>\d+)$', views.delete_order, name="delete_order"),
    url(r'^display_plan$', display_plan, name="display_plan"),
    url(r'^display_employee$', display_employee, name="display_employee"),
    url(r'^display_vendor$', display_vendor, name="display_vendor"),
    url(r'^display_assign$', display_assign, name="display_assign"),
    url(r'^display_faq$', display_faq, name="display_faq"),
    url(r'^display_referal$', display_referal, name="display_referal"),
    url('add_plan', views.add_plan, name="add_plan"),
    url('add_employee', views.add_employee, name="add_employee"),
    url('add_vendor', views.add_vendor, name="add_vendor"),
    url('add_assign', views.add_assign, name="add_assign"),
    url('add_faq', views.add_faq, name="add_faq"),
    url('add_newcustomer', views.add_newcustomer, name="add_newcustomer"),
    url('add_newcustomers', views.add_newcustomer, name="add_newcustomer"),
    url('add_complain', views.add_complain, name="add_complain"),
    url('newsletter', views.newsletter, name="newsletter"),
    url('salesfaq', views.salesfaq, name="salesfaq"),
    url(r'^plan/edit_item/(?P<pk>\d+)$', views.edit_plan, name="edit_plan"),
    url(r'^employee/edit_item/(?P<pk>\d+)$', views.edit_employee, name="edit_employee"),
    url(r'^faq/edit_item/(?P<pk>\d+)$', views.edit_faq, name="edit_faq"),
    url(r'^customer/edit_item/(?P<pk>\d+)$', views.edit_customer, name="edit_customer"),
    url(r'^installation/edit_item/(?P<pk>\d+)$', views.edit_installation, name="edit_installation"),
    path('edit_myassignment/<str:pk>/', views.edit_myassignment, name='edit_myassignment'),
    url(r'^plan/delete_item/(?P<pk>\d+)$', views.delete_plan, name="delete_plan"),
    url(r'^faq/delete_item/(?P<pk>\d+)$', views.delete_faq, name="delete_faq"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="travello/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="travello/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="travello/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="travello/password_reset_done.html"),
         name="password_reset_complete"),
]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
