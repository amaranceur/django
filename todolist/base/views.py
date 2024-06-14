from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
class Login(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('task')
def task(request):
    context = {
        'username': request.user.username,
        'taskname':task.title
    }    
    return render(request,'base/task.html',context)