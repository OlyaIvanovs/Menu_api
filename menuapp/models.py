from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    method = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    weeks = models.ManyToManyField('Week')
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='IngredientsRecipes',
        related_name='recipes',
    )

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IngredientsRecipes(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=1)
    addinfo = models.CharField(max_length=50, blank=True)
    unit = models.CharField(max_length=10, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Week(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name