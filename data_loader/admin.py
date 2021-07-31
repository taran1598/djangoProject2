from django.contrib import admin
from .models import FoodName, NutrientName, NutrientAmount

# Register your models here.
admin.site.register([FoodName, NutrientName, NutrientAmount])