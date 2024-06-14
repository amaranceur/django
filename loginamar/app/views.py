from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def home(req):
    return render(req,'app/home.html')
def signup(req):
    
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        pass1 = req.POST['pass1']
        pass2 = req.POST['pass2']
        
        if pass1 != pass2:
           messages.error(req, 'Passwords do not match')
            
        elif User.objects.filter(username=username).exists():
            messages.error(req, 'Username already exists')
            
        elif User.objects.filter(email=email).exists():
            messages.error(req, 'Email already registered')
      
        else:
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.save()
            messages.success(req, 'You have registered successfully')
            user1=authenticate(req,username=username,password=pass1)
            login(req,user1)
            return redirect('home')  # Redirect to the login page or another appropriate page

    return render(req, 'app/signup.html')

def Login(req):
    if req.method == 'POST':
        username = req.POST['username']
        pass1 = req.POST['pass1']
        user = authenticate(req, username=username, password=pass1)
        user2 = authenticate(req, email=username, password=pass1)

        if user is not None :
                login(req, user)
                messages.info(req, 'you login succesfully')
                return redirect('home')
        elif user2 is not None:
                login(req,user2)
                messages.info(req, 'you login succesfully')
                return redirect('home')
        else :
            messages.info(req,'Invalid Username or Password')

    return render(req, 'app/login.html')
