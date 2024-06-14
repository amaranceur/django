from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('admin_login',admin,name='admin'),
    path('logout/',logout_,name='logout')
]
