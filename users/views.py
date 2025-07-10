from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
# abc@123#$d

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # confirm_password = form.cleaned_data.get('password2')

            # if password == confirm_password:
            #     User.objects.create(username=username, password=password)
            # else:
            #     print("Passwords are not same")

    return render(request, "register.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def sign_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('sign_in')