from django.db import models
from django.contrib.postgres.fields import ArrayField
from cocktails.apps.utility.types import (
    ALCOHOLIC_CONTENT, DRINK_CATEGORY, GLASS_TYPE)


class Drink(models.Model):
    strDrink = models.CharField(max_length=100)
    strAlcoholic = models.CharField(max_length=100, choices=ALCOHOLIC_CONTENT)
    strGlass = models.CharField(max_length=100, choices=GLASS_TYPE)
    strCategory = models.CharField(max_length=100, choices=DRINK_CATEGORY)
    strIngredients = ArrayField(models.CharField(
        max_length=200, blank=True), blank=True, null=True)
    strMeasures = ArrayField(models.CharField(
        max_length=200, blank=True), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    custom_drink = models.BooleanField(default=False)

    class Meta:
        db_table = "drinks"
