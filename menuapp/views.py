# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RecipeSerializer, CategorySerializer
from .models import Recipe, IngredientsRecipes, Ingredient, Category


class RecipeList(APIView):

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes , many=True)
        return Response(serializer.data)

    def post(self):
        pass


class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class RecipeAPI(APIView):

    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = RecipeSerializer(recipe);
        return Response(serializer.data)

    def post(self):
        pass



def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes 
    }
    # import ipdb; ipdb.set_trace()
    return render(request, 'index.html', context);


def recipe(request, recipe_id): 
    recipe = Recipe.objects.get(id=recipe_id)

    context = {
        'recipe': recipe
    }
    return render(request, 'recipe.html', context); 
