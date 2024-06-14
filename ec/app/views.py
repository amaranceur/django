from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.views import LoginView# Create your views here.
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm ,UserChangeForm
from .forms import CustomUserCreationForm as CC 
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required(login_url='login')
def base(req):
   return render(req,'app/home.html') 
def Login(req):
    if req.method == 'POST':
        username=req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None :
            login(req, user)
            messages.success(req,'You successfully Logged in  ')
            return redirect('base')
        elif User.objects.filter(username=username).exists() :
            messages.error(req,'Password false')
            
        else :
            messages.error(req,'We dont have any username With that name')
    return render(req,'app/login.html')

def home(req):
   return render(req,'app/index.html')


class register(FormView):
    template_name = 'app/register.html'
    form_class = CC  # Use the custom form
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('base')
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 != password2:
            messages.error(self.request, "Passwords do not match.")

        if User.objects.filter(username=username).exists():
            messages.error(self.request, "Username already exists.")
        
        user = form.save()

        if user is not None:
            user.email = email
            user.save()
            login(self.request, user)
            return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base')
        return super().get(request, *args, **kwargs)
@login_required(login_url='login')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('base')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change_password.html', {
        'form': form
    })
class EditProfile(UpdateView):
    form_class = UserChangeForm
    template_name='app/settings.html'
    def get_success_url(self):
        return reverse_lazy('base')
    def get_object(self):
        return self.request.user