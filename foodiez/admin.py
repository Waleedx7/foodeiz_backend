from django.contrib import admin
from .models import Recipe,Category , Ingredient, RecipeOfIngrediant , Rating
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(RecipeOfIngrediant)
admin.site.register(Ingredient)
admin.site.register(Rating)