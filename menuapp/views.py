# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RecipeSerializer
from .models import Recipe, IngredientsRecipes, Ingredient


class RecipeList(APIView):

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes , many=True);
        return Response(serializer.data)

    def post(self):
        pass




def index(request):
    recipes = Recipe.objects.all()
    # all_recipes = Recipe.objects.all()
    # recipes = []
    # for recipe in all_recipes:
    #     r = {};
    #     r['title'] = recipe.title
    #     r['method'] = recipe.method
    #     ingredients = []
    #     all_ingredients = recipe.ingredientsrecipes_set.all()
    #     for item in all_ingredients:
    #         ingredient = {}
    #         ingredient['name'] = item.ingredient.name
    #         ingredient['unit'] = item.ingredient.unit
    #         ingredient['amount'] = item.amount
    #         ingredients.append(ingredient)
    #     r['ingredients'] = ingredients
    #     r['category'] = recipe.category
    #     recipes.append(r)
    context = {
        'recipes': recipes 
    }
    # import ipdb; ipdb.set_trace()
    return render(request, 'index.html', context);
