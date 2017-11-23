from rest_framework import serializers
from .models import Recipe, IngredientsRecipes, Ingredient, Category



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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    ingredients = IngredientsRecipesSerializer(source='ingredientsrecipes_set', many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'method', 'category', 'ingredients')