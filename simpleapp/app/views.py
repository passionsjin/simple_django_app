import socket

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def hello(request):
    print(request)
    info = {'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.getfqdn())
            }
    return render(request, 'main.html', {'contents': info})


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            print('회원가입')
            # auth.login(request, user)
            # return redirect('home')
            return redirect('login')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        print('login')
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')