from django.shortcuts import render
from blogapp.forms import NewBlogForm
from django.http import HttpResponse, HttpResponseRedirect
from blogapp import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='blogapp/login/')
def blog(request):
    form  = NewBlogForm
    res = render(request,'blogapp/content.html', {'form':form})
    return res


def add(request):
    if request.method == 'POST':
        blog = models.Blog()
        blog.name=request.POST['Name']
        blog.Gamil=request.POST['Gmail']
        blog.content=request.POST['Content']
        blog.save()
    s="Record Stored<br><a href='/'> Click for a new Blog</a>"
    return HttpResponse(s)

def viewBlog(request):
    blogs = models.Blog.objects.all()
    res=render(request,'blogapp/view_blog.html', {'blogs':blogs})
    return res

def resis(request):
    res = render(request,'blogapp/resister.html')
    return res


def submit(request):
    if request.method == 'POST':
        
        blog = models.Resister()
        blog.username=request.POST['username']
        blog.Gamil=request.POST['Gmail']
        blog.password=request.POST['password']
        blog.save()
    s="Your resistration is Sucessfull <br> Thank You for Resistration <br><a href='/'> Click for a new Blog</a>"
    return HttpResponse(s)

def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            data['error']="Username or Password is incorrect"
            res=render(request,'blogapp/login.html',data)
            return res
    else:
        return render(request,'blogapp/login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('login')