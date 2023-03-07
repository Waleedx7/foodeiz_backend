from django.urls import path
from foodiez.views import RecipeListAPIView,UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/',UserCreateAPIView.as_view(), name='recipe-list'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('recipes/',RecipeListAPIView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/',RecipeListAPIView.as_view(), name='recipe-detail'),

    
]