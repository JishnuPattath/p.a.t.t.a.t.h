from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"successfully logined")
            print("successfully login")
            return redirect('/')
        else:
            messages.info(request,"invalid")
            print("invalid")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['FirstName']
        second_name = request.POST['SecondName']
        email = request.POST['email']
        password = request.POST['Password']
        cpassword = request.POST['CPassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email taken")
                print("email is taken")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=second_name
                )
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('/')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        return redirect('/')  # Redirect to home page if request method is not POST

    return render(request,'registering.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



