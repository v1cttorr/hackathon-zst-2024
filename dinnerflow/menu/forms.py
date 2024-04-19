from django import forms
from .models import Meal

class Meal_add_form(forms.Form):
    meal_name = forms.CharField(max_length=100)
    meal_description = forms.CharField(widget=forms.Textarea)
    meal_price = forms.DecimalField(max_digits=5, decimal_places=2)
    meal_image = forms.ImageField()
    allergens = forms.MultipleChoiceField(choices=[('gluten', 'Gluten'), ('jaja', 'Jaja'), ('orzechy', 'Orzechy'), ('nabiał', 'Nabiał'), ('sezam', 'Sezam')], widget=forms.CheckboxSelectMultiple)

    class Meta:
        fields = ['meal_name', 'meal_description', 'meal_price', 'meal_image', 'allergens']

    def save(self):
        meal = Meal.objects.create(
            meal_name=self.cleaned_data['meal_name'],
            meal_description=self.cleaned_data['meal_description'],
            meal_price=self.cleaned_data['meal_price'],
            meal_image=self.cleaned_data['meal_image'],
            allergens=self.cleaned_data['allergens']
        )
        return meal
class Meal_edit_form(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'meal_description', 'meal_price', 'meal_image', 'allergens']
