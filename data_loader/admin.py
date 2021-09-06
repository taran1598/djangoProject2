from django.contrib import admin
from .models import FoodName, NutrientName, NutrientAmount, ConversionFactor, MeasureName, FoodGroup, NutrientCsvFiles

# Register your models here.
admin.site.register([NutrientCsvFiles, FoodName, NutrientName, NutrientAmount, FoodGroup, MeasureName, ConversionFactor])