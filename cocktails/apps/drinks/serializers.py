from rest_framework import serializers
from .models import Drink
from cocktails.apps.utility.types import (
    ALCOHOLIC_CONTENT, DRINK_CATEGORY, GLASS_TYPE)


class DrinkSerializer(serializers.ModelSerializer):

    DRINK_CATEGORY = DRINK_CATEGORY
    ALCOHOLIC_CONTENT = ALCOHOLIC_CONTENT
    GLASS_TYPE = GLASS_TYPE

    strDrink = serializers.CharField(max_length=100)
    strIngredients = serializers.ListField(child=serializers.CharField())
    strMeasures = serializers.ListField(child=serializers.CharField())
    strAlcoholic = serializers.ChoiceField(choices=ALCOHOLIC_CONTENT)
    strGlass = serializers.ChoiceField(choices=GLASS_TYPE)
    strCategory = serializers.ChoiceField(choices=DRINK_CATEGORY)

    class Meta:
        model = Drink
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
