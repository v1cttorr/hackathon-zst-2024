from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PassDinner
from django.shortcuts import redirect
from .models import Client
from django.contrib.auth.models import User

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

@login_required
def pass_diner_to_someone(request):
    if request.method == 'POST':
        form = PassDinner(request.POST)
        if form.is_valid():
            user = Client.objects.get(user=request.user)
            user.how_many_days -= 1
            user.save()

            email = form.cleaned_data.get('email')

            new_user_model = User.objects.get(email=email)
            
            try:
                new_user = Client.objects.get(user=new_user_model)
            except:
                new_user = None
            print(f'-----------{new_user}')
            if new_user == None:
                Client.objects.create(user=new_user_model, how_many_days=1)
            else:
                new_user.how_many_days += 1
                new_user.save()

            return render(request, 'accounts/pass_dinner_complete.html')
    else:
        form = PassDinner()
    
    return render(request, 'accounts/pass_dinner.html', {'form': form})