from django.contrib import admin
from .models import FoodName, NutrientName, NutrientAmount, ConversionFactor, MeasureName, FoodGroup

# Register your models here.
admin.site.register([FoodName, NutrientName, NutrientAmount, FoodGroup, MeasureName, ConversionFactor])