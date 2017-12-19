from rest_framework import serializers
from .models import Recipe, IngredientsRecipes, Ingredient, Category, Week


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', )


class IngredientsRecipesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='ingredient.name')

    class Meta:
        model = IngredientsRecipes
        fields = ('unit', 'addinfo', 'amount', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.id')
    ingredients = IngredientsRecipesSerializer(source='ingredientsrecipes_set', many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'method', 'category','ingredients', 'weeks')
        depth = 1

    def to_representation(self, instance):
        representation = super(RecipeSerializer, self).to_representation(instance)
        representation['category'] = instance.category.name       
        return representation

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredientsrecipes_set')
        category_data = validated_data.pop('category')
        category_id, created = Category.objects.get_or_create(id=category_data['id'])
        recipe = Recipe.objects.create(**validated_data, category=category_id)
        for ing in ingredients_data:
            i, created = Ingredient.objects.get_or_create(name=ing['ingredient']['name'])
            IngredientsRecipes.objects.create(recipe=recipe, ingredient=i, unit=ing['unit'], amount=ing['amount'])
        return recipe
