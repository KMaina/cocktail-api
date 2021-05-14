from django.urls import path
from .views import (
    CreateListCocktails, SaveFetchedCocktails, UpdateCustomCocktail, SaveRandomFetchedCocktails)

app_name = "drinks"
urlpatterns = [
    path('v1/drinks/',
         CreateListCocktails.as_view(),
         name="cocktail_view"),
    path('v1/drinks/<int:id>',
         UpdateCustomCocktail.as_view(),
         name="cocktail_edit_view"),
    path('v1/fetched-drinks/',
         SaveFetchedCocktails.as_view(),
         name="fetched_cocktail_view"),
    path('v1/fetched-random-drinks/',
         SaveRandomFetchedCocktails.as_view(),
         name="fetched_random_cocktail_view"),
    ]
