from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.generics import ListCreateAPIView
from cocktails.apps.utility.api_fetch import fetch_single_cocktail, fetch_five_random_drinks
import requests


class CreateListCocktails(APIView):
    """Class to create and retrieve custom cocktails"""
    serializer_class = DrinkSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = {'message': 'success'}
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        drinks = Drink.objects.all().order_by('-created_at')[:5]
        serializer = self.serializer_class(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateCustomCocktail(APIView):
    """Class to update a custom drink"""
    serializer_class = DrinkSerializer

    def put(self, request, id):
        try:
            cocktail_instance = Drink.objects.get(id=id)
        except:
            message = {'error': 'Cocktail does not exist'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = self.serializer_class(
            instance=cocktail_instance,
            data=data,
            partial=True,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SaveFetchedCocktails(APIView):
    serializer_class = DrinkSerializer

    def get(self, request):
        fetched_drink = fetch_single_cocktail()
        serializer = self.serializer_class(fetched_drink)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 


class SaveRandomFetchedCocktails(APIView):
    serializer_class = DrinkSerializer

    def get(self, request):
        fetched_random_drinks = fetch_five_random_drinks()
        print(fetched_random_drinks)
        serializer = self.serializer_class(fetched_random_drinks, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
