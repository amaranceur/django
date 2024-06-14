from django.urls import path
from .views import *
urlpatterns = [
    path('',Login.as_view()),
    path('task',task,name="task")
]
