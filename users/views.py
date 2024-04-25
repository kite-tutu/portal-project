from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            employee_id = form.cleaned_data.get('employee_id')
            member_id = employee_id.zfill(10)
            
            #user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            ''' if user.is_authenticated:
                return redirect('dashboard')
            else: '''
            messages.success(request,f'Your Account has been successfully created. Reach the Admin to activate it before you can log in')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', { 'form' : form })

""" def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Successfully created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

def home(request):
    form = AuthenticationForm()
    #username = form.cleaned_data.get('username')
    return render(request,'users/login.html',{ 'form': form })


def login(request):
    username = ""

    if request.method == 'POST':
       form = AuthenticationForm(request.POST)
       username = self.cleaned_data.get('username')
       return render(request,'portal/dashboard.html',{'username': username})

 """
