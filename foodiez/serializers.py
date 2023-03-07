from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Ingredient, Recipe, Rating



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    category = CategorySerializer()
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeDetailSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    category = CategorySerializer()
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'chef', 'category', 'ingredients', 'description', 'image', 'prep_time', 'cook_time', 'servings', 'created_at', 'updated_at']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

