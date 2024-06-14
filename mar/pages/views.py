from django.shortcuts import render
from django.http import HttpResponse
from .models import LOgin
from .forms import Loginform


def index(response):
  return render(response, 'pages/index.html', {'name': 'amar'})



def about(reqeust):
  if reqeust.method=='POST':
    data=Loginform(reqeust.POST)
    if data.is_valid():
        data.save()
     
  return render(reqeust,'pages/about.html',{'lf':Loginform})




# Create your views here.
