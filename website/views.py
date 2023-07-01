from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check of logging in
    if request.method == 'POST': # у логина метод пост, поэтому так чекаем был логин или нет
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) #готовая функция на джанго
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error in loggin in. Try again")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
