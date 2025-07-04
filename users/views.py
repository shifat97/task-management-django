from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import RegisterForm, CustomRegistrationForm
from django.contrib.auth import login, logout, authenticate


def sign_up(request):
    if request.method == 'GET':
        form = CustomRegistrationForm()
    else:
        form = CustomRegistrationForm(request.POST)
        
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # confirm_password = form.cleaned_data.get('password2')

            # if password == confirm_password:
            #     User.objects.create(username=username, password=password)
            # else:
            #     print('Password are not same')
            form.save()

    return render(request, 'registration/register.html', context={
        "form": form
    })

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request=request, username=username, password=password)
        print('Doc', username, password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')