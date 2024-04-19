from django.contrib import admin
from .models import Meal

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Meal, MealAdmin)