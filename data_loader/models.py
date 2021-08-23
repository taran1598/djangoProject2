import math

from django.db import models
from django.db.models import Q


# Create your models here.
class FoodName(models.Model):
    food_id = models.IntegerField(primary_key=True)
    food_code = models.IntegerField()
    food_group_id = models.IntegerField()
    food_source_id = models.IntegerField()
    food_desc = models.CharField(max_length=200)
    food_desc_f = models.CharField(max_length=200)
    # TODO: CHANGE FIELDS TO ACTUAL DATE FIELDS
    food_date_of_entry = models.CharField(max_length=200)
    food_date_of_publication = models.CharField(max_length=200)

    country_code = models.IntegerField(default=None)
    scientific_name = models.CharField(max_length=200, default=None)

    @staticmethod
    def populate_model_food_name_dataframe(df):
        """
        Helper method that populates the FoodName model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_objects = [
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
        FoodName.objects.bulk_create(batch_objects)


class NutrientName(models.Model):
    nutrient_id = models.IntegerField(primary_key=True)
    nutrient_code = models.IntegerField()
    nutrient_symbol = models.CharField(max_length=200)
    nutrient_unit = models.CharField(max_length=200)
    nutrient_name = models.CharField(max_length=200)
    nutrient_decimals = models.IntegerField()

    @staticmethod
    def populate_model_nutrient_name_dataframe(df):
        # TODO: FIND WAY TO GENERALIZE THIS METHOD
        """
        Helper method that populates the NutrientName model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_objects = [
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
        NutrientName.objects.bulk_create(batch_objects)


class NutrientAmount(models.Model):
    food_id = models.ForeignKey(FoodName, on_delete=models.CASCADE)
    nutrient_id = models.ForeignKey(NutrientName, on_delete=models.CASCADE)
    nutrient_value = models.FloatField()
    nutrient_source_id = models.IntegerField()
    nutrient_date_of_entry = models.CharField(max_length=200)

    @staticmethod
    def populate_model_nutrient_amount_dataframe(df):
        """
        Helper method that populates the NutrientAmount model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_objects = [
            NutrientAmount(
                food_id=FoodName.objects.get(food_id=row['FoodID']),
                nutrient_id=NutrientName.objects.get(nutrient_id=row['NutrientID']),
                nutrient_value=row['NutrientValue'],
                nutrient_source_id=row['NutrientSourceID'],
                nutrient_date_of_entry=row['NutrientDateOfEntry'],
            )
            for i, row in df.iterrows()
        ]
        NutrientAmount.objects.bulk_create(batch_objects)


class FoodGroup(models.Model):
    food_group_id = models.IntegerField(primary_key=True)
    food_group_code = models.IntegerField()
    food_group_name = models.CharField(max_length=200)
    food_group_name_french = models.CharField(max_length=200)

    @staticmethod
    def populate_model_food_group_dataframe(df):
        # TODO: FIND WAY TO GENERALIZE THIS METHOD
        """
        Helper method that populates the FoodGroup model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_objects = [
            FoodGroup(
                food_group_id=row['FoodGroupID'],
                food_group_code=row['FoodGroupCode'],
                food_group_name=row['FoodGroupName'],
            )
            for i, row in df.iterrows()
        ]
        FoodGroup.objects.bulk_create(batch_objects)


class MeasureName(models.Model):
    measure_id = models.IntegerField(primary_key=True)
    measure_description = models.CharField(max_length=200)

    @staticmethod
    def populate_model_measure_name_dataframe(df):
        # TODO: FIND WAY TO GENERALIZE THIS METHOD
        """
        Helper method that populates the MeasureName model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_objects = [
            MeasureName(
                measure_id=row['MeasureID'],
                measure_description=row['MeasureDescription'],
            )
            for i, row in df.iterrows()
        ]
        MeasureName.objects.bulk_create(batch_objects)


class ConversionFactor(models.Model):
    food_id = models.ForeignKey(FoodName, on_delete=models.CASCADE)
    measure_id = models.ForeignKey(MeasureName, on_delete=models.CASCADE)
    conversion_factor_value = models.FloatField()
    conversion_factor_date_of_entry = models.CharField(max_length=200)

    @staticmethod
    def populate_model_conversion_factor_dataframe(df):
        # TODO: FIND WAY TO GENERALIZE THIS METHOD
        """
        Helper method that populates the ConversionFactor model from a csv file
        :param df: data frame object that contains the data from the csv file
        """
        batch_objects = [
            ConversionFactor(
                food_id=FoodName.objects.get(food_id=row['FoodID']),
                measure_id=MeasureName.objects.get(measure_id=row['MeasureID']),
                conversion_factor_value=row['ConversionFactorValue'],
                conversion_factor_date_of_entry=['ConvFactorDateOfEntry']
            )
            for i, row in df.iterrows()
        ]
        ConversionFactor.objects.bulk_create(batch_objects)