import pytest
from cocktails.apps.drinks.models import Drink


@pytest.fixture(scope='function')
def new_drink():
    drink = Drink.objects.create(
                strDrink="Reign of Terror",
                strAlcoholic="Alcoholic",
                strGlass="Jar",
                strCategory="Beer",
                strIngredients=["Guinness", "Tusker"],
                strMeasures=["1 l", "1 l"])
    return drink

@pytest.fixture(scope='function')
def new_drink2():
    drink = Drink.objects.create(
                strDrink="Bubble of Happiness",
                strAlcoholic="Non alcoholic",
                strGlass="Jar",
                strCategory="Beer",
                strIngredients=["Guinness", "Tusker"],
                strMeasures=["1 l", "1 l"])
    return drink

@pytest.fixture(scope='function')
def new_drink3():
    drink = Drink.objects.create(
                strDrink="Kid's Delight",
                strAlcoholic="Non alcoholic",
                strGlass="Copper Mug",
                strCategory="Soft Drink / Soda",
                strIngredients=["Milk", "Honey", "Sugar"],
                strMeasures=["1 l", "1 teaspoon", "1 teaspoon"])
    return drink

@pytest.fixture(scope='function')
def new_drink4():
    drink = Drink.objects.create(
                strDrink="Forget Your Worries",
                strAlcoholic="Alcoholic",
                strGlass="Copper Mug",
                strCategory="Soft Drink / Soda",
                strIngredients=["Vodka", "Rum", "Whiskey"],
                strMeasures=["2 shots", "5 shots", "11 shots"])
    return drink

@pytest.fixture(scope='function')
def new_drink5():
    drink = Drink.objects.create(
                strDrink="New Year's Joy",
                strAlcoholic="Alcoholic",
                strGlass="Highball glass",
                strCategory="Homemade Liqueur",
                strIngredients=["Vodka", "Gin", "Sprite"],
                strMeasures=["3 shots", "2 shots", "300 ml"])
    return drink
