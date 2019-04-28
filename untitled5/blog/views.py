from django.shortcuts import render
from .models import post

posts = [{'author': 'nikhil',
          'title': 'blog post 1',
          'dated': 'march 24 2019',
          'content': 'blog content will be here'},
         {'author': 'suthar',
          'title': 'blog post 2',
          'dated': 'march 24 2019',
          'content': 'blog content will be here'}
        ]

def home(request):
    context={'posts':post.objects.all()}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'about'})
# Create your views here.
