from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    method = models.TextField()
    category = models.ForeignKey('Category')
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='IngredientsRecipes',
        related_name='recipes',
    )

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class IngredientsRecipes(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey('Ingredient')
    amount = models.DecimalField(max_digits=5, decimal_places=1)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name