from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def landing_page(request):
    return render(request,'landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})


def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out. Come back soon!')
    return redirect('landing_page')

