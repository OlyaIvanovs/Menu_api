from django.contrib import admin
from .models import Recipe, Ingredient, Category, IngredientsRecipes

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )

class IngredientsRecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount', 'unit', 'addinfo')
    # list_filter = ('recipe', 'ingredient')

admin.site.register(Recipe)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category)
admin.site.register(IngredientsRecipes,IngredientsRecipesAdmin)
