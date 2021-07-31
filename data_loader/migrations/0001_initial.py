# Generated by Django 3.2.5 on 2021-07-25 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodName',
            fields=[
                ('food_id', models.IntegerField(primary_key=True, serialize=False)),
                ('food_code', models.IntegerField()),
                ('food_group_id', models.IntegerField()),
                ('food_source_id', models.IntegerField()),
                ('food_desc', models.CharField(max_length=200)),
                ('food_desc_f', models.CharField(max_length=200)),
                ('food_date_of_entry', models.CharField(max_length=200)),
                ('food_date_of_publication', models.CharField(max_length=200)),
                ('country_code', models.IntegerField(default=None)),
                ('scientific_name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NutrientAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField()),
                ('nutrient_id', models.IntegerField()),
                ('nutrient_value', models.FloatField()),
                ('nutrient_source_id', models.IntegerField()),
                ('nutrient_date_of_entry', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NutrientName',
            fields=[
                ('nutrient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nutrient_code', models.IntegerField(verbose_name='Nutrient Code')),
                ('nutrient_symbol', models.CharField(max_length=200)),
                ('nutrient_unit', models.CharField(max_length=200)),
                ('nutrient_name', models.CharField(max_length=200)),
                ('nutrient_decimals', models.IntegerField(verbose_name='Nutrient Decimals')),
            ],
        ),
    ]