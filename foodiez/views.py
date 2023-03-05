from rest_framework.generics import ListAPIView
from .models import Category, Recipe
from .serializers import CategorySerializer,IngredientSerializer,RecipeSerializer,RatingSerializer

# Create your views here.

class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
