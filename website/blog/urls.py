from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='blog-home'),
    path('about/',views.about,name='about-web'),
]
