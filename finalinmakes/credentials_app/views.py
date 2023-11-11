from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Module

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password0 = request.POST['password0']
        user  = auth.authenticate(username=username,
                                  password=password0)
        if user is not None:
            auth.login(request, user)
            return redirect('/credentials_app/courses')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password0 = request.POST['password0']
        password1 = request.POST['password1']

        if password0==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('/credentials_app/register') #
            else:
                user = User.objects.create_user(username=username,
                                                password=password0)
                user.save();
                #print('User Created')
                return redirect('/credentials_app/login')
        else:
            messages.info(request, "password not matching")
            return redirect('/credentials_app/register') #
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'profile.html')

def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'university.html', context)

def modules(request):
    course = request.GET.get('course')
    modules = Module.objects.filter(course=course)
    context = {'modules': modules}
    return render(request, 'partials/modules.html', context)