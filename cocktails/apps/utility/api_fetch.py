import requests
from cocktails.apps.drinks.models import Drink

def fetch_single_cocktail():
    fetched_drink = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php')
    r_json = fetched_drink.json()['drinks'][0]
    drink = Drink.objects.create(
        strDrink = r_json['strDrink'],
        strAlcoholic =r_json['strAlcoholic'],
        strGlass=r_json['strGlass'],
        strCategory=r_json['strCategory'],
        strIngredients = [value for key, value in r_json.items() if 'strIngr' in key],
        strMeasures = [value for key, value in r_json.items() if 'strMeas' in key]
    )
    drink.save()
    return drink

def fetch_five_random_drinks():
    fetched_drink = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php')
    random_drinks = []
    num = 0
    while num<6:
        r_json = fetched_drink.json()['drinks'][0]
        drink = Drink.objects.create(
            strDrink = r_json['strDrink'],
            strAlcoholic =r_json['strAlcoholic'],
            strGlass=r_json['strGlass'],
            strCategory=r_json['strCategory'],
            strIngredients = [value for key, value in r_json.items() if 'strIngr' in key],
            strMeasures = [value for key, value in r_json.items() if 'strMeas' in key]
        )
        # import pdb; pdb.set_trace()
        random_drinks.append(drink)
        num+=1
    # import pdb; pdb.set_trace()
    return random_drinks
