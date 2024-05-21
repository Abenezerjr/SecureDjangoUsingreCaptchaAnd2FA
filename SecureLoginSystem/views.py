from django.shortcuts import render , redirect
from .forms import CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')

def Register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('two_factor:login')

    context={
        'form':form
    }
    return render(request,'SecureLoginSystem/register.html',context)

@login_required(login_url='two_factor:login')
def dashboard(request):
    return render(request,'SecureLoginSystem/dashboard.html')

def login_user(request):
    return render(request,'SecureLoginSystem/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('home')

def accountLocked(request):
    return render(request,'SecureLoginSystem/account _locked.html')





#TODO Passwored management :- user can reset and update the password functionality