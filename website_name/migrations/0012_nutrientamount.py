# Generated by Django 3.2.5 on 2021-07-23 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_name', '0011_delete_nutrientamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutrientAmount',
            fields=[
                ('food_id', models.IntegerField()),
                ('nutrient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nutrient_value', models.FloatField()),
                ('nutrient_source_id', models.IntegerField()),
                ('nutrient_date_of_entry', models.CharField(max_length=200)),
            ],
        ),
    ]