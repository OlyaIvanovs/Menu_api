from rest_framework import serializers
from .models import Recipe, IngredientsRecipes, Ingredient



class IngredientsRecipesSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')
    ingredient_unit = serializers.ReadOnlyField(source='ingredient.unit')

    class Meta:
        model = IngredientsRecipes
        fields = ('ingredient_unit', 'ingredient_name', 'amount')


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