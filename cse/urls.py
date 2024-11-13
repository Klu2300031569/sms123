from django.contrib import admin
from django.urls import path
from. import views
from .views import contact_list, contact_add, contact_delete, send_all_contacts

urlpatterns = [
    #path('',views.home,name='home'),
     path('',views.base,name='base'),
    # path('login/',views.login,name='login'),
    # path('logout/',views.logout,name='logout')
    path('timezonepagecall/',views.timezonepagecall,name='t'),
    path('timezonepagelogic/',views.timezonepagelogic,name='timezonepagelogic'),
    path('contactpagecall/',views.contactpagecall,name='contactpagecall'),
    path('contactlogic/',views.contactlogic,name='contactlogic'),
    path('contactList/', contact_list, name='contact_list'),
    path('add/', contact_add, name='contact_add'),
    path('delete/<int:pk>/', contact_delete, name='contact_delete'),
    path('send_all/', send_all_contacts, name='send_all_contacts'),
]
