from django.urls import path

from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.base, name='base'),
    path('logout/', LogoutView.as_view(next_page='base'), name='logout'),
    path('home/', views.home),
    path('login/', views.Login, name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('password/', views.changepassword, name='change_password'),
    path('account/',views.EditProfile.as_view(), name='account')
    
]
