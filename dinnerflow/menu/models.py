from django.db import models

# Create your models here.
class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.TextField()
    meal_price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_image = models.ImageField(upload_to='meal_images')
    allergens = models.CharField(max_length=100)
    
    def __str__(self):
        return self.meal_name