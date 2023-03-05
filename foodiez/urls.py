from django.urls import path
from foodiez.views import RecipeListView
urlpatterns = [
    path('recipes/',RecipeListView.as_view(), name='recipe-list'),
]