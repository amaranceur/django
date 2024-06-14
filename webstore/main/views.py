from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'main.html', {})
def admin(request):
    if request.method=='POST':
        admin=request.POST['admin']
        password=request.POST['password']
        user = authenticate(username=admin, password=password)
        if user is not None:
          login(request,user)
          messages.success(request,'Welcome admin')
          return  redirect('home')
    return render(request, 'admin_login.html', {})
def logout_(req):
    logout(req)
    return redirect('home') 