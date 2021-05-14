from django.http import response
import pytest, json
from django.urls import reverse
from rest_framework import status


class TestDrink:
    """Class to test the drinks app"""
    @pytest.mark.django_db
    def test_create_custom_drink(self, client):
        """This tests to add a new drink"""
        drink = {
            "strDrink": "Reign of Terror",
            "strAlcoholic": "Alcoholic",
            "strGlass": "Jar",
            "strCategory": "Beer",
            "strIngredients": ["Guinness", "Tusker"],
            "strMeasures": ["1 l", "1 l"]
        }
        url = reverse('drinks:cocktail_view')
        response = client.post(url, data=json.dumps(drink), content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_update_custom_drink(self, client, new_drink):
        """This tests to update a custom drink"""
        new_drink.save()
        drink = {
            "strDrink": "Coolness Iced",
            "strAlcoholic": "Non alcoholic"
        }
        url = reverse('drinks:cocktail_edit_view', kwargs={'id':new_drink.id})
        response = client.put(url, data=drink)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update_custom_drink_fails(self, client, new_drink):
        """This tests to update a custom drink"""
        new_drink.save()
        drink = {
            "strDrink": "Coolness Iced",
            "strAlcoholic": "Non alcoholic"
        }
        url = reverse('drinks:cocktail_edit_view', kwargs={'id':2316549})
        response = client.put(url, data=drink)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_get_five_latest_custom_drinks(self, client, new_drink, new_drink2, new_drink3, new_drink4, new_drink5):
        """This tests  to fetch the 5 newest drinks"""
        new_drink.save()
        new_drink2.save()
        new_drink3.save()
        new_drink4.save()
        new_drink5.save()
        url = reverse('drinks:cocktail_view')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_fetch_a_random_drink_from_external_api(self, client):
        """This test to fetch a drink from the cocktail API"""
        url = reverse('drinks:fetched_cocktail_view')
        response = client.get(url)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_fetch_five_random_drinks_from_external_api(self, client):
        """This test to fetch a drink from the cocktail API"""
        url = reverse('drinks:fetched_random_cocktail_view')
        response = client.get(url)
        assert response.status_code == status.HTTP_201_CREATED
