from django.conf import settings
from django.urls import path
from foodiez.views import CategoryListAPIView, IngredientDetailListAPIView, IngredientListAPIView, RatingListAPIView, RecipeListAPIView,UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static

urlpatterns = [
    path("register/",UserCreateAPIView.as_view(), name='recipe-list'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("categories/",CategoryListAPIView.as_view(), name='category-list'),
    path("categories/<int:pk>/",CategoryListAPIView.as_view(), name='category-detail'),
    path("ingredients/",IngredientListAPIView.as_view(), name='ingredient-list'),
    path("ingredients/<int:pk>/",IngredientDetailListAPIView.as_view(), name='ingredient-detail'),
    path("recipes/",RecipeListAPIView.as_view(), name='recipe-list'),
    path("recipes/<int:pk>/",RecipeListAPIView.as_view(), name='recipe-detail'),
    path("ratings/",RatingListAPIView.as_view(), name='rating-list'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)