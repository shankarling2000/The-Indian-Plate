from django.contrib.auth import decorators
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'accounts/signin.html')


def home(request):

    return render(request, 'accounts/index.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def about(request):
    return render(request, 'accounts/about.html')

def TableRes(request):
    return render(request, 'accounts/TableRes.html')

def Contactus(request):
    return render(request,'accounts/Contactus.html')

def receipt(request):
    return render(request,'accounts/receipt.html')
