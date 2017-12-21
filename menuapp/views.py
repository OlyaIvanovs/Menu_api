# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RecipeSerializer, CategorySerializer, WeekSerializer
from .models import Recipe, IngredientsRecipes, Category, Week
from django.shortcuts import render

from .forms import  CategoryForm



class RecipeList(APIView):
    def get(self, request):
        week = request.GET.get('week')
        recipes = Recipe.objects.all()
        if week:
            recipes = recipes.filter(weeks__id=week)
        serializer = RecipeSerializer(recipes , many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeekList(APIView):
    def get(self, request):
        weeks = Week.objects.all()
        serializer = WeekSerializer(weeks, many=True)
        return Response(serializer.data)


class WeekDetail(APIView):
    def get(self, request, week_id):
        week = Week.objects.get(id=week_id)
        serializer = WeekSerializer(week);
        return Response(serializer.data)


class RecipeDetail(APIView):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = RecipeSerializer(recipe);
        return Response(serializer.data)

    def put(self, request, recipe_id, format=None):
        recipe = Recipe.objects.get(id=recipe_id)
        data_context = {'week': request.data.get('week', '')}
        serializer = RecipeSerializer(recipe, data=request.data, partial=True, context=data_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        return {"week": self.kwargs['week']}


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


def addRecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('index')
    else:
        form = RecipeForm()

    return render(request, 'add_recipe.html', {'form': form})


def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('index')
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})
