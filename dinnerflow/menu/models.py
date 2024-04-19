from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date

# Create your models here.
    # Create your models here.
class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.TextField()
    meal_price = models.DecimalField(max_digits=5, decimal_places=2)
    allergens = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.meal_name
     
    def delete_after_day(self):
        if self.date < date.today():
            self.delete()
    
    def save(self, *args, **kwargs):
        self.delete_after_day()
        super().save(*args, **kwargs)
