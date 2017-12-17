from django.contrib import admin
from .models import Recipe, Ingredient, Category, IngredientsRecipes, WeeksRecipes, Week

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )

class WeekAdmin(admin.ModelAdmin):
    list_display = ('name', )

class IngredientsRecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount', 'unit', 'addinfo')

class WeeksRecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'week')

admin.site.register(Recipe)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Category)
admin.site.register(IngredientsRecipes, IngredientsRecipesAdmin)
admin.site.register(WeeksRecipes, WeeksRecipesAdmin)
