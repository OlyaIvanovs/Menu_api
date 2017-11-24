from django.forms import ModelForm
from .models import Recipe, Category

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'method', 'category')
        # fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'