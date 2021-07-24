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


class FoodName(models.Model):
    food_id = models.IntegerField(primary_key=True)
    food_code = models.IntegerField()
    food_group_id = models.IntegerField()
    food_source_id = models.IntegerField()
    food_desc = models.CharField(max_length=200)
    food_desc_f = models.CharField(max_length=200)
    # TODO: CHANGE FIELDS TO ACTUAL DATE FIELDS
    food_date_of_entry = models.CharField(max_length=200)
    food_date_of_publication =models.CharField(max_length=200)
    country_code = models.IntegerField(default=None)
    scientific_name = models.CharField(max_length=200, default=None)

    @staticmethod
    def populate_model_food_name_dataframe(df):
        """
        Helper method that populates the FoodName model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_food_name_objects = [
            FoodName(
                food_id=row['FoodID'],
                food_code=row['FoodCode'],
                food_group_id=row['FoodGroupID'],
                food_source_id=row['FoodSourceID'],
                food_desc=row['FoodDescription'],
                food_desc_f=row['FoodDescriptionF'],
                food_date_of_entry=row['FoodDateOfEntry'],
                food_date_of_publication="" if math.isnan(row['FoodDateOfPublication']) else row[
                    'FoodDateOfPublication'],
                country_code=-1 if math.isnan(row['CountryCode']) else row['CountryCode'],
                scientific_name="" if math.isnan(row['ScientificName']) else row['ScientificName']
            )
            for i, row in df.iterrows()
        ]
        FoodName.objects.bulk_create(batch_food_name_objects)


class NutrientAmount(models.Model):
    food_id = models.IntegerField()
    nutrient_id = models.IntegerField()
    nutrient_value = models.FloatField()
    nutrient_source_id = models.IntegerField()
    nutrient_date_of_entry = models.CharField(max_length=200)

    @staticmethod
    def populate_model_nutrient_amount_dataframe(df):
        """
        Helper method that populates the NutrientAmount model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_food_name_objects = [
            NutrientAmount(
                food_id=row['FoodID'],
                nutrient_id=row['NutrientID'],
                nutrient_value=row['NutrientValue'],
                nutrient_source_id=row['NutrientSourceID'],
                nutrient_date_of_entry=row['NutrientDateOfEntry'],
            )
            for i, row in df.iterrows()
        ]
        NutrientAmount.objects.bulk_create(batch_food_name_objects)


class NutrientName(models.Model):
    nutrient_id = models.IntegerField(primary_key=True)
    nutrient_code = models.IntegerField('Nutrient Code')
    nutrient_symbol = models.CharField(max_length=200)
    nutrient_unit = models.CharField(max_length=200)
    nutrient_name = models.CharField(max_length=200)
    nutrient_decimals = models.IntegerField("Nutrient Decimals")

    @staticmethod
    def populate_model_nutrient_name_dataframe(df):
        # TODO: FIND WAY TO GENERALIZE THIS METHOD
        """
        Helper method that populates the NutrientName model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_food_name_objects = [
            NutrientName(
                nutrient_id=row['NutrientID'],
                nutrient_code=row['NutrientCode'],
                nutrient_symbol=row['NutrientSymbol'],
                nutrient_unit=row['NutrientUnit'],
                nutrient_name=row['NutrientName'],
                nutrient_decimals=row['NutrientDecimals']
            )
            for i, row in df.iterrows()
        ]
        NutrientName.objects.bulk_create(batch_food_name_objects)
