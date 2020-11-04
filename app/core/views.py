from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from 

# Create your views here.

@login_required(Login_url='/login')
def index(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'Utilizador e/ou senha inválido. Vá para o gulag.' )
    return redirect('/login/')