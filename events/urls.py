from django.contrib import admin
from django.urls import path
from events import views
urlpatterns = [
    path('',views.index, name = 'home'),
    path('login',views.login, name = 'login'),
    path('logout',views.logoutuser, name = 'logout'),
    path('adlog',views.adlog, name = 'adlog'),
    path('adminlog',views.adminlog, name = 'adminlog'),
    path('crt_acc',views.crt_acc, name = 'crt_acc'),
    path('Acc_crt',views.Acc_crt, name = 'Acc_crt'),
    path('poc_crt',views.pocs_crt, name = 'poc_crt'),
    path('crt_comp',views.crt_comp, name = 'crt_comp'),
    path('poc_login',views.poc_login, name = 'poc_login'),
    path('poc_page',views.poc_page, name = 'poc_page'),
    path('comp_details',views.comp_details, name = 'comp_details'),
    path('details_added',views.details_added, name = 'details_added')
]