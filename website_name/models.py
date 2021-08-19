import math

from django.db import models
import pandas


# Create your models here.
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    total_calories = models.IntegerField('Total Calories')
    protein_grams = models.IntegerField('Protein(g)')
    carbohydrate_grams = models.IntegerField('Carbohydrate(g)')
    fat_grams = models.IntegerField('Fats(g)')

    def __str__(self):
        return self.ingredient_name  # defines representation of the object


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredient = models.ManyToManyField(Ingredient)

    # TODO: add calorie count, protein, carbs, fat based off of the ingredients used

    def __str__(self):
        return self.recipe_name


class NutritionLabel(models.Model):
    serving_size = models.IntegerField()
    serving_unit = models.CharField(max_length=200)
    calories = models.IntegerField()
    total_fat = models.IntegerField(default=0)
    saturated_Fat = models.IntegerField(default=0)
    unsaturated_Fat = models.IntegerField(default=0)
    trans_fat = models.IntegerField(default=0)
    cholesterol = models.IntegerField(default=0)
    total_carbs = models.IntegerField(default=0)
    dietary_fiber = models.IntegerField(default=0)
    total_sugar = models.IntegerField(default=0)
    added_sugar = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
