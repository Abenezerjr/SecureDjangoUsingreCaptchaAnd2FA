from django.shortcuts import render , redirect
from .forms import CreateUserForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def Register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={
        'form':form
    }
    return render(request,'SecureLoginSystem/register.html',context)

def dashboard(request):
    return render(request,'SecureLoginSystem/dashboard.html')

def login_user(request):
    return render(request,'SecureLoginSystem/login.html')