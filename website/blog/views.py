from django.http import HttpResponse
from django.shortcuts import render

posts=[
    {
    'author':'amaranceur',
    'title': 'blog-post',
    'content':'first post content',
    'date-posted':'14/12/2023'  
    },
        {
    'author':'youssef',
    'title': '2nd blog-post',
    'content':'Second post content',
    'dateposted':'14/12/2023'  
    }
       ]
def index(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
