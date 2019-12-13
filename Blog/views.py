from django.shortcuts import render,HttpResponse
from .models import Post as PostD

# Create your views here.

def Blog(r):
     Posts = PostD.objects.all().reverse() 
     return render(r,'Blog/Blog.html',{'Posts':Posts}) 

def Post(r,slug):
    Post = PostD.objects.filter(Slug=slug).first()
    return render(r,'Blog/Post.html', {"post": Post})