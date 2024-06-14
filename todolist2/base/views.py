from django.shortcuts import render

# Create your views here.
def about(req):
    return render(req,'base.html')