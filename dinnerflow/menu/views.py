from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Meal_add_form, Meal_edit_form
from .models import Meal
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Meal_add_form, Meal_edit_form
from .models import Meal

# Create your views here.
def add_meal(request):
    if request.method == "POST":
        form = Meal_add_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/menu/")
    else:
        form = Meal_add_form()
    
    return render(request, "menu/add_meal.html", {"form": form})

# Create your views here.
def add_meal(request):
    if request.method == "POST":
        form = Meal_add_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/menu/")
    else:
        form = Meal_add_form()
    
    return render(request, "menu/add_meal.html", {"form": form})

def edit_meal(request, id):
    meal = Meal.objects.get(id=id)
    if request.method == "POST":
        form = Meal_edit_form(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            return redirect("/menu/")
    else:
        form = Meal_edit_form(instance=meal)
    
    return render(request, "menu/edit_meal.html", {"form": form})