from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return (self.name)

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    chef = models.ForeignKey(User, on_delete=models.CASCADE,related_name='recipes')
    description = models.TextField()
    image = models.ImageField(upload_to='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='recipes')

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='ratings')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()

class RecipeOfIngrediant(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name='ingrediant_of_recipe')
    ingrediant = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name='recipe_of_ingrediant')
    