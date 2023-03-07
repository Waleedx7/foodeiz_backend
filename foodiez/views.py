from django.urls import path
from rest_framework.generics import CreateAPIView ,ListAPIView 
from foodiez.models import Recipe
from .serializers import RegisterSerializer,RecipeSerializer
from foodiez import serializers

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer

class RecipeListAPIView(ListAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

