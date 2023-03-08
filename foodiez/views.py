from django.urls import path
from rest_framework.generics import CreateAPIView ,ListAPIView , RetrieveUpdateDestroyAPIView
from foodiez.models import Category, Ingredient, Rating, Recipe, RecipeOfIngrediant
from foodiez import serializers

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer

class CategoryListAPIView(ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDetailListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    
class RecipeListAPIView(ListAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeByCategoryAPIView(ListAPIView):
    serializer_class = serializers.RecipeSerializer
    def get_queryset(self):
        recipebycategory = self.kwargs['category']
        return Rating.objects.filter(recipe__category__name=recipebycategory)
    
class IngredientListAPIView(ListAPIView):
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
class IngredientDetailListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()

class RecipeOfIngrediantAPIView(ListAPIView):
    queryset = RecipeOfIngrediant.objects.all()
    serializer_class = serializers.RecipeOfIngrediantSerializer
    
class RatingListAPIView(ListAPIView):
    serializer_class = serializers.RatingSerializer
    def perform_class(self, serializer):
        serializer.save(chef=self.request.user)