from django.contrib import admin
from .models import Recipe, Ingredient, Category, IngredientsRecipes

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

class IngredientsRecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    list_filter = ('recipe', 'ingredient')

admin.site.register(Recipe)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category)
admin.site.register(IngredientsRecipes,IngredientsRecipesAdmin)
