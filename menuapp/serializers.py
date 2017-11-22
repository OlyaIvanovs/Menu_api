from rest_framework import serializers
from .models import Recipe, IngredientsRecipes, Ingredient



class IngredientsRecipesSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='ingredient.name')
    unit = serializers.ReadOnlyField(source='ingredient.unit')

    class Meta:
        model = IngredientsRecipes
        fields = ('name', 'amount', 'unit')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'unit')


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    ingredients = IngredientsRecipesSerializer(source='ingredientsrecipes_set', many=True)

    class Meta:
        model = Recipe
        fields = ('title', 'method', 'category', 'ingredients')