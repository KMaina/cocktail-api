# Generated by Django 3.2.2 on 2021-05-13 19:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strDrink', models.CharField(max_length=100)),
                ('strAlcoholic', models.CharField(choices=[('Alcoholic', 'Alcoholic'), ('Non alcoholic', 'Non alcoholic'), ('Optional alcohol', 'Optional alcohol')], max_length=100)),
                ('strGlass', models.CharField(choices=[('Highball glass', 'Highball glass'), ('Cocktail glass', 'Cocktail glass'), ('Old-fashioned glass', 'Old-fashioned glass'), ('Whiskey Glass', 'Whiskey Glass'), ('Collins glass', 'Collins glass'), ('Pousse cafe glass', 'Pousse cafe glass'), ('Champagne flute', 'Champagne flute'), ('Whiskey sour glass', 'Whiskey sour glass'), ('Cordial glass', 'Cordial glass'), ('Brandy snifter', 'Brandy snifter'), ('Wine Glass', 'Wine Glass'), ('Nick and Nora Glass', 'Nick and Nora Glass'), ('Hurricane glass', 'Hurricane glass'), ('Coffee mug', 'Coffee mug'), ('Shot glass', 'Shot glass'), ('Jar', 'Jar'), ('Irish coffee cup', 'Irish coffee cup'), ('Punch bowl', 'Punch bowl'), ('Pitcher', 'Pitcher'), ('Pint glass', 'Pint glass'), ('Copper Mug', 'Copper Mug'), ('White wine glass', 'White wine glass'), ('Beer mug', 'Beer mug'), ('Margarita glass', 'Margarita glass'), ('Beer pilsner', 'Beer pilsner'), ('Beer Glass', 'Beer Glass'), ('Parfait glass', 'Parfait glass'), ('Mason jar', 'Mason jar'), ('Coupette glass', 'Coupette glass'), ('Martini Glass', 'Martini Glass'), ('Balloon Glass', 'Balloon Glass'), ('Coupe Glass', 'Coupe Glass')], max_length=100)),
                ('strCategory', models.CharField(choices=[('Ordinary Drink', 'Ordinary Drink'), ('Cocktail', 'Cocktail'), ('Milk / Float / Shake', 'Milk / Float / Shake'), ('Other/Unknown', 'Other/Unknown'), ('Cocoa', 'Cocoa'), ('Shot', 'Shot'), ('Coffee / Tea', 'Coffee / Tea'), ('Homemade Liqueur', 'Homemade Liqueur'), ('Punch / Party Drink', 'Punch / Party Drink'), ('Beer', 'Beer'), ('Soft Drink / Soda', 'Soft Drink / Soda')], max_length=100)),
                ('strIngredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, null=True, size=None)),
                ('strMeasures', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, null=True, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
    ]