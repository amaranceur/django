from django.shortcuts import render
from django.apps import apps
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate 
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import*
from django.shortcuts import redirect
from django.contrib import messages
from django.apps import apps
from django.http import Http404
from .forms import CostumerForm,ProductForm,SallerCreationForm
from django.contrib.auth.hashers import check_password
from django import forms 
# Create your views here.
def home(request):
    saller=Saller()
    product=Product.objects.all()
    
    return render(request, 'home.html', {'product':product,'saller':saller})

def admin(request):
    s=None
    e=None
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        if request.method=='POST':
            admin=request.POST['admin']
            password=request.POST['password']
            user = authenticate(username=admin, password=password)
            
            if user is not None:
                login(request,user)
                s=messages.success(request,'Welcome admin')
                return  redirect('home')
            else:
                e=messages.error(request,'Invalid information')
                return redirect('admin')
        return render(request, 'admin_login.html', {'error':e,'success':s})
def logout_(req):
    logout(req)
    return redirect('home') 
def managment(request,a):
    sallers=Saller.objects.all()
    product=Product.objects.all()
    costumer=Costumer.objects.all()
    context={'sallers':sallers,'product':product,'costumer':costumer}
    return render(request, f'{a}_managment.html', context)

def detailes(req, thing, pk):
    if req.user.is_authenticated:
        try:
            # Convert model name to lowercase to ensure consistency
            thing = thing.lower()
            app_config = apps.get_app_config('main')
            model = app_config.get_model(thing)
            obj = get_object_or_404(model, pk=pk)
            return render(req, f'{thing}_card.html', {'obj': obj})
        except LookupError:
            raise Http404(f"Model {thing} does not exist")
        except model.DoesNotExist:
            raise Http404(f"No {thing} found with id {pk}")
    else:
        messages.error(req, "You must be logged in to do that...")
        return redirect('home')

def delete_(req, thing, pk):
    if req.user.is_authenticated:
        try:
            app_config = apps.get_app_config('main')
            model = app_config.get_model(thing)
            obj = model.objects.get(id=pk)
            obj.delete()
            messages.success(req, f'{thing} has been deleted')
        except model.DoesNotExist:
            raise Http404(f"No {thing} found with id {pk}")
        except LookupError:
            raise Http404(f"Model {thing} does not exist")
        return redirect('managment', a=f'{thing}')
    else:
        messages.success(req, "You must be logged in to do that...")
        return redirect('home')
def create_costumer(request):
    if request.method == 'POST':
        form = CostumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('managment',a='Costumer')  # Replace 'success' with your success URL or view name
    else:
        form = CostumerForm()
    
    return render(request, 'Add_Costumer.html', {'form': form})
def create_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)  # Handle file uploads
            if form.is_valid():
                product = form.save(commit=False)
                if request.user.is_saller():
                    product.saller = request.user.saller_profile
                product.save()
                return redirect('managment', a='Product')  # Ensure 'management' URL pattern exists
        else:
            form = ProductForm()  # This line ensures form is always defined
            if request.user.is_authenticated and request.user.is_saller():
                form.fields['saller'].initial = request.user.saller_profile
                form.fields['saller'].widget = forms.HiddenInput()

        return render(request, 'Add_Product.html', {'form': form})
    else:
        messages.error(request,"You must login first !!!!")
        return redirect('home')
def create_saller(request):
    if request.method == 'POST':
        form = SallerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('managment', a='Saller')
    else:
        form = SallerCreationForm()
    return render(request, 'Add_Saller.html', {'form': form})
    
        
def costumer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if(user):
                costumer = Costumer.objects.get(user=user)
                if check_password(password, user.password):
                    messages.success(request, 'You logged in successfully')
                    login(request,user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'You are not registred as costumer')

        except Costumer.DoesNotExist:
            messages.error(request, 'You are not registred as costumer')
    return render(request, 'Costumer_login.html')
def saller_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                try:
                    saller = Saller.objects.get(user=user)
                    messages.success(request, 'You logged in successfully')
                    login(request, user)
                    return redirect('home')
                except Saller.DoesNotExist:
                    messages.error(request, 'You are not a saller')
            else:
                messages.error(request, 'Invalid username or password')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'Saller_login.html')
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'buy_product.html',{'product':product})
def add_orders(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_costumer():  # Ensure this check is correct as per your user model
                quantity = request.POST['quantity']
                try:
                    quantity = int(quantity)
                except ValueError:
                    messages.error(request, 'Invalid quantity')
                    return redirect('product', pk=pk)

                product = get_object_or_404(Product, id=pk)

                if quantity > product.quantity:
                    messages.error(request, 'Quantity not enough')
                    return redirect('product', pk=pk)
                else:
                    product.buy(quantity=quantity)
                    customer = request.user.customer_profile  # Ensure this relation is correct
                    order = Order.objects.create(
                        name_of_customer=customer,  # Corrected variable name
                        name_of_Product=product,
                        quantity=quantity
                    )
                    messages.success(request, 'This product has been added to your cart')
                    return redirect('product', pk=pk)
            else:
                messages.error(request, 'You must be logged in as a customer to buy this product')
                return redirect('home')
        else:
            messages.error(request, 'You must be logged in')
            return redirect('home')
    return redirect('home')