# Generated by Django 3.2.5 on 2021-07-25 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_name', '0014_nutrientamount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodName',
        ),
        migrations.DeleteModel(
            name='NutrientAmount',
        ),
        migrations.DeleteModel(
            name='NutrientName',
        ),
    ]
