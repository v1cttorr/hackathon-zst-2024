from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/login/")
    else:
        form = RegisterForm()
    
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('/')
    return render(request, 'registration/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')

def home(request):
    return redirect('/')